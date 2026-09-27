### Known working replacement drives

This is an incomplete list of drives that are known to work, or to be
incompatible, with the ATAPI driver Konami used in the BIOS shell and games. The
driver was likely written using an old version of the ATAPI specification as a
reference; CD-ROM drives manufactured in the late 1990s and very early 2000s
have a higher chance of being compatible than drives manufactured later,
possibly due to changes introduced in later revisions of the ATAPI specification
that broke the assumptions Konami's driver makes.

CD-DA playback is particularly problematic as Konami's code seems to be unable
to handle the subtle implementation differences across different drives. To add
insult to injury, some of the few drives that *do* work have bugs in their
subchannel handling that result in incorrect playback status data being reported
to the 573, completely breaking pre-digital-I/O Bemani titles that rely heavily
on audio timing.

| Manufacturer         | Known rebrands | Model          | Type | BIOS    | CD-DA   | Notes                               |
| :------------------- | :------------- | :------------- | :--- | :------ | :------ | :---------------------------------- |
| ASUSTeK              |                | DVD-E616P3     | DVD  | **Yes** | Unknown |                                     |
| Creative             |                | CD4832E        | CD   | **Yes** | No      |                                     |
| Hitachi              |                | CDR-7930       | CD   | **Yes** | No      |                                     |
| LG                   | Compaq         | CRD-8400B      |      | **Yes** | Unknown |                                     |
| LG?                  | Compaq         | CRN-8241B      | CD   | **Yes** | **Yes** | Laptop drive, has CD-DA sync issues |
| LG                   |                | GCE-8160B      | CD   | **Yes** | No      |                                     |
| LG                   |                | GCR-8523B      | CD   | **Yes** | Unknown |                                     |
| LG                   |                | GCR-8525B      | CD   | **Yes** | **Yes** | Has CD-DA sync issues               |
| LG                   |                | GDR-8163B      | DVD  | **Yes** | **Yes** |                                     |
| LG                   | HP             | GDR-8164B      | DVD  | **Yes** | **Yes** |                                     |
| LG                   |                | GH22LP20       | DVD  | **Yes** | Unknown |                                     |
| LG                   |                | GH22NP20       | DVD  | **Yes** | Unknown |                                     |
| ~~LG~~               |                | ~~GSA-4165B~~  | DVD  | No      |         |                                     |
| LG                   |                | GWA-4166B      | DVD  | **Yes** | Unknown |                                     |
| Lite-On              |                | DH-20A4P       |      | **Yes** | Unknown |                                     |
| Lite-On              |                | LH-18A1H       | DVD  | **Yes** | **Yes** |                                     |
| Lite-On              |                | LTD-163        | DVD  | **Yes** | Unknown |                                     |
| Lite-On              |                | LTD-165H       | DVD  | **Yes** | Unknown |                                     |
| Lite-On              |                | LTR-40125S     | CD   | **Yes** | Unknown |                                     |
| Lite-On              |                | SHW-160P6S     | DVD  | **Yes** | Unknown |                                     |
| Lite-On              |                | SOHR-48327S    |      | **Yes** | Unknown |                                     |
| Lite-On              | HP             | SOHR-4839S     | CD   | **Yes** | Unknown | Jitters on CD-RW                    |
| Lite-On              |                | XJ-HD166S      | DVD  | **Yes** | Unknown |                                     |
| Matsushita/Panasonic |                | CR-583         | CD   | **Yes** | **Yes** | Stock drive                         |
| Matsushita/Panasonic |                | CR-587         | CD   | **Yes** | **Yes** | Stock drive, can't read CD-R        |
| Matsushita/Panasonic |                | CR-589B        | CD   | **Yes** | **Yes** | Stock drive                         |
| Matsushita/Panasonic |                | CR-594C        | CD   | **Yes** | Unknown |                                     |
| Matsushita/Panasonic | HP             | SR-8585B       | DVD  | **Yes** | Unknown |                                     |
| Matsushita/Panasonic |                | SR-8589B       | DVD  | **Yes** | Unknown |                                     |
| Matsushita/Panasonic |                | UJDA770        |      | **Yes** | Unknown | Laptop drive                        |
| Mitsumi              |                | CRMC-FX4830T   | CD   | **Yes** | Unknown |                                     |
| NEC                  |                | CDR-1900A      | CD   | **Yes** | Unknown |                                     |
| ~~NEC~~              |                | ~~ND-2510A~~   | DVD  | No      |         |                                     |
| Sony                 | Compaq         | CDU701-Q1      | CD   | **Yes** | Unknown |                                     |
| Sony                 |                | CRX217E        | CD   | **Yes** | Unknown |                                     |
| Sony                 |                | DRU-510A       | DVD  | **Yes** | Unknown |                                     |
| Sony                 |                | DRU-810A       | DVD  | **Yes** | Unknown |                                     |
| TDK                  |                | AI-CDRW241040B | CD   | **Yes** | Unknown |                                     |
| TDK                  |                | AI-481648B     | CD   | **Yes** | Unknown |                                     |
| TEAC                 |                | CD-W552E       | CD   | **Yes** | Unknown |                                     |
| Toshiba              |                | SW-252         |      | **Yes** | Unknown |                                     |
| Toshiba              |                | TS-H292C       | CD   | **Yes** | Unknown |                                     |
| Toshiba              |                | XM-5702B       | CD   | **Yes** | Unknown |                                     |
| Toshiba              |                | XM-6102B       | CD   | **Yes** | **Yes** | Stock drive                         |
| Toshiba              |                | XM-7002B       | CD   | **Yes** | Unknown | Stock drive, laptop drive           |

**NOTE**: Konami shipped some units with a Toshiba XM-7002B laptop drive and a
passive adapter board (`GX874-PWB(B)`) to break out the drive's signals to a
regular 40-pin IDE connector. Laptop drives were also used by Konami in the
`GXA25-PWB(A)` multisession unit.
