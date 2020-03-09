# -*- coding: cp936 -*-
# 如何导入模块
import math
    math.pi
#sys模块
#python官方提供的自带的模块

#一、
#1.如何查看系统信息
sys.version
'2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)]'
#2.查看当前编辑目录的地址
sys.executable
'C:\\Python27\\pythonw.exe'
#3.查看Windows 版本一些信息
sys.getwindowsversion()
sys.getwindowsversion(major=6, minor=2, build=9200, platform=2, service_pack='')
#4.查看已经导入的模块关键字
sys.modules.keys()
['heapq', 'code', 'tkFileDial 等等

#二、字节编译
#1. .pyc文件就是经过变异后的模块对应的为二进制文件
#2. 字节编译与编译的区别


#from...import 使用
python中导入一个模块的方法可以使用import，但是import只是导入了这个模块
而并没有导入我们模块的某个属性或方法。而我们要不仅导入一个模块，还有导入模块中对
对应的一个功能，我们可以使用from。。。import语句。
from sys import version
    version
'2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)]'

#学会使用from...import*
如果我们想一次性把这个模块的所有功能，也就是所有的属性有方法都导入的话，我们可以使用
from...import*语句
