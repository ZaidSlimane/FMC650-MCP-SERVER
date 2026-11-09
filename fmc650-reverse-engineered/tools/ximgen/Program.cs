using System; using System.IO; using System.Linq; using System.Reflection; using System.Xml.Linq; using System.Collections.Generic;
using Configuration.Generator; using Configuration.Generator.Factories; using Configuration.Generator.Shared;
using Configuration.Generator.Shared.Mappers; using Configuration.Generator.Shared.Filters;
using Configuration.Generator.Shared.Services; using Configuration.Generator.Interpreters;
using Configuration.Generator.Validation; using Configuration.Generator.Families; using Configuration.Generator.Spec;
using Configurator.Shared.Functional;

class StubKey : IKey {
  public StubKey(int id){ SpecId=id; }
  public string Description => "stub";
  public bool IsValid => true;
  public string KeyString => "stub";
  public string Name => "stub";
  public int SpecId { get; }
}
class StubExt : IExtensionsService {
  readonly Dictionary<int,Key> _keys = new Dictionary<int,Key>();
  public Dictionary<int,Key> Keys => _keys;
  public IKey CanUse(int specId) => new StubKey(specId);
  public void SetAllowedKey(int allowedKey) {}
  public void ClearAllowedKey() {}
  public bool RegisterKey(Key newKey) => true;
  public bool RemoveKey(Key key) => true;
  public void RefreshKeys() {}
  public Result<Guid> RegisterUser() => default(Result<Guid>);
  public Result<Guid> GetUserId() => default(Result<Guid>);
}
class Settings : IConfigurationSettings {
  public List<FamilySettings> FamiliesSettings { get; set; }
  public Version ConfiguratorVersion { get; set; }
}
class P {
  static void Main(){
    string dir=Environment.GetEnvironmentVariable("BUNDLE_DIR") ?? "/tmp/opencode/fmx65analysis/bundle_extract";
    AppDomain.CurrentDomain.AssemblyResolve += (s,e)=>{ var p=Path.Combine(dir,new AssemblyName(e.Name).Name+".dll"); return File.Exists(p)?Assembly.LoadFrom(p):null; };
    void Step(string m){ Console.WriteLine("[step] "+m); Console.Out.Flush(); }
    Step("start");
    var parser=new XElementParser(); Step("parser"); var specFactory=new SpecFactory(parser); var hwInterp=new HardwareVersionInterpreter();
    Step("specFactory+interp"); var hwFactory=new HardwareFactory(specFactory,parser,hwInterp); var swFactory=new SoftwareFactory(hwFactory,parser,specFactory);
    Step("hw+sw factories"); var extFactory=new BaseExtensionFactory(swFactory,parser); IExtensionsService extSvc=new StubExt();
    Step("extFactory+extSvc"); var filter=new ConfigurationFilter(extSvc); var mapper=new ConfigurationMapper(extSvc);
    var inheritor=new ConfigurationVariationInheritor(hwInterp); var hwProv=new HardwareConfigurationProvider();
    Step("filter+mapper+inheritor+hwprov"); var varGen=new ConfigurationVariationGenerator(inheritor,hwProv,mapper,filter);
    Step("varGen"); var cfgParser=new ConfigurationParser(filter); var formatter=new ConfigurationFormatter();
    var compiler=new ConfigurationCompiler(formatter,cfgParser); var validation=new ConfigurationValidation();
    Step("compiler+validation"); var familyCreator=new ConfigurationFamilyCreator();
    string brandDir=Environment.GetEnvironmentVariable("BRAND_DIR") ?? "/tmp/opencode/fmx65analysis/brand/FMB640";
    var specs=new string[0];
    Step("familyCreator"); var fs=new FamilySettings(brandDir,specs,new string[0],false);
    var settings=new Settings{FamiliesSettings=new List<FamilySettings>{fs},ConfiguratorVersion=new Version(1,8,26,0)};
    Step("fs"); var provider=new ConfigurationProviderFactory(settings,extSvc,extFactory,compiler,varGen,cfgParser,validation,familyCreator).Create();
    Step("provider created");
    if(Environment.GetEnvironmentVariable("PROBE_SPEC")=="1"){
      var m=typeof(SpecFactory).GetMethods().First(x=>x.Name=="BuildSpecs");
      Console.WriteLine("BuildSpecs("+string.Join(", ",m.GetParameters().Select(p=>p.ParameterType.FullName+" "+p.Name))+")");
      var sp=new SpecFactory(parser);
      var paths=Directory.GetFiles(brandDir,"Specs.*.xml").Select(Path.GetFullPath).ToList();
      var xels=paths.Select(f=>XDocument.Load(f).Root).ToList();
      foreach(var arg in new object[]{ paths, xels }){
        try{ var r=m.Invoke(sp,new object[]{ new List<int>{1001}, arg }); Console.WriteLine("OK with "+(arg is List<XElement>?"XElements":"paths")+": "+((System.Collections.ICollection)r).Count); }
        catch(Exception e){ Console.WriteLine("FAIL with "+(arg is List<XElement>?"XElements":"paths")+": "+(e.InnerException??e).Message); }
      }
      return;
    }
    var htsTry = provider.AvailableHardwareTypes;
    Step("hw types: "+(htsTry==null?"null":htsTry.Count.ToString()));
    var hwv=new HardwareVersion("FMC650:1");
    Step("hwv="+hwv.Version);
    var hi=new HardwareInformation();
    var gm=provider.GetType().GetMethods().First(m=>m.Name=="GenerateConfiguration");
    var task=System.Threading.Tasks.Task.Run(()=>{
      try{
        var doc=(XDocument)gm.Invoke(provider,new object[]{ hwv,"FMC650",new Version(4,43,1,0),new int[0],"FMB640",hi,1,null });
        doc.Save("/tmp/opencode/fmx65analysis/generated_FMC650_spec1_cfg4.43.1.0.xml");
        var ids=doc.Descendants().Select(x=>(string)x.Attribute("ParameterId")).Where(v=>v!=null).Select(int.Parse).Distinct().OrderBy(x=>x).ToList();
        File.WriteAllLines("/tmp/opencode/fmx65analysis/generated_FMC650_spec1_cfg4.43.1.0_ids.txt", ids.Select(x=>x.ToString()));
        Console.WriteLine("GENERATED elements="+doc.Descendants().Count()+" ids="+ids.Count);
      }catch(Exception e){ Console.WriteLine("gen err: "+(e.InnerException??e)); }
    });
    Console.WriteLine("started, waiting..."); Console.Out.Flush();
    if(!task.Wait(TimeSpan.FromSeconds(80))) Console.WriteLine("GEN TIMEOUT (still running)");
    else Console.WriteLine("gen finished");
  }
}
