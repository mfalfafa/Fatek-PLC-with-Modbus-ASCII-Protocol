### FATEK PLC with Modbus ASCII Protocol using Python3 ###
#### MF Alfafa ####
#### miftahf77@gmail.com ####
#### 3 September 2018 ####

> Introduction

This Python 3 script is used to read or write data onto FATEK PLC using Modbus ASCII Protocol. 

> Requirements

	* hardware
		1. FATEK PLC FBs-20MCT2-AC
		2. CB55-7 RS485 Module
		3. RS485 to USB converter
		4. Computer
	* Software
		1. Python 3 Application
		2. WinProLadder

> Settings

	1. Insert CB55 RS485 module to FATEK PLC
	2. In this case we use Port 2 of CB55 Module
	3. Open WinProLadder software and set Port 2 to use Modbus ASCII Slave as its protocol
	4. Connect FATEK PLC to computer using RS485 to USB converter

> Refferences

	1. http://www.modbustools.com/modbus.html#function05
	2. http://www.simplymodbus.ca/ASCII.htm
	3. http://www.simplymodbus.ca/FAQ.htm#Modbus