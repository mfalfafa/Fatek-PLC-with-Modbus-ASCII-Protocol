# MODBUS ASCII Protocol using Python Script

import serial
import serial.tools.list_ports
import time
from LRC_checksum_calculator import *
from Modbus_ascii_command import *

connected = False
ser_rfid=0
n=200
buff=['']*n
count_=0

## Establish connection to COM Port
## Connection from HMI
comlist = serial.tools.list_ports.comports()
## loop until the device tells us it is ready
while not connected:
    ## COM Port settings
    for device in comlist: 
        try:
            # print ("Trying...",device)
            ## Serial Initialization
            ser_rfid = serial.Serial(device[0],      #port
                                9600,              #baudrate
                                serial.EIGHTBITS,   #bytesize
                                serial.PARITY_NONE,  #parity
                                serial.STOPBITS_ONE, #,#stop bit
                                0,                  #timeout
                                False,              #xonxoff
                                False,              #rtscts
                                0,                  #write_timeout
                                False,              #dsrdtr
                                None,               #inter byte timeout
                                None                #exclusive
                                )
            connected=True
        except:
            connected=False
            print ("trying to connect to ", device[0])
            time.sleep(1.5)
if connected:
    serin = ser_rfid.read()
    print ("Connected to ",device[0])
    connected=False

recData=''
# Format Data :
# ':01 03 00 00 00 02 FA\r\n'
# cmd = [slave_addr, func, start_addr_H, start_addr_L, quantity_H, quantity_L]

# cmd=['1,1,0,7,0,1','1,5,0,7,0,0','1,3,0,1,0,1','1,6,0,1,0,3','1,15,0,0,0,2,2,0,3']
# for i in range(len(cmd)):
#    cmd[i]=LRC_calc(cmd[i])

# Turn on single coil
def Y0_on():
    ser_rfid.write(LRC_calc(Y0_ON).encode('utf-8'))
def Y1_on():
    ser_rfid.write(LRC_calc(Y1_ON).encode('utf-8'))
def Y2_on():
    ser_rfid.write(LRC_calc(Y2_ON).encode('utf-8'))
def Y3_on():
    ser_rfid.write(LRC_calc(Y3_ON).encode('utf-8'))
def Y4_on():
    ser_rfid.write(LRC_calc(Y4_ON).encode('utf-8'))
def Y5_on():
    ser_rfid.write(LRC_calc(Y5_ON).encode('utf-8'))
def Y6_on():
    ser_rfid.write(LRC_calc(Y6_ON).encode('utf-8'))
def Y7_on():
    ser_rfid.write(LRC_calc(Y7_ON).encode('utf-8'))
# Turn off single coil
def Y0_off():
    ser_rfid.write(LRC_calc(Y0_OFF).encode('utf-8'))
def Y1_off():
    ser_rfid.write(LRC_calc(Y1_OFF).encode('utf-8'))
def Y2_off():
    ser_rfid.write(LRC_calc(Y2_OFF).encode('utf-8'))
def Y3_off():
    ser_rfid.write(LRC_calc(Y3_OFF).encode('utf-8'))
def Y4_off():
    ser_rfid.write(LRC_calc(Y4_OFF).encode('utf-8'))
def Y5_off():
    ser_rfid.write(LRC_calc(Y5_OFF).encode('utf-8'))
def Y6_off():
    ser_rfid.write(LRC_calc(Y6_OFF).encode('utf-8'))
def Y7_off():
    ser_rfid.write(LRC_calc(Y7_OFF).encode('utf-8'))

# Parse incoming data from serial port
def parse_data():
    if ser_rfid.inWaiting():
        data=ser_rfid.readall()
        try:
            data=data.decode('ascii')
            start = data.index( ':' ) + len( ':' )
            end = data.index( '\r\n', start )
            data = data[start:end]
            n=len(data)
            data=data[n-4:n-2]
            return (data)
        except Exception as e:
            print (e)
            return (-1)
    else:
        return (-1)

# reads all Coils (Y0 - Y7)
def Y0_Y7_read():
    ser_rfid.write(LRC_calc(READ_Y0_Y7).encode('utf-8'))
    result=parse_data()
    if result != (-1):
        # Convert HEX to bits for Coils (Y)
        buff=[0]*8  # there are 8 coils
        result=int(result,16)
        for i in range(8):
            if result >= 2:
                div=int(result/2)
                mod=result%2
                buff[i]=mod
                result=div
            else:
                if result == 1:
                    buff[i]=result
                    result=0
        print (buff)
        return buff
    else:
        return (-1)

Y4_on()
time.sleep(0.1)
Y5_on()
time.sleep(0.1)

# Main while
while 1:
    lamps=Y0_Y7_read()
    if lamps != (-1):
        if lamps[0] != (-1):
            if lamps[0] == 1:
                print ('Coil Y0 is on')
            else:
                print ('Coil Y0 is off')
    time.sleep(0.1)
