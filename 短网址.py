# -*- coding: utf-8 -*-
import requests
"""学习request请求"""
entry_url = 'www.baidu.com'
url = 'http://api.kks.me/api.php?format=json&url={0}&apikey=@ddd'.format(entry_url)
html = requests.get(url).text
print(html[8:-13])
