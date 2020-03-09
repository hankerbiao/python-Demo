
    # -*- coding: cp936 -*-
# c ="""fisixxrenxxdlkfsaxxqingxxwdlkjjixx
# xiaoxxlwdhlkjxxzhuoxxdwlkn9kjxxmaxxddwdok"""
# b = re.findall('xx(.*?)xx',c,re.S)
# print b
#
#
# #没有re.S输出的是：['ren', 'qing', 'lwdhlkj', 'dwlkn9kj']
# #有re.S输出的是：  ['ren', 'qing', '\nxiao', 'zhuo', 'ma']
#
# #对比 sub的使用：替换的功能
#
# s = "123abc123"
# b = re.sub('123(.*?)123','123%d123'%789,s) #把 789替换到（.*？）中
# print b
#
#
#
# #匹配纯数字（\d+）
# a = "15156dddjj656"
# b = re.findall('(\d+)',a)
# print b

import re

old_url = 'http://ww.jikexueyuan.com/course/android/?pageNum=2'
total_page = 20

f = open('text.txt','r')
html = f.read()
f.close()

# #爬去标题
# title = re.search('<title>(.*?)</title>',html,re.S).group(1)
# print title

# #爬去链接
# links = re.findall('href="(.*?)">',html,re.S)
# for each in links:
#     print each

#sub实现翻页
for i in range(2,total_page +1):
    new_link = re.sub('pageNum=\d+','pageNum=%d'%i,old_url,re.S)
    print new_link


