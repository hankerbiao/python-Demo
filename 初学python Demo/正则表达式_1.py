# -*-coding:utf8-*-
import re
import requests

f = open('text.txt','r')
html = f.read()
f.close()

pic_url = re.findall('sec="(.*?)",html,re.S')
i = 0
for each in pic_url:
    print 'now downing:'+each
    pic = requests.get(each)
    fp = open('pic\\' + str(i) + '.jpg','wb')
    fp.close()
    i += 1


