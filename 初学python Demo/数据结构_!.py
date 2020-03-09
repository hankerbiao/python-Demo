# -*- coding: cp936 -*-
#数据结构: 栈
#什么是栈：数据结构，不是系统自带的，  栈相当于一段开口 一段封闭的容器
#python中栈的实现  存储方式e
"""
class Stack():
    def __init__(st,size):    #__init__初始化函数的名称   （主体  容量）
        st.stack=[];         #st.  栈的属性 最初是列表
        st.size=size;         #规定栈的容量   赋值给 st.size
        st.top=-1;            #初始化栈顶的位置
#入栈
    def push(st,content):
        if st.Full():
            print "zhan man le "

        else:
            st.stack.append(content)
            st.top=st.top+1

    def out(st):    #出栈
        if st.Empty():
            print "zhan kong le"
        else:
            st.top=st.top-1

    def Full(st):
        if st.top ==st.size:
            return True
        else:
            return False

    def Empty(st):
        if st.top==-1:
            return True
        else:
            return False
        

#出栈
"""





#队列



