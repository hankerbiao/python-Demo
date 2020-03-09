#-*-coding:utf8-*-

#xpath 提取内容
#//定位跟节点
#/往下层寻找
#提取文本内容 /text（）
#提取属性内容：/@xxxx


from lxml import etree
html = """
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>测试-常规用法</title>
</head>
<body>
<div id="content">
    <ul id="useful">
        <li>这是第一条信息</li>
        <li>这是第二条信息</li>
        <li>这是第三条信息</li>
    </ul>
    <ul id="useless">
        <li>不需要的信息1</li>
        <li>不需要的信息2</li>
        <li>不需要的信息3</li>
    </ul>

    <div id="url">
        <a href="http://jikexueyuan.com">极客学院</a>
        <a href="http://jikexueyuan.com/course/" title="极客学院课程库">点我打开课程库</a>
    </div>
</div>

</body>
</html>"""
selector = etree.HTML(html) #使用etree.HTML将多行字符串转化为xpath可识别的一个对象  传递给 selector

#提取文本
# content = selector.xpath('//div[@id="content"]/ul[@id="useful"]/li/text()') #[@id = "useful"] 限定的id = useful 这个url，而不是所有的rul
# for each in content:
#     print (each)

#提取属性
# link = selector.xpath('//div[@id="url"]/a/@href')
# for each in link:
#     print (each)

#提取标题
# title = selector.xpath('//a/@title')
# for each in title :
#     print (each)
