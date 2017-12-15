# -*- coding: utf-8 -*
from os import path
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
from scipy.misc import imread
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
font_path="STHeiti Medium.ttc"
data=path.dirname('.')
text=open(path.join(data,'count.txt')).read()

def cloudGenerator(data,text):
	wifeImg=imread(path.join(data,"background.jpeg"))
	wc = WordCloud(font_path=font_path,background_color="white",mask=wifeImg,stopwords="",max_font_size=100,random_state=40)
	wc.generate(text)
	image_colors=ImageColorGenerator(wifeImg)
	plt.imshow(wc)
	plt.axis("off")
	plt.figure()
	plt.imshow(wifeImg,cmap=plt.cm.gray)
	plt.axis("off")
	plt.show()
	wc.to_file(path.join(data,"词云.png"))

print text
cloudGenerator(data,text)