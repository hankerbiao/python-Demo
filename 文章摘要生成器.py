import urllib.request
import urllib.parse
import tkinter as tk

"""
用过调用阿里云api

"""
root = tk.Tk()
root.title = '文章摘要生成器'  # 标题
root.geometry('800x500+400+200')  # 窗体位置


def WenZhangZhiYao():
    host = 'http://showapizy.market.alicloudapi.com'
    path = '/actialAbstract'
    method = 'POST'
    appcode = ''  # 在阿里云申请
    querys = ''
    bodys = {}
    url = host + path

    # bodys['num'] = str(entry2.get())
    # bodys['text'] = str(entry.get())
    bodys['num'] = '3'
    bodys[
        'text'] = ''''''
    post_data = urllib.parse.urlencode(bodys).encode('utf8')
    request = urllib.request.Request(url, post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    # 根据API的要求，定义相对应的Content-Type
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response
    """
    {'showapi_res_error': '', 'showapi_res_id': '2c0b970c81184478a23cb87db076bc77', 'showapi_res_code': 0, 'showapi_res_body': {'ret_code': 0, 'list': ['国家气象局天气预报接口API', '实时天气情况每30分钟更新1次', '7天天气范围的预报每天更新3次']}}

    """
    import json
    json = json.load(content)
    res = json['showapi_res_body']['list']
    num = 1
    for i in res:
        print("{0}:".format(num) + i)
        num += 1
        Text.insert(i)


label = tk.Label(root, text='根据传入的长篇文章，系统使用智能算法抽取文章摘要。适用于新闻摘要等场景。', font=('微软雅黑', 16), fg='red')
label.grid(row=0, column=0)
label2 = tk.Label(root, text='请输入文章内容:', font=('微软雅黑', 16), fg='red')
label2.place(x=30, y=60)
label3 = tk.Label(root, text='请输入要生成摘要条目数:', font=('微软雅黑', 16), fg='red')
label3.place(x=10, y=100)
Text = tk.Text(root, width=100, height=20)
Text.place(x=30, y=160)
entry = tk.Entry(root, font=('微软雅黑', 16), width=42)
entry.place(x=200, y=60)
entry2 = tk.Entry(root, font=('微软雅黑', 16), width=4)
entry2.place(x=280, y=100)
button1 = tk.Button(text='开始生成', font=('微软雅黑', 16), command=WenZhangZhiYao)
button1.place(x=350, y=100)

root.mainloop()
