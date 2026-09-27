#   Pinouts - SIO Pinouts
#### Serial Port
That port exists only on original Playstation (not on the PSone). The shape of
the Serial Port is identical to the 12pin Multiout (audio/video) port, but with
only 8pins.<br/>
```
  1 SIO1 In  RXD receive data    (from remote TXD)
  2 SIO2 -   VCC +3.5VDC         (supply, eg. for voltage conversion)
  3 SIO3 In  DSR                 (from remote DTR)           _________________
  4 SIO4 Out TXD transmit data   (to remote RXD)            |                 |
  5 SIO5 In  CTS clear to send   (from remote RTS)          | 8 7 6 5 4 3 2 1 |
  6 SIO6 Out DTR                 (to remote DSR)            |_________________|
  7 SIO7 -   GND Ground          (supply, eg. for voltage conversion)
  8 SIO8 Out RTS request to send (to remote CTS)
  Shield     GND Ground          (to/from remote GND)
```
Can be used to communicate with another PSX via simple cable connection. With
an external RS232 adaptor (for voltage conversion) it could be also used to
communicate with a PC, a mouse, a modem, etc.<br/>

#### PSone Serial Port
The PSone doesn't have an external serial connector, however, easy to use
soldering points for serial port signals are found as cluster of 5 soldering
points (below CPU pin52), and a single soldering point (below CPU pin100),
arranged like so (on PM-41 boards) (might be different on PM-41(2) boards):<br/>
```
                     CPU70.RTS
               CPU71.CTS   CPU74.TxD
                     CPU72.DTR   CPU75.RxD                       CPU73.DSR
```
The three outputs (RTS,DTR,TXD) are left floating, the RXD input is wired via a
1K ohm pull-up resistor to 3.5V, the other two inputs (CTS,DSR) are wired via
1K ohm pull-down resistors to GND.<br/>
If you want to upgrade the PSone, remove that resistors, and then install the
PSX-style serial circuit (as shown below), or, think of a more simplified
circuit without (dis-)inverted signals.<br/>

#### PSX Serial Port Connection (PU-23 board) (missing on PM-41 board)
The PSX serial circuit basically consists of a few transistors, diodes, and
resistors. The relevant part is that most of the signals are inverted -
compared with RS232 signals, the CPU uses normal high/low levels (of course
with 0V and 3.5V levels, not -12V and +12V), and the signals at the serial port
socket are inverted. Ie. if you want to built a RS232 adaptor, you must either
externally undo the inversion, or, disconnect the transistors, and wire your
circuit directly to the CPU signals.<br/>
```
  SIO8    SIO6    SIO4    SIO1    SIO3    SIO5    SIO2    SIO7---GND
    |       |       |       |       |       |      |
  FB112   FB114   FB116   FB115   FBnnn   FBnnn    o--L102-------3.5V
    |       |       |       |       |       |
    |       |       o-------|-------|-------|--------diode-------GND
    |       |       |       o-------|-------|--------diode-------GND
    |       |       |       |       o-------|--------diode-------GND
    |       |       |       |       |       o--------diode-------GND
    |       |       |       |       |       |
    |       |       |       o-------|-------|--------[1K]--------3.5V
    |       |       |       |       o-------|--------[1K]--------3.5V
   [22]    [22]    [22]    [22]     |       o--------[1K]--------3.5V
    |       |       |       |       |       |
   Q105-----|-------|-------|-------|-------|--------------------GND
    |      Q105-----|-------|-------|-------|--------------------GND
    |       |       |       |      Q106-----|--------------------GND
    |       |       |       |       |      Q106------------------GND
    |       |       |       |       |       |
    |       |       |       |       o-------|--------[470]-------3.5V
    |       |       |       |       |       o--------[470]-------3.5V
    |       |       |       |       |       |
   RTS     DTR     TxD     RxD     DSR     CTS
  CPU70   CPU72   CPU74   CPU75   CPU73   CPU71   <-- CPU Pin Numbers
   out     out     out     in      in      in
```
All six signals are passed through fuses (or loops or so). The three inputs
have 1K ohm pull-ups, and diodes as protection against negative voltages, two
of the inputs are inverted via transistors, with 470 ohm pull-ups at the CPU
side, the other input is passed through 22 ohm to the CPU. The three outputs
are also passed through 22 ohm, one of them having a diode as negative voltage
protection, the other two are inverted via transistors (which may also serve as
negative voltage protection).<br/>
Note that there is no positive voltage protection (ie. +12V inputs would do no
good, also strong -12V inputs might overheat the diodes/fuses, so if you want
to use RS232 voltages, better use a circuit for voltage conversion).<br/>

#### Serial RS232 Adaptor
The PSX serial port uses 0V/3.5V logic, whilst RS232 uses -5V/+5V...-15V/+15V
logic. An example circuit for converting the logic levels would be:<br/>
```
    PSX.VCC--+||--PSX.GND  PSX.GND----DSUB.5.GND----DSUB.SHIELD  DSUB.1,9----NC
                   ______                                 ______
  ,-----------||+-|1   16|-------PSX.VCC ,-----------||+-|1   16|-------PSX.VCC
  | PSX.GND---||+-|2   15|-------PSX.GND | PSX.GND---||+-|2   15|-------PSX.GND
  '---------------|3   14|----DSUB.3.TXD '---------------|3   14|--- N/A
         ,---+||--|4   13|----DSUB.2.RXD        ,---+||--|4   13|--- N/A
         '--------|5   12|-------PSX.RXD        '--------|5   12|--- N/A
    PSX.GND--+||--|6   11|-------PSX.TXD   PSX.GND--+||--|6   11|--- N/A
    DSUB.7.RTS----|7   10|--o<|--PSX.RTS   DSUB.4.DTR----|7   10|--o<|--PSX.DTR
    DSUB.8.CTS----|8    9|--|>o--PSX.CTS   DSUB.6.DSR----|8    9|--|>o--PSX.DSR
                  |______|                               |______|
```
Parts List: 1 or 2 MAX232 chips (voltage conversion), 0 or 1 7400 (NAND, used
as inverter), 4 or 8 1uF/16V capacitors, 1x 10uF/16V capacitor, 1x 9pin male
SubD plug.<br/>
The four inverters are needed only for external adapters (which need to undo
the transistor inversion on the PSX mainboard) (ie. the inverters are not
needed when when connecting the circuit directly to the PSX CPU).<br/>
The second MAX232 chip is needed only if DTR/DSR "not ready" conditions are
required (for an "always ready" condition: DSUB.4.DTR can be wired to -8.5V,
which is available at Pin6 of the first MAX232 chip, and PSX.DSR can be wired
to +3.5V).<br/>
With the above DSUB pin numbers, peripherals like mice or modems can be
connected directly to the circuit. For connection to another computer, use a
"null modem" cable (with crossed RXD/TXD, RTS/CTS, DTR/DSR wires).<br/>
The circuit works with both VCC=5V (default for MAX232) and with VCC=3.5V
(resulting in slightly weaker signals, but still strong enough even for serial
mice; which are mis-using the RS232 signals as power supply).<br/>
