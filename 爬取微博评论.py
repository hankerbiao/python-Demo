# -*- coding: utf-8 -*-
import requests
from lxml import etree
import time
"""爬取微博话题#疫情过后，你最想吃什么东西#前50页评论"""
nums = 50#爬取多少页
for num in range(1, nums+1):
    url = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id=4470061467455282&page={0}'.format(num)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Referer': 'https://weibo.com/5991853169/ItoCmvhsu?type=comment',
        'Cookie': 'UOR=www.nhc.gov.cn,widget.weibo.com,www.nhc.gov.cn; SINAGLOBAL=5174071058218.561.1580359176821; ULV=1580359176832:1:1:1:5174071058218.561.1580359176821:; YF-V5-G0=9717632f62066ddd544bf04f733ad50a; _s_tentry=www.nhc.gov.cn; Apache=5174071058218.561.1580359176821; Ugrow-G0=cf25a00b541269674d0feadd72dce35f; SUB=_2A25zRKMlDeRhGeFN7lIT8ybOzjmIHXVQM5PtrDV8PUNbmtANLViikW9NQABmY0QsRx-INtrKd1io8q4lX1zODbKf; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhcjXBHrzhkagne7ZBkpdB05JpX5KzhUgL.FoM0SK5Ee0nESK-2dJLoIEBLxK.L1-BLBKzLxK-L1K5L1K2LxKqLBK5L1KMLxK-LB-BL1K5t; SUHB=0tKaBuseNtCJh-; ALF=1612842741; SSOLoginState=1581306741; YF-Page-G0=16139189c1dbd74e7d073bc6ebfa4935|1581306774|1581306748; wb_view_log_7350238255=1536*8641.25; webim_unReadCount=%7B%22time%22%3A1581306865141%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D'
    }
    response = requests.get(url, headers=headers)
    data = response.json()['data']['html']
    HTML = etree.HTML(data)
    comment = HTML.xpath('//div[@class="WB_text"]/text()')
    with open("1.txt", "a", encoding='utf8') as file:
        for i in comment:
            comment_data = str(i).replace("：", "").replace(":", "").replace(" ", "").replace("回复", "")
            file.write(comment_data)
    print("第{0}页爬取成功".format(num))
    time.sleep(0.5)
