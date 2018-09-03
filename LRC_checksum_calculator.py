# data = '17,03,00,107,00,03'
# 1. split data
# 2. convert splitted data to int
# 3. convert array data integer to hex
# 4. sum all of array data integer
# 5. make negation of summing of array data integer
# 6. calculate two's complement of sum data and convert it to hex to get LRC data

def LRC_calc(data):
	data=data.split(",")
	n=len(data)
	# convert to integer
	for i in range(n):
		data[i]=int(data[i])
	
	# Convert to hex
	data_hex=[0]*n
	for i in range(n):
		data_hex[i]=hex(data[i])[2:]
		k=len(data_hex[i])
		if k == 1:
			data_hex[i]='0'+data_hex[i]
		data_hex[i]=data_hex[i].upper()

	# Get sum of all integer data value
	data_sum=sum(data)
	# Make negative data_sum
	data_sum=data_sum*(-1)

	# Calculate two's complement to get LRC
	val=data_sum
	# nbits=data_sum.bit_length()
	nbits=8
	LRC=hex((val + (1 << nbits)) % (1 << nbits))[2:]
	if len(LRC) == 1:
		LRC='0'+LRC
	LRC=LRC.upper()

	modbus_ascii_data=''
	for i in range(n):
		modbus_ascii_data=modbus_ascii_data+data_hex[i]
	modbus_ascii_data=':'+modbus_ascii_data+LRC+'\r\n'
	# print(modbus_ascii_data)
	return modbus_ascii_data

# LRC_calc('1,3,0,107,0,3')
