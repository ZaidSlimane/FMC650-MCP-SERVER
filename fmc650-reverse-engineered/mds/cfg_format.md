---
title: FMC650 / FMX65 .cfg format
status: text payload byte-exact; container bytes not reproducible
verified: 2026-11-05
---

# `.cfg` format

## Container

A `.cfg` export is **one gzip member**. Example `cfgs/device_export_original.cfg`:

```
size 27,370 B
header 1f 8b 08 00  00 00 00 00  00  0a
       magic       mtime=0       xfl os=10
```

`os = 10` and the deflate stream are produced by the vendor's compressor. All
nine zlib levels, `Z_FILTERED`, .NET `GZipStream`, and the bundled
`ICSharpCode.SharpZipLib.GZipOutputStream` (levels 1–9) were tried against the
sample; **none reproduces the 27,370 bytes** (closest: SharpZipLib level 5 →
27,423 B, header `… 00 FF`). Byte-exact *text* is therefore the reproducible
contract; byte-exact container bytes are not, and are not needed for upload —
the device parses the inflated text.

## Text payload

One line, no trailing newline, `;`-delimited:

```
ConfigurationVersion:4.43.1.0;HwVersion:FMC650_1;Title:03.01.01+ (Automatic source);FmType:FMC650;SpecId:1;
100:1;101:1;102:0;103:30;104:30000;…;181334:0;10:FMC650DEMO;
```

Header keys, in this fixed order: `ConfigurationVersion`, `HwVersion`, `Title`,
`FmType`, `SpecId`.

## Parsing rule (matters)

A new parameter starts only at a token matching `^(\d+):` whose id is **greater
than the previous id**. Anything else is a continuation of the previous value.

The sample contains exactly one continuation:

```
181334: 0;10:FMC650DEMO
```

i.e. the raw value of 181334 is `0;10:FMC650DEMO`. A naive `split(';')` parser
invents a parameter `10` and corrupts both entries.

## Verified round-trip

```
$ python3 tools/cfg_tool.py verify cfgs/device_export_original.cfg
text_identical: True
sha256_original: a1c8c712e5de0d71ae19fb81445b3e2e448cdb949964f076b23e6ef7184c315d
sha256_rebuilt : a1c8c712e5de0d71ae19fb81445b3e2e448cdb949964f076b23e6ef7184c315d
params=11688 header={'ConfigurationVersion': '4.43.1.0', 'HwVersion': 'FMC650_1',
 'Title': '03.01.01+ (Automatic source)', 'FmType': 'FMC650', 'SpecId': '1'}
```

`read` → JSON, `write` → gzip (mtime 0), `verify` → parse/rebuild/compare.

## Value types seen in the sample

| Type | Count | Encoding |
| --- | --- | --- |
| integer | 11,388 | decimal |
| float | 5 | decimal point (`147:0.5`) |
| string | 50 | raw text, may be empty (`801:`) |
| empty | 245 | `id:;` |

Strings are not quoted or escaped; an empty value is legal and distinct from a
missing id. The device rejects a cfg whose id set does not match its
firmware/hardware/spec, which is why the id set — not the labels — is the
thing that must be complete.
