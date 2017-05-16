 #! -*- coding:utf-8 -*-

'''
__author__="nMask"
__Date__="2017年5月15日"
__Blog__="http://thief.one"
__version__="1.0"
__Python__="2.7.11"
'''

import requests 
# from oprethinkdb import oprethinkdb
import re

url="https://technet.microsoft.com/en-us/library/security/dn632603.aspx"
res='title=\"MS[\d-]+\">(.*)</a>' #re
msurl="https://technet.microsoft.com/en-us/library/security/"

red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
white = '\033[1;37m'
reset = '\033[0m'


def getcontent(url):
	'''
	获取每年的ms漏洞号
	'''
	try:
		body=requests.get(url).content
	except:
		print "%s[INFO]Request url error %s" % (red,reset)
		result_list=[]
	else:
		p=re.compile(res)
		result_list=p.findall(body)
	'''
	result_list=['MS16-003',......]
	'''
	return result_list   

def getkb(url,ms):
	'''
	获取一个ms漏洞每个系统版本对应的kb号。
	'''
	dicts={}
	dicts["MS_ID"]=ms
	try:
		body=requests.get(url).content
	except:
		print "%s[INFO]Request url error %s" % (red,reset)
	else:
		res=r"<a href=\"([^>]*)\">([^<]*)<\/a>[\s\<\>spanclu \=\"\[\]\d\/]+?[^<]+?<br />(\([^\<\(\)]*\))" 
		p=re.compile(res,re.DOTALL)
		result_list=p.findall(body)
		print "%s[INFO]result_lens is %s %s" % (green,len(result_list),reset)
		dicts["Content"]=result_list
		print "[INFO]result is ",dicts
		# try:
		# 	cur_db.Insert(dicts,"MS_ID")
		# 	print "%s[INFO]Insert DB Success %s" % (green,reset)
		# except:
		# 	print "%s[INFO]Insert DB error %s" % (red,reset)



# cur_db=oprethinkdb("","")

result_list=getcontent(url)

for ms in result_list:
	msurl_new=msurl+ms.lower()+".aspx"
	print "%s[INFO]target_url is %s %s" % (white,msurl_new,reset)
	getkb(msurl_new,ms)
	break






