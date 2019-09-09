#!/usr/bin/python
from datetime import datetime
import asyncore,re
import netifaces as ni
from smtpd import SMTPServer

class EmlServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data):
        for line in data.splitlines():
            if re.search('Ref:',line):
                print(line.split('Ref:',1)[1])
        self.no += 1

def run(ip):
    foo = EmlServer(('{}'.format(ip), 25), None)
    print('[*] SMTP Server started')
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    ni.ifaddresses('tun0')
    ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
    run(ip)
