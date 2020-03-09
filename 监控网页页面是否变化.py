import smtplib
from email.mime.text import MIMEText
import requests
from lxml import etree

url = 'http://onsgep.moe.edu.cn/edoas2/website7/level2.jsp?infoid=1335254343701173&location=TZGG'
html = requests.get(url).text
HTML = etree.HTML(html)
title = HTML.xpath('//td[@class="news_font"]/a/@title')
frist = title[0]


def Send(content):
    msg_from = '@qq.com'  # 发送方邮箱
    passwd = ''  # 填入发送方邮箱的授权码
    msg_to = '@qq.com'  # 收件人邮
    subject = '不知道起啥名字'  # 主题

    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())


def main():
    if len(frist) != 42:
        now_title = frist
        Send(now_title)


if __name__ == '__main__':
    main()
