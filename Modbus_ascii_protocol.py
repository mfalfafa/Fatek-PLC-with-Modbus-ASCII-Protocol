import serial
import serial.tools.list_ports
import time
from LRC_checksum_calculator import *

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
# Commands
# Turn on single coil :
# '1,5,0,0,255,0' -> coil Y0
# '1,5,0,1,255,0' -> coil Y1
# '1,5,0,2,255,0' -> coil Y2
# '1,5,0,3,255,0' -> coil Y3
# '1,5,0,4,255,0' -> coil Y4
# '1,5,0,5,255,0' -> coil Y5
# '1,5,0,6,255,0' -> coil Y6
# '1,5,0,7,255,0' -> coil Y7
# Turn off single coil
# '1,5,0,0,0,0' -> coil Y0
# '1,5,0,1,0,0' -> coil Y1
# '1,5,0,2,0,0' -> coil Y2
# '1,5,0,3,0,0' -> coil Y3
# '1,5,0,4,0,0' -> coil Y4
# '1,5,0,5,0,0' -> coil Y5
# '1,5,0,6,0,0' -> coil Y6
# '1,5,0,7,0,0' -> coil Y7
# Read Single coil
# '1,1,0,0,0,1' -> coil Y0
# '1,1,0,1,0,1' -> coil Y1
# '1,1,0,2,0,1' -> coil Y2
# '1,1,0,3,0,1' -> coil Y3
# '1,1,0,4,0,1' -> coil Y4
# '1,1,0,5,0,1' -> coil Y5
# '1,1,0,6,0,1' -> coil Y6
# '1,1,0,7,0,1' -> coil Y7
# Read Holding Register (Single)
# '1,3,0,0,0,1' -> Register R0
# '1,3,0,1,0,1' -> Register R1
# '1,3,0,2,0,1' -> Register R2
# '1,3,0,3,0,1' -> Register R3
# '1,3,0,4,0,1' -> Register R4

cmd=['1,1,0,7,0,1','1,5,0,7,0,0','1,3,0,1,0,1','1,6,0,1,0,3','1,15,0,0,0,2,2,0,3']
for i in range(len(cmd)):
   cmd[i]=LRC_calc(cmd[i])
    
while 1:
    ser_rfid.write(cmd[2].encode('utf-8'))
    #print(cmd[1])
    if ser_rfid.inWaiting():
        recData=ser_rfid.readall()
        recData=recData.decode('ascii')
        # print (recData)
        try:            
            start = recData.index( ':' ) + len( ':' )
            end = recData.index( '\n', start )
            recData = recData[start:end]
            print (recData)
        except Exception as e:
            print (e)
            pass
    time.sleep(0.5)
