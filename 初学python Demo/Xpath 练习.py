from lxml import etree
import requests

url = 'http://www.minimp4.com/movie/?'
html = requests.get(url)

selector = etree.HTML(html.text)
result = selector.xpath('//div[@class = "meta"]/h1/a/@href=text()')
print(result)