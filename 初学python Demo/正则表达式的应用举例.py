
    # -*- coding: cp936 -*-
# c ="""fisixxrenxxdlkfsaxxqingxxwdlkjjixx
# xiaoxxlwdhlkjxxzhuoxxdwlkn9kjxxmaxxddwdok"""
# b = re.findall('xx(.*?)xx',c,re.S)
# print b
#
#
# #û��re.S������ǣ�['ren', 'qing', 'lwdhlkj', 'dwlkn9kj']
# #��re.S������ǣ�  ['ren', 'qing', '\nxiao', 'zhuo', 'ma']
#
# #�Ա� sub��ʹ�ã��滻�Ĺ���
#
# s = "123abc123"
# b = re.sub('123(.*?)123','123%d123'%789,s) #�� 789�滻����.*������
# print b
#
#
#
# #ƥ�䴿���֣�\d+��
# a = "15156dddjj656"
# b = re.findall('(\d+)',a)
# print b

import re

old_url = 'http://ww.jikexueyuan.com/course/android/?pageNum=2'
total_page = 20

f = open('text.txt','r')
html = f.read()
f.close()

# #��ȥ����
# title = re.search('<title>(.*?)</title>',html,re.S).group(1)
# print title

# #��ȥ����
# links = re.findall('href="(.*?)">',html,re.S)
# for each in links:
#     print each

#subʵ�ַ�ҳ
for i in range(2,total_page +1):
    new_link = re.sub('pageNum=\d+','pageNum=%d'%i,old_url,re.S)
    print new_link


