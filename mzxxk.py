#!/usr/bin/env python
#coding=utf-8

import requests, sys, urllib, os, json, os.path
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')


s = requests.session()

headers = {
                'User-Agent' : 'User-Agent,Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5' ,
                'Connection' : 'keep-alive',
                'Accept'         : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding' : 'gzip, deflate, sdch',
                'Accept-Language' : 'zh-CN,zh;q=0.8',
        }

login_url = 'http://www.zxxk.com/services/jsonservice.asmx/Authorize'
params = {
	'username': 'xkwyx01',
	'password': '55669r',
	'_eventId': 'submit',
	'rememberMe': 'true'
}
postData = {'hashed' : 'false',  
            'isLogin' : 'true',  
            'loadSchoolUser' : 'false', 
            'password' : '55669r',  
            'remember' : 'false',   
            'saveCookie' : 'false',
            'type' : '27' ,
            'username' : 'xkwyx01'  
            }  
resp = s.post(login_url, data=postData, headers=headers, verify=False)

# resp_user = s.get('http://m.zxxk.com/User')
# print resp_user.text

def downFile(fileID):
	'''
	输入ID下载文件
	'''
	downUrl = 'http://download.zxxk.com/?UrlID=29'
	params = {
		'InfoID' : fileID
	}

	respfile = s.get(downUrl,params=params,stream=True)
	realurl = respfile.url.encode('utf-8')
	name = urllib.unquote(realurl.split('&')[1].split('=')[1])
	# print name
	# name = name.decode('utf-8')
	# print 'codename:',name
	if '.doc?' in realurl:
		filename = name + '.doc'
	elif '.pptx?' in realurl:
		filename = name + '.pptx'
	elif '.ppt?' in realurl:
		filename = name + '.ppt'
	elif '.mp4?' in realurl:
		filename = name + '.mp4'
	elif '.pdf?' in realurl:
		filename = name + '.pdf'
	else:
		filename = name + '.rar'
	filename = filename.decode('utf-8')

	if os.path.exists('Downloads'):
		os.chdir('Downloads')
	else:
		os.mkdir('Downloads')
		os.chdir('Downloads')

	# os.chdir('Downloads')
	with open(filename,'wb') as testf:
		for chunk in respfile.iter_content(chunk_size=1024):
			testf.write(chunk)



downFile('6081234')