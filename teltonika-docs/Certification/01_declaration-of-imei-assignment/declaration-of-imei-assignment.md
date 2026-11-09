---
title: FMC650 Declaration of IMEI assignment
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_Declaration_of_IMEI_assignment
archived-snapshot: https://web.archive.org/web/20260609232427/https://wiki.teltonika-gps.com/view/FMC650_Declaration_of_IMEI_assignment
captured: 2026-11-04
---

# FMC650 Declaration of IMEI assignment

The International Mobile Equipment Identity or IMEI /aɪˈmiː/ is a number, usually unique, to identify 3GPP and iDEN mobile phones, as well as some satellite phones. It is usually found printed inside the battery compartment of the phone, but can also be displayed on-screen on most phones by entering *#06# on the dialpad, or alongside other system information in the settings menu on smartphone operating systems.

# Description

The IMEI number is used by a GSM network to identify valid devices and therefore can be used for stopping a stolen phone from accessing that network. For example, if a mobile phone is stolen, the owner can call their network provider and instruct them to blacklist the phone using its IMEI number. This renders the phone useless on that network and sometimes other networks too, whether or not the phone's subscriber identity module (SIM) is changed.

# Structure of the IMEI and IMEISV (IMEI software version)

The IMEI (15 decimal digits: 14 digits plus a check digit) or IMEISV (16 decimal digits: 14 digits plus two software version digits) includes information on the origin, model, and serial number of the device. The structure of the IMEI/SV is specified in [3GPP TS 23.003](http://www.3gpp.org/ftp/Specs/html-info/23003.htm). The model and origin comprise the initial 8-digit portion of the IMEI/SV, known as the Type Allocation Code (TAC). The remainder of the IMEI is manufacturer-defined, with a Luhn check digit at the end. For the IMEI format prior to 2003, the GSMA guideline was to have this Check Digit always transmitted to the network as zero. This guideline seems to have disappeared for the format valid from 2003 and onwards.

As of 2004, the format of the IMEI is *AA-BBBBBB-CCCCCC-D*, although it may not always be displayed this way. The IMEISV does not have the Luhn check digit but instead has two digits for the Software Version Number (SVN), making the format *AA-BBBBBB-CCCCCC-EE*

Prior to 2002, the TAC was six digits long and was followed by a two-digit Final Assembly Code (FAC), which was a manufacturer-specific code indicating the location of the device's construction.
From January 1, 2003 until that April 1, 2004, the FAC for all phones was 00.
After April 1, 2004, the Final Assembly Code ceased to exist and the Type Allocation Code increased to eight digits in length.

In any of the above cases, the first two digits of the TAC are the Reporting Body Identifier, which identifies the GSMA-approved group that allocated the TAC. The RBI numbers are allocated by the Global Decimal Administrator. IMEI numbers being decimal allows them to be distinguished from a MEID, which is hexadecimal and always has 0xA0 or larger as its first two hexadecimal digits.

For example, the old style IMEI code 35-209900-176148-1 or IMEISV code 35-209900-176148-23 tells us the following:

**TAC**: 35-2099 - issued by the BABT (code 35) with the allocation number 2099
**FAC**: 00 - indicating the phone was made during the transition period when FACs were being removed.
**SNR**: 176148 - uniquely identifying a unit of this model
**CD**: 1 so it is a GSM Phase 2 or higher
**SVN**: 23 - The "software version number" identifying the revision of the software installed on the phone. 99 is reserved.

By contrast, the new style IMEI code 49-015420-323751 has an 8-digit TAC of 49-015420.

The new CDMA Mobile Equipment Identifier (MEID) uses the same basic format as the IMEI.

| — | — |
| --- | --- |

You can the find PDF version of the MeiGLink SLM320 SLM320-E SLM320-L Declaration of IMEI assignment **[here](https://web.archive.org/images/c/cb/Declaration_of_IMEI_assignment%2C_MeiGLink_SLM320_SLM320-E_SLM320-L%2C_2026-04-14.pdf)**.
