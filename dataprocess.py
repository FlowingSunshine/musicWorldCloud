# -*- coding: utf-8 -*
import requests
import re
#import json
def count():
    singers={}
    f1=open('count.txt')
    f2=file('result.txt','w')
    line=f1.readline()
    while line:
    	if str(line) not in singers.keys():
    		singers[str(line)]=1
    	else:
    		singers[str(line)]+=1
		line=f1.readline()
#	jssinges=json.dumps(singers)
#	f2.write(jssingers)
	for singer in singers:
		f2.write(singer+'\t')
		f2.write(str(singers[singer]))
	#f1.close()
    f2.close()

#def sort(counts):
#	items=counts.items()
#	backitems=[[v[1],v[0]]for v in items]
#	backitems.sort()
#	return [backitems[i][1] for i in range(0,len(backitems))]

if __name__ == '__main__':
	count()
