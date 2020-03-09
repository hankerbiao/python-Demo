#-*-coding:utf8-*-
#以相同的字符开头
#1、starts-with(@属性名称，属性字符相同的部分)
from lxml import etree

html1 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test-1">需要的内容1</div>
    <div id="test-2">需要的内容2</div>
    <div id="testfault">需要的内容3</div>
</body>
</html>
'''

html2 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test3">
        我左青龙，
        <span id="tiger">
            右白虎，
            <ul>上朱雀，
                <li>下玄武。</li>
            </ul>
            老牛在当中，
        </span>
        龙头在胸口。
    </div>
</body>
</html>
'''

# selector = etree.HTML(html1)
# content = selector.xpath('//div[starts-with(@id,"test")]/text()')#在id这个属性里面以test所有的div标签都提取出来
# for each in content:
#     print (each)
#

#2、标签套标签
selector = etree.HTML(html2)
data = selector.xpath('//div[@id="test3"]')[0]
info = data.xpath('string(.)')
content_2 = info.replace('\n','').replace(' ','')
print (content_2)

