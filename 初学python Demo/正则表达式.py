# -*- coding: cp936 -*-
import re
c ="""fisixxrenxxdlkfsaxxqingxxwdlkjjixx
xiaoxxlwdhlkjxxzhuoxxdwlkn9kjxxmaxxddwdok"""
b = re.findall('xx(.*?)xx',c,re.S)
print b


#没有re.S输出的是：['ren', 'qing', 'lwdhlkj', 'dwlkn9kj']
#有re.S输出的是：  ['ren', 'qing', '\nxiao', 'zhuo', 'ma']

#对比 sub的使用：替换的功能

s = "123abc123"
b = re.sub('123(.*?)123','123%d123'%789,s) #把 789替换到（.*？）中
print b



#匹配纯数字（\d+）
a = "15156dddjj656"
b = re.findall('(\d+)',a)
print b
