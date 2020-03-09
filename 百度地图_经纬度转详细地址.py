# -*- coding: utf-8 -*
import requests
import json

url = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak=&output=json&coordtype=wgs84ll&location=39.09508666666667,117.08661666666667'
response = requests.get(url)
response.encoding = 'utf8'
html = response.text
html = json.loads(html)

location = html["result"]["formatted_address"]
print(location)
