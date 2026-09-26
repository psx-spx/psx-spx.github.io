#   CDROM File Formats
#### Official PSX File Formats
[CDROM File Official Sony File Formats](#cdrom-file-official-sony-file-formats)<br/>

#### Executables
[CDROM File Playstation EXE and SYSTEM.CNF](executables.md#cdrom-file-playstation-exe-and-systemcnf)<br/>
[CDROM File PsyQ .CPE Files (Debug Executables)](executables.md#cdrom-file-psyq-cpe-files-debug-executables)<br/>
[CDROM File PsyQ .SYM Files (Debug Information)](executables.md#cdrom-file-psyq-sym-files-debug-information)<br/>

#### Video Files
[CDROM File Video Texture Image TIM/PXL/CLT (Sony)](graphics.md#cdrom-file-video-texture-image-timpxlclt-sony)<br/>
[CDROM File Video Texture/Bitmap (Other)](graphics.md#cdrom-file-video-texturebitmap-other)<br/>
[CDROM File Video 2D Graphics CEL/BGD/TSQ/ANM/SDF (Sony)](graphics.md#cdrom-file-video-2d-graphics-celbgdtsqanmsdf-sony)<br/>
[CDROM File Video 3D Graphics TMD/PMD/TOD/HMD/RSD (Sony)](graphics.md#cdrom-file-video-3d-graphics-tmdpmdtodhmdrsd-sony)<br/>
[CDROM File Video STR Streaming and BS Picture Compression (Sony)](streaming.md#cdrom-file-video-str-streaming-and-bs-picture-compression-sony)<br/>

#### Audio Files
[CDROM File Audio Single Samples VAG (Sony)](audio.md#cdrom-file-audio-single-samples-vag-sony)<br/>
[CDROM File Audio Sample Sets VAB and VH/VB (Sony)](audio.md#cdrom-file-audio-sample-sets-vab-and-vhvb-sony)<br/>
[CDROM File Audio Sequences SEQ/SEP (Sony)](audio.md#cdrom-file-audio-sequences-seqsep-sony)<br/>
[CDROM File Audio Other Formats](audio.md#cdrom-file-audio-other-formats)<br/>
[CDROM File Audio Streaming XA-ADPCM](audio.md#cdrom-file-audio-streaming-xa-adpcm)<br/>
[CDROM File Audio CD-DA Tracks](audio.md#cdrom-file-audio-cd-da-tracks)<br/>

#### Virtual Filesystem Archives
PSX titles are quite often using virtual filesystems, with numerous custom file
archive formats.<br/>
[CDROM File Archives with Filename](archives.md#cdrom-file-archives-with-filename)<br/>
[CDROM File Archives with Offset and Size](archives.md#cdrom-file-archives-with-offset-and-size)<br/>
[CDROM File Archives with Offset](archives.md#cdrom-file-archives-with-offset)<br/>
[CDROM File Archives with Size](archives.md#cdrom-file-archives-with-size)<br/>
[CDROM File Archives with Chunks](archives.md#cdrom-file-archives-with-chunks)<br/>
[CDROM File Archives with Folders](archives.md#cdrom-file-archives-with-folders)<br/>
[CDROM File Archives in Hidden Sectors](archives.md#cdrom-file-archives-in-hidden-sectors)<br/>
More misc stuff...<br/>
[CDROM File Archive HED/DAT/BNS/STR (Ape Escape)](archives.md#cdrom-file-archive-heddatbnsstr-ape-escape)<br/>
[CDROM File Archive WAD.WAD, BIG.BIN, JESTERS.PKG (Crash/Herc/Pandemonium)](archives.md#cdrom-file-archive-wadwad-bigbin-jesterspkg-crashhercpandemonium)<br/>
[CDROM File Archive BIGFILE.BIG (Gex)](archives.md#cdrom-file-archive-bigfilebig-gex)<br/>
[CDROM File Archive BIGFILE.DAT (Gex - Enter the Gecko)](archives.md#cdrom-file-archive-bigfiledat-gex-enter-the-gecko)<br/>
[CDROM File Archive FF9 DB (Final Fantasy IX)](archives.md#cdrom-file-archive-ff9-db-final-fantasy-ix)<br/>
[CDROM File Archive Ace Combat 2 and 3](archives.md#cdrom-file-archive-ace-combat-2-and-3)<br/>
[CDROM File Archive NSD/NSF (Crash Bandicoot 1-3)](archives.md#cdrom-file-archive-nsdnsf-crash-bandicoot-1-3)<br/>
[CDROM File Archive STAGE.DIR and *.DAT (Metal Gear Solid)](archives.md#cdrom-file-archive-stagedir-and-dat-metal-gear-solid)<br/>
[CDROM File Archive DRACULA.DAT (Dracula)](archives.md#cdrom-file-archive-draculadat-dracula)<br/>
[CDROM File Archive Croc 1 (DIR, WAD, etc.)](archives.md#cdrom-file-archive-croc-1-dir-wad-etc)<br/>
[CDROM File Archive Croc 2 (DIR, WAD, etc.)](archives.md#cdrom-file-archive-croc-2-dir-wad-etc)<br/>
[CDROM File Archive Headerless Archives](archives.md#cdrom-file-archive-headerless-archives)<br/>
Using archives can avoid issues with the PSX's poorly implemented ISO
filesystem: The PSX kernel supports max 800h bytes per directory, and lacks
proper caching for most recently accessed directories (additionally, some
archives can load the whole file/directory tree from continous sectors, which
could be difficult in ISO filesystems).<br/>

#### Compression
[CDROM File Compression](compression.md#cdrom-file-compression)<br/>

#### Misc
[CDROM File XYZ and Dummy/Null Files](compression.md#cdrom-file-xyz-and-dummynull-files)<br/>

#### General CDROM Disk Images
[CDROM Disk Images CCD/IMG/SUB (CloneCD)](diskimages.md#cdrom-disk-images-ccdimgsub-clonecd)<br/>
[CDROM Disk Images CDI (DiscJuggler)](diskimages.md#cdrom-disk-images-cdi-discjuggler)<br/>
[CDROM Disk Images CUE/BIN/CDT (Cdrwin)](diskimages.md#cdrom-disk-images-cuebincdt-cdrwin)<br/>
[CDROM Disk Images MDS/MDF (Alcohol 120%)](diskimages.md#cdrom-disk-images-mdsmdf-alcohol-120)<br/>
[CDROM Disk Images NRG (Nero)](diskimages.md#cdrom-disk-images-nrg-nero)<br/>
[CDROM Disk Image/Containers CDZ](diskimages.md#cdrom-disk-imagecontainers-cdz)<br/>
[CDROM Disk Image/Containers ECM](diskimages.md#cdrom-disk-imagecontainers-ecm)<br/>
[CDROM Subchannel Images](diskimages.md#cdrom-subchannel-images)<br/>
[CDROM Disk Images Other Formats](diskimages.md#cdrom-disk-images-other-formats)<br/>

#### FILENAME.EXT
The BIOS seems to support only (max) 8-letter filenames with 3-letter
extension, typically all uppercase, eg. "FILENAME.EXT". Eventually, once when
the executable has started, some programs might install drivers for long
filenames(?)<br/>

The PSX uses the standard CDROM ISO9660 filesystem without any encryption (ie.
you can put an original PSX CDROM into a DOS/Windows computer, and view the
content of the files in text or hex editors without problems).<br/>

#### Note
MagDemoNN is short for "Official U.S. Playstation Magazine Demo Disc NN"<br/>



##   CDROM File Official Sony File Formats
#### Official Sony File Formats
<https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Filefrmt.pdf> - Sony 1998<br/>
```
  File Formats
    (c) 1998 Sony Computer Entertainment Inc.
    Publication date: November 1998
  Chapter 1: Streaming Audio and Video Data
    STR: Streaming (Movie) Data                               1-3
    BS: MDEC Bitstream Data                                   1-8
    XA: CD-ROM Voice Data                                     1-31
  Chapter 2: 3D Graphics
    RSD: 3D Model Data [RSD,PLY,MAT,GRP,MSH,PVT,COD,MOT,OGP]  2-3
    TMD: Modeling Data for OS Library                         2-24
    PMD: High-Speed Modeling Data                             2-35
    TOD: Animation Data                                       2-40
    HMD: Hierarchical 3D Model, Animation and Other Data      2-49
  Chapter 3: 2D Graphics
    TIM: Screen Image Data                                    3-3
    SDF: Sprite Editor Project File                           3-8
    PXL: Pixel Image Data                                     3-11
    CLT: Palette Data                                         3-14
    ANM: Animation Information                                3-16
    TSQ: Animation Time Sequence                              3-22
    CEL: Cell Data                                            3-23
    BGD: BG Map Data                                          3-27
  Chapter 4: Sound
    SEQ: PS Sequence Data                                     4-3
    SEP: PS Multi-Track Sequence Data                         4-3
    VAG: PS Single Waveform Data                              4-5
    VAB: PS Sound Source Data [VAB and VH/VB]                 4-5
    DA: CD-DA Data                                            4-7
  Chapter 5: PDA and Memory Card
    FAT: Memory Card File System Specification                5-3
```
Most games are using their own custom file formats. However, VAG, VAB/VH(VB,
STR/XA, and TIM are quite popular (because they are matched to the PSX
low-level data encoding). Obviously, EXE is also very common (although not
included in the above document).<br/>
