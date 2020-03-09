#-*-coding:utf8-*-

from multiprocessing.dummy import Pool as ThreadPool
import requests
import time

def getsource(url):
    html = requests.get(url)

urls = []

for i in range(1,21):
    newpage = 'http://tieba.baidu.com/p/3522395718?pn=' + str(i) #str  表示字符串类,也可以是将变量强制转换为字符串的函数
    urls.append(newpage)# append() 方法向列表的尾部添加一个新的元素。只接受一个参数。

time1 = time.time()
for i in urls:
    print (i)
    getsource(i)
time2 = time.time()
print (u'单线程耗时：' + str(time2-time1))

pool = ThreadPool(2)
time3 = time.time()
results = pool.map(getsource, urls)
pool.close()
pool.join()
time4 = time.time()
print (u'并行耗时：' + str(time4-time3))

