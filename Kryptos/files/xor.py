#!/usr/bin/python
import sys
import base64

# 1 => decrypted msg
# 2 => cipher msg
# 3 => remote msg
# Read two files as byte arrays

file1_b = bytearray(open(sys.argv[1], 'rb').read())
file2_b = bytearray(base64.b64decode(open(sys.argv[2], 'rb').read()))
file3_b = bytearray(base64.b64decode(open(sys.argv[3], 'rb').read()))

size = len(file3_b) if len(file3_b) < len(file2_b) else len(file2_b)
xord_byte_array = bytearray(size)

for i in range(size):
	xord_byte_array[i] = file3_b[i] ^ file2_b[i]

size2 = len(xord_byte_array) if len(xord_byte_array) < len(file1_b) else len(file1_b)
m = bytearray(size2)

for i in range(size2):
	m[i] = file1_b[i] ^ xord_byte_array[i]
 
print(m)
