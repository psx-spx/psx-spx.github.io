# Controllers - Taiko Controllers (Tatacon)
Drum controllers made by Namco and used by the Taiko no Tatsujin series on the
PS2 (but compatible with the PS1, even though no PS1 Taiko game was ever made).
These controllers behave like standard digital pads (ID 41h) and contain four
hit sensors mapped to the following buttons:<br/>

| Sensor             | Button     | Bit |
| :----------------- | :--------- | --: |
| Left ka (rim)      | L1         |  10 |
| Right ka (rim)     | R1         |  11 |
| Left don (center)  | D-pad left |   7 |
| Right don (center) | Circle     |  13 |

Dedicated start and select buttons are also present. Unlike Pop'n Controllers,
no additional buttons are hardcoded to be always pressed.<br/>
