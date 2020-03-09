# -*- coding: cp936 -*-
#函数
#len()   取字符串长度
#---------------------
#split    分割字符串
#a = "nihaopython"
#b = a.split("a")
#print b
#---------------------
#自定义函数
def a():
    print  "heloo "
a()
#---------------------

#函数定义格式

def 函数名():
    函数内容;函数内容
    函数内容;函数内容

	def fun2(a,b):
    if a>b:
        print a;print"前面的数大"
    else:
       print b 
fun2(1,4)
a = "nihao python"
b = a.split("a")
print b

# 形参 ：函数定义  实参：函数调用

#参数的传递
#
# -*- coding: cp936 -*-
#局部变量
def max(a,b):
    if a>b:
        print a
    else:
        print b
max(3,4)

#全局变量  global
def fun1():
    global i
    i = 5
    print i
fun1()
print i

#函数的调用

比如一个函数是
def func3（）：
func3（） //调用即可

例
def a():
    i = 1
a()


#函数的返回值
函数的返回值是通过return语句来实现的 ，r让函数变成一个具有一个值的函数

#一个返回值的情况
def test():
    i=7
    return i    //变成了一个整体
print test()

#返回多个指值
def fun3(i,j):
    k=i*j
    return(i,j,k)

#print fun3(3,4)
x,y,z=fun3(4,5)
print z

# -*- coding: cp936 -*-
# 文档字符串
#为每一个函数进行文档说明
#文档字符，在每个函数开头的地方 加上一行说明性文字


#文档字符串 编写使用规则
#       a.第一行紧挨着定义的函数
#       b.用三引号
#       c.第二行空开，第一行概括，后面具体些描述
#       d.句末都使用。 第一个字母大写


#文档字符串的使用
#def f(a,b):
 
    这是一个乘法函数

    函数会返回一个乘法运算结果。
   
#    k = a*b
#    return k
#print f.__doc__

输出

    这是一个乘法函数

    函数会返回一个乘法运算结果。

#help(f)


输出
f(a, b)
    这是一个乘法函数
    
    函数会返回一个乘法运算结果。



