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
	for singer in singers:
		f2.write(singer+'\t')
		f2.write(str(singers[singer]))
    f2.close()


"""
if __name__ == '__main__':
	count()
"""