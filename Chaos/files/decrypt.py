#!/usr/bin/python
import os,random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def main():
	decrypt(getKey('sahay'),'enim_msg.txt')

def decrypt(key, filename):
	chunksize = 64*1024

	with open(filename, 'rb') as infile:
		IV = infile.read(16)
		#print IV

		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open('decryted.txt','wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(decryptor.decrypt(chunk))

def getKey(password):
	hasher = SHA256.new(password.encode('utf-8'))
	return hasher.digest()

if __name__ == "__main__":
	main()
