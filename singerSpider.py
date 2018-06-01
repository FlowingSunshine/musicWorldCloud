# -*- coding: utf-8 -*
import requests
import re
import urllib2
from bs4 import BeautifulSoup



def execList(url,file,headers):#爬取页面并处理
	f1=file('songs.txt','w')
	f2=file('artists.txt','w')
	f3=file('count.txt','w')
	count=0
	s=requests.session()

	s=BeautifulSoup(s.get(url,headers=headers).content)
	print s
	lst = s.find('ul',{'class':'f-hide'})
	#print lst.find_all('a')
	for song in lst.find_all('a'):
		f1.write(str(song))
	f1.close()
		

	for song in lst.find_all('a'):
		x=song.get('href')
		url='http://music.163.com'+str(x)
		#print url
		singer=execSong(url,headers)
		f2.write(singer+'\n')
		if str(singer)!='None':
			singername=str(singer).split('>')[1].split('<')[0]
			singername=singername.replace(' ','')
			f3.write(singername+'\n')
		count=count+1
		#print singer
	f2.close()
	f3.close()
	print count
	"""
	except:
		print "error"
		pass
	"""

def execSong(url,headers):
	s=requests.session()
	try:	
		s=BeautifulSoup(s.get(url,headers=headers).content)
		singer=s.find('p',{'class':'des s-fc4'}).find('a',{'class':'s-fc7'})
		print str(singer)
		return str(singer)

	except:
		pass
'''
if __name__ == '__main__':
	url='http://music.163.com/user/home?id=272269212'
	#file=file('results.txt','a')
	headers = {
        'Referer':'http://music.163.com/',
        'Host':'music.163.com',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }

	execList(url,file,headers)
	#file.close()
'''
