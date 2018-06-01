import sys
sys.path.append("singerSpider.py")
sys.path.append("dataprocess.py")

import singerSpider as ss
import dataprocess as dp

url='http://music.163.com/playlist?id=373126389'
	#file=file('results.txt','a')
headers = {
     	'Referer':'http://music.163.com/',
        'Host':'music.163.com',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }

ss.execList(url,file,headers)
dp.count()