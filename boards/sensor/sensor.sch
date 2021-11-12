EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Conn_01x04_Female i2c1
U 1 1 61900CAB
P 7300 3050
F 0 "i2c1" H 7328 3026 50  0000 L CNN
F 1 "Conn_01x03_Female" H 7328 2935 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 7300 3050 50  0001 C CNN
F 3 "~" H 7300 3050 50  0001 C CNN
	1    7300 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	6150 4150 6600 4150
Wire Wire Line
	6150 4250 6700 4250
Text Label 6450 3350 0    50   ~ 0
SDA
$Comp
L power:GND #PWR02
U 1 1 618EA9CA
P 6350 5100
F 0 "#PWR02" H 6350 4850 50  0001 C CNN
F 1 "GND" H 6355 4927 50  0000 C CNN
F 2 "" H 6350 5100 50  0001 C CNN
F 3 "" H 6350 5100 50  0001 C CNN
	1    6350 5100
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR01
U 1 1 618EAFE2
P 5550 2300
F 0 "#PWR01" H 5550 2150 50  0001 C CNN
F 1 "+5V" H 5565 2473 50  0000 C CNN
F 2 "" H 5550 2300 50  0001 C CNN
F 3 "" H 5550 2300 50  0001 C CNN
	1    5550 2300
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR03
U 1 1 618ED672
P 6950 2650
F 0 "#PWR03" H 6950 2400 50  0001 C CNN
F 1 "GND" H 6955 2477 50  0000 C CNN
F 2 "" H 6950 2650 50  0001 C CNN
F 3 "" H 6950 2650 50  0001 C CNN
	1    6950 2650
	-1   0    0    1   
$EndComp
NoConn ~ 5150 3150
NoConn ~ 5150 3250
NoConn ~ 5150 3450
NoConn ~ 5150 3550
NoConn ~ 5150 3650
NoConn ~ 5150 3750
NoConn ~ 5150 3850
NoConn ~ 5150 3950
NoConn ~ 6150 3550
NoConn ~ 6150 3250
NoConn ~ 6150 3150
NoConn ~ 6150 4350
NoConn ~ 6150 4450
Wire Wire Line
	6350 4750 6350 5100
Wire Wire Line
	5650 4750 5750 4750
Wire Wire Line
	5850 2500 5550 2500
Wire Wire Line
	5550 2500 5550 2300
NoConn ~ 5750 2750
Wire Wire Line
	5750 4750 6350 4750
Connection ~ 5750 4750
Wire Wire Line
	5850 2750 5850 2500
$Comp
L sensor-rescue:Arduino_Nano_v3.x-MCU_Module A1
U 1 1 618F2A9F
P 5650 3750
F 0 "A1" H 5650 2661 50  0000 C CNN
F 1 "Arduino_Nano_v3.x" H 5650 2570 50  0000 C CNN
F 2 "Module:Arduino_Nano" H 5650 3750 50  0001 C CIN
F 3 "http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf" H 5650 3750 50  0001 C CNN
	1    5650 3750
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x02_Male Power1
U 1 1 618EF24B
P 4600 2200
F 0 "Power1" V 4662 2244 50  0000 L CNN
F 1 "Conn_01x02_Male" V 4753 2244 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 4600 2200 50  0001 C CNN
F 3 "~" H 4600 2200 50  0001 C CNN
	1    4600 2200
	0    1    1    0   
$EndComp
Wire Wire Line
	4600 2400 4600 2500
Wire Wire Line
	4600 2500 5550 2500
Connection ~ 5550 2500
$Comp
L power:GND #PWR0101
U 1 1 618F04F6
P 4500 2800
F 0 "#PWR0101" H 4500 2550 50  0001 C CNN
F 1 "GND" H 4505 2627 50  0000 C CNN
F 2 "" H 4500 2800 50  0001 C CNN
F 3 "" H 4500 2800 50  0001 C CNN
	1    4500 2800
	1    0    0    -1  
$EndComp
Wire Wire Line
	4500 2400 4500 2800
$Comp
L Connector:Conn_01x04_Female J1
U 1 1 618F23A8
P 2900 3750
F 0 "J1" H 2792 3325 50  0000 C CNN
F 1 "Conn_01x04_Female" H 2792 3416 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 2900 3750 50  0001 C CNN
F 3 "~" H 2900 3750 50  0001 C CNN
	1    2900 3750
	-1   0    0    1   
$EndComp
$Comp
L Connector:Conn_01x04_Female J2
U 1 1 618F49D0
P 3400 4300
F 0 "J2" V 3246 4448 50  0000 L CNN
F 1 "Conn_01x04_Female" V 3337 4448 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 3400 4300 50  0001 C CNN
F 3 "~" H 3400 4300 50  0001 C CNN
	1    3400 4300
	0    1    1    0   
$EndComp
$Comp
L Connector:Conn_01x04_Female J3
U 1 1 618F58D1
P 3950 4700
F 0 "J3" V 3796 4848 50  0000 L CNN
F 1 "Conn_01x04_Female" V 3887 4848 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 3950 4700 50  0001 C CNN
F 3 "~" H 3950 4700 50  0001 C CNN
	1    3950 4700
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 618FBB7B
P 3750 3250
F 0 "#PWR0102" H 3750 3000 50  0001 C CNN
F 1 "GND" H 3755 3077 50  0000 C CNN
F 2 "" H 3750 3250 50  0001 C CNN
F 3 "" H 3750 3250 50  0001 C CNN
	1    3750 3250
	-1   0    0    1   
$EndComp
$Comp
L power:+5V #PWR0103
U 1 1 618FC678
P 4100 3250
F 0 "#PWR0103" H 4100 3100 50  0001 C CNN
F 1 "+5V" H 4115 3423 50  0000 C CNN
F 2 "" H 4100 3250 50  0001 C CNN
F 3 "" H 4100 3250 50  0001 C CNN
	1    4100 3250
	1    0    0    -1  
$EndComp
Wire Wire Line
	3100 3550 3200 3550
Wire Wire Line
	3750 3550 3750 3250
Wire Wire Line
	3100 3650 3300 3650
Wire Wire Line
	4100 3650 4100 3250
Wire Wire Line
	3200 4100 3200 3550
Connection ~ 3200 3550
Wire Wire Line
	3200 3550 3750 3550
Wire Wire Line
	3300 4100 3300 3650
Connection ~ 3300 3650
Wire Wire Line
	3300 3650 3850 3650
Wire Wire Line
	3750 4500 3750 3550
Connection ~ 3750 3550
Wire Wire Line
	3850 4500 3850 3650
Connection ~ 3850 3650
Wire Wire Line
	3850 3650 4100 3650
Wire Wire Line
	4050 4500 4050 4450
Wire Wire Line
	4050 4450 5150 4450
Wire Wire Line
	3500 4100 4950 4100
Wire Wire Line
	4950 4100 4950 4350
Wire Wire Line
	4950 4350 5150 4350
Wire Wire Line
	3100 3850 5050 3850
Wire Wire Line
	5050 3850 5050 4250
Wire Wire Line
	5050 4250 5150 4250
Wire Wire Line
	3950 4500 3950 5650
Wire Wire Line
	3950 5650 6450 5650
Wire Wire Line
	6450 5650 6450 3950
Wire Wire Line
	6450 3950 6150 3950
Wire Wire Line
	3400 4100 3400 5750
Wire Wire Line
	3400 5750 6500 5750
Wire Wire Line
	6500 5750 6500 3850
Wire Wire Line
	6500 3850 6150 3850
Wire Wire Line
	6550 5800 6550 3750
Wire Wire Line
	6550 3750 6150 3750
Wire Wire Line
	3100 3750 3150 3750
Wire Wire Line
	3150 3750 3150 5800
Wire Wire Line
	3150 5800 6550 5800
$Comp
L Connector:Conn_01x04_Female i2c2
U 1 1 6191BF1F
P 7300 3500
F 0 "i2c2" H 7328 3476 50  0000 L CNN
F 1 "Conn_01x03_Female" H 7328 3385 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 7300 3500 50  0001 C CNN
F 3 "~" H 7300 3500 50  0001 C CNN
	1    7300 3500
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x04_Female J4
U 1 1 6191E7F5
P 7300 4300
F 0 "J4" H 7328 4276 50  0000 L CNN
F 1 "Conn_01x04_Female" H 7328 4185 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 7300 4300 50  0001 C CNN
F 3 "~" H 7300 4300 50  0001 C CNN
	1    7300 4300
	1    0    0    -1  
$EndComp
Wire Wire Line
	2500 4300 2500 4250
Wire Wire Line
	6150 4050 6850 4050
Wire Wire Line
	6850 4050 6850 4300
Wire Wire Line
	6850 4300 7100 4300
Wire Wire Line
	7100 4200 6650 4200
Wire Wire Line
	6650 4200 6650 5500
Wire Wire Line
	6650 5500 5100 5500
Wire Wire Line
	5100 5500 5100 4150
Wire Wire Line
	5100 4150 5150 4150
$Comp
L power:+5V #PWR0104
U 1 1 6192A886
P 6900 4950
F 0 "#PWR0104" H 6900 4800 50  0001 C CNN
F 1 "+5V" H 6915 5123 50  0000 C CNN
F 2 "" H 6900 4950 50  0001 C CNN
F 3 "" H 6900 4950 50  0001 C CNN
	1    6900 4950
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0105
U 1 1 6192B1AD
P 7050 4950
F 0 "#PWR0105" H 7050 4700 50  0001 C CNN
F 1 "GND" H 7055 4777 50  0000 C CNN
F 2 "" H 7050 4950 50  0001 C CNN
F 3 "" H 7050 4950 50  0001 C CNN
	1    7050 4950
	1    0    0    -1  
$EndComp
Wire Wire Line
	6900 4400 6900 4950
Wire Wire Line
	7050 4950 7050 4500
Wire Wire Line
	7050 4500 7100 4500
Wire Wire Line
	6700 4250 6700 3700
Wire Wire Line
	6700 3700 7100 3700
Wire Wire Line
	6700 3700 6700 3250
Wire Wire Line
	6700 3250 7100 3250
Connection ~ 6700 3700
Wire Wire Line
	7100 3600 6600 3600
Connection ~ 6600 3600
Wire Wire Line
	6600 3600 6600 4150
Wire Wire Line
	6600 3150 7100 3150
Wire Wire Line
	6600 3150 6600 3600
Wire Wire Line
	6950 2650 6950 3050
Connection ~ 6950 3050
Wire Wire Line
	6950 3050 7100 3050
Wire Wire Line
	6900 4400 7100 4400
Wire Wire Line
	6950 3500 7100 3500
Wire Wire Line
	6950 3050 6950 3500
Wire Wire Line
	7100 3400 7050 3400
Wire Wire Line
	7050 3400 7050 2950
Wire Wire Line
	7050 2950 7100 2950
Wire Wire Line
	7050 2950 6350 2950
Wire Wire Line
	6350 2950 6350 2500
Wire Wire Line
	6350 2500 5850 2500
Connection ~ 7050 2950
Connection ~ 5850 2500
$EndSCHEMATC
