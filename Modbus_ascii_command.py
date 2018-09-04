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

# Turn on Yx command
Y0_ON='1,5,0,0,255,0'
Y1_ON='1,5,0,1,255,0'
Y2_ON='1,5,0,2,255,0'
Y3_ON='1,5,0,3,255,0'
Y4_ON='1,5,0,4,255,0'
Y5_ON='1,5,0,5,255,0'
Y6_ON='1,5,0,6,255,0'
Y7_ON='1,5,0,7,255,0'
# Turn off Yx command
Y0_OFF='1,5,0,0,0,0'
Y1_OFF='1,5,0,1,0,0'
Y2_OFF='1,5,0,2,0,0'
Y3_OFF='1,5,0,3,0,0'
Y4_OFF='1,5,0,4,0,0'
Y5_OFF='1,5,0,5,0,0'
Y6_OFF='1,5,0,6,0,0'
Y7_OFF='1,5,0,7,0,0'
# Read Yx command
READ_Y0='1,1,0,0,0,1'
READ_Y1='1,1,0,1,0,1'
READ_Y2='1,1,0,2,0,1'
READ_Y3='1,1,0,3,0,1'
READ_Y4='1,1,0,4,0,1'
READ_Y5='1,1,0,5,0,1'
READ_Y6='1,1,0,6,0,1'
READ_Y7='1,1,0,7,0,1'
# Read all Coils
READ_Y0_Y7='1,1,0,0,0,8'
# Read Holding Register
READ_R0='1,3,0,0,0,1'
READ_R1='1,3,0,1,0,1'
READ_R2='1,3,0,2,0,1'
READ_R3='1,3,0,3,0,1'
READ_R4='1,3,0,4,0,1'
READ_R5='1,3,0,5,0,1'