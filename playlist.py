# -*- coding: utf-8 -*
import requests
import re
from bs4 import BeautifulSoup

def execList(url,file,headers):#爬取页面并处理
	f1=file('songs.txt','w')
	f2=file('artists.txt','w')
	f3=file('count.txt','w')
	count=0
	s=requests.session()
	try:
		s=BeautifulSoup(s.get(url,headers=headers).content)
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
	except:
		pass


def execSong(url,headers):
	s=requests.session()
	try:	
		s=BeautifulSoup(s.get(url,headers=headers).content)
		singer=s.find('p',{'class':'des s-fc4'}).find('a',{'class':'s-fc7'})
		#if(str(s)!="None"):
		#	singer=str(singer).split('>')[1].split('<')[0]
		print str(singer)
		return str(singer)
		'''pattern_start=re.compile('"name":"')
		pattern_end	=re.compile('","tns"')
		content_get=pattern_start.split(artists)
		content_get=pattern_end.split(content_get[-1])
		content=re.split('',constent_get[0])
		'''
	except:
		pass

if __name__ == '__main__':
	url="http://music.163.com/#/playlist?id=40177729"
	#file=file('results.txt','a')
	headers = {
        'Referer':'http://music.163.com/',
        'Host':'music.163.com',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }

	execList(url,file,headers)
	#file.close()
    
