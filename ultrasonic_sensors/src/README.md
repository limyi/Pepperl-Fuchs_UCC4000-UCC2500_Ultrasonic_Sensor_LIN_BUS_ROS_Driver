Telegram Structure
_____________________________________________________

1. SYNC_BYTE (8-bits)

Bit 7->4	|		Bit 3		|			Bit 2->0		
  0xA	  	|	  1/0 (R/W)		|	0xSensor_Address (e.g 0x1, 0x2)

Convert Bit 7->4 and Bit 2->0 to binary

0xA -> 1010 in binary

Sensor address (HEX | BINARY) E.g.
	1 :  001
	2 :  010
	... :  ...

SYNC BYTE (BINARY):
(0xA)  (R)	(0x1)
1010 	1 	 001 (Reading from address 0x1 = 10101001)

_____________________________________________________

2. PROFILES 
Profile A: 0xFE
Profile B: 0xFD
Profile C: 0xFC
Temperature: 0xFF

_____________________________________________________

3. DATA BYTE
Distance Measurement:
	Data byte = number of measuring cycles
	1 cycle = 0xFE
	2 cycles = 0xD
	...
	254 cycles = 0x00

Temperature Measurement:
	0xFF = temperature compensation on
	0x00 = temperature compensation off
	0xFE = PWM output on
	0x01 = PWM output off

____________________________________________________

4. CHECK BYTE
Use Excel Sheet to calculate, entering first 3 bytes

####################################################

Commands
____________________________________________________

Write Sensor Address:

SYNC BYTE | OP CODE | DATA BYTE | CHECK BYTE
  0xA..	  |  0x35	| 	0x..	|    0x..

*DATA BYTE = New Sensor Address

Rsponse:

DATA BYTE 	| CHECK BYTE
New address |    0x..

_____________________________________________________

Read Sensor Address (For Unknown Address):

SYNC BYTE |	OP CODE	| DATA BYTE | CHECK BYTE
   0xA8   |  0x00	| 	0x00	| 	0x43

Response:

DATA BYTE 	| CHECK BYTE
Address 	|    0x..

_____________________________________________________

Read Sensor Address (Test Sensor Response):

SYNC BYTE  |   OP CODE	|   DATA BYTE | CHECK BYTE
   0xA..   |  	0x35	| 	  0xFF	  | 	0X..

Response:

DATA BYTE 	| CHECK BYTE
	0x.. 	|    0x..

_____________________________________________________

PWM MODE OFF:

SYNC BYTE67:


1010 |	0	|	(sensor address)

SYNC BYTE  |   OP CODE	|   DATA BYTE | CHECK BYTE
   0xA..   |  	0x0A	| 	  0x01	  | 	0X..

Response:

DATA BYTE 	| CHECK BYTE
	0x.. 	|    0x..

#####################################################

ERROR CODES
___________

0xFF: OK/No Error
0x1: Checksum Error
0x2: Telegram Timeout
0x3: Telegram Below Threshold
0x4: Telegram Above Threshold
0x5: Parameter Error
0x6: Session Error
0x7: Transmission Error
0x8; EEPROM Error
0x9: OP CODE Error
0xA: Object is read-only
0xB: Temperature Error