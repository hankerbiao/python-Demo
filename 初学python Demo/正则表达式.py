# -*- coding: cp936 -*-
import re
c ="""fisixxrenxxdlkfsaxxqingxxwdlkjjixx
xiaoxxlwdhlkjxxzhuoxxdwlkn9kjxxmaxxddwdok"""
b = re.findall('xx(.*?)xx',c,re.S)
print b


#û��re.S������ǣ�['ren', 'qing', 'lwdhlkj', 'dwlkn9kj']
#��re.S������ǣ�  ['ren', 'qing', '\nxiao', 'zhuo', 'ma']

#�Ա� sub��ʹ�ã��滻�Ĺ���

s = "123abc123"
b = re.sub('123(.*?)123','123%d123'%789,s) #�� 789�滻����.*������
print b



#ƥ�䴿���֣�\d+��
a = "15156dddjj656"
b = re.findall('(\d+)',a)
print b
