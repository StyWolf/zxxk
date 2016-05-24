#!/usr/bin/env python
#coding=utf-8

import requests, sys, urllib, os, json
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')


mysession = requests.Session()

def Checkcode():
	'''
	获取验证码cookie
	'''
	headers = {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' ,
                'Connection' : 'keep-alive',
                'Accept'         : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding' : 'gzip, deflate, sdch',
                'Accept-Language' : 'zh-CN,zh;q=0.8'
        }
	resp = mysession.get('http://user.zxxk.com/RanImg.aspx',headers=headers,stream=True)
	with open('yzm.png','wb') as f:
		for chunk in resp.iter_content():
			f.write(chunk)
	return resp.cookies

def Login(code,username,password):
	'''
	登录学科网用户中心，获取帐号信息
	'''
	#login_cookies = Checkcode()
	post_headers = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' ,
        'Connection' : 'keep-alive',
        'Accept'         : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, sdch',
        'Accept-Language' : 'zh-CN,zh;q=0.8',
        'DNT'	: '1',
        'Referer' : 'http://user.zxxk.com/Login.aspx?ComeUrl=http%3a%2f%2fuser.zxxk.com%2fdefault.aspx',
	}
	payload = {
		'UserName' : username,
		'UserPassword' : password,
		'CheckCode' : code,
		'comeUrl' : 'http%3a%2f%2fuser.zxxk.com%2fdefault.aspx'
	}
	post_resp = mysession.post('http://user.zxxk.com/Login.aspx',data=payload, headers=post_headers)
	
	
	return post_resp.cookies
def Getinfo():
	'''
	获取用户基本信息
	'''
	resp_user = mysession.get('http://user.zxxk.com/default.aspx')

	soup = BeautifulSoup(resp_user.text,'lxml')
	soup.prettify()
	userName = soup.find(class_='bl-name').text
	userLevel = soup.find(class_='item_sort').text


	return (userName,userLevel)

def downFile(fileID):
	'''
	输入ID下载文件
	'''
	downUrl = 'http://download.zxxk.com/?UrlID=30'
	params = {
		'InfoID' : fileID
	}

	respfile = mysession.get(downUrl,params=params,stream=True)
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
	else:
		filename = name + '.rar'
	filename = filename.decode('utf-8')

	os.chdir('./Downloads')
	with open(filename,'wb') as testf:
		for chunk in respfile.iter_content(chunk_size=1024):
			testf.write(chunk)


def main():
	Checkcode()
	code = raw_input('请输入验证码:\n')
	
	fp = file('config.json')
	s = json.load(fp)
	for key in s.keys():
		username = key
		passwd = s[key]
	Login(code,username, passwd)
	un,ul = Getinfo()
	return un,ul

if __name__ == '__main__':


		# Checkcode()
		# code = raw_input('请输入验证码:\n')
		
		# fp = file('config.json')
		# s = json.load(fp)
		# for key in s.keys():
		# 	username = key
		# 	passwd = s[key]
		# Login(code,username, passwd)
		# un,ul = Getinfo()
		# print '用户名：{0} \n账户信息:{1}'.format(un,ul)
		while True:
			try:
				un,ul = main()
				print '用户名：{0} \n账户信息:{1}'.format(un,ul)
				break
			except:
				print '你输入的验证码有误，请重新输入：'
		


		while True:
			FileID = raw_input("请输入编码ID:")
			print "请稍候，正在下载中。。。"
			downFile(FileID)
		
	




	