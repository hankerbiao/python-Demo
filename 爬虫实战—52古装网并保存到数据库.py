import requests
from lxml import etree
import threading
import pymysql


def get_page_html():
    page_num = 1
    db = pymysql.connect(host='localhost', user='root', password='', port=3306)
    cursor = db.cursor()
    cursor.execute('use 52guzhung')
    while True:
        name_id = 11
        url = 'http://52guzhuang.com/forum-59-{0}.html'.format(page_num)
        html = requests.get(url).text
        HTML = etree.HTML(html)
        result = HTML.xpath('//div[@class="v-link"]/a/@href')
        for i in result:
            response = requests.get(i).text
            HTML2 = etree.HTML(response)
            result2 = HTML2.xpath('//div[@align="center"]/ignore_js_op/img/@zoomfile')

            for i in result2:
                pic_url = 'http://52guzhuang.com/' + str(i)
                # pic = requests.get(pic_url)
                # with open(r'F:\python3网络爬虫（1）\picture\{0}.jpg'.format(name_id), 'wb+') as file:
                #     file.write(pic.content)#下载到本地
                #     name_id +=1
                sql = 'INSERT INTO url_(id,url) values(%s,%s);'

                try:
                    cursor.execute(sql, (0, pic_url))
                    print('插入成功')
                    db.commit()
                except:
                    db.rollback()
                    print('插入失败')
                    db.close()
                # print(pic_url)
        if page_num == 10:  # 取到page_num - 1 页
            # file.close()
            db.close()
            break
        page_num += 1


# for i in range(4):
#     t = threading.Thread(target=get_page_html)
#     t.start()

get_page_html()
