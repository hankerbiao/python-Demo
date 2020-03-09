from selenium import webdriver
import time
from PIL import Image

driver = webdriver.Chrome()
driver.get('http://172.16.88.104/')
driver.maximize_window()
picture_url = driver.get_screenshot_as_file('a.png', )
time.sleep(2)
driver.find_element_by_xpath(
    '/html/body/table/tbody/tr/td/table[3]/tbody/tr[1]/td[2]/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input').send_keys(
    '1707100219')
driver.find_element_by_xpath(
    '/html/body/table/tbody/tr/td/table[3]/tbody/tr[1]/td[2]/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').send_keys(
    'hanker9527')
location = driver.find_element_by_id('vchart').location
size = driver.find_element_by_id('vchart').size
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']
a = Image.open("a.png")
im = a.crop((left, top, right, bottom))
im.save('a.png')
Image._show(im)
yzm = input("请输入验证码：")
driver.find_element_by_xpath(
    '/html/body/table/tbody/tr/td/table[3]/tbody/tr[1]/td[2]/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').send_keys(
    yzm)
driver.find_element_by_xpath('//*[@id="btnSure"]').click()

"""
公众号：城建417
"""
