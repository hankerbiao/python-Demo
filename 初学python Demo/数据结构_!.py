# -*- coding: cp936 -*-
#���ݽṹ: ջ
#ʲô��ջ�����ݽṹ������ϵͳ�Դ��ģ�  ջ�൱��һ�ο��� һ�η�յ�����
#python��ջ��ʵ��  �洢��ʽe
"""
class Stack():
    def __init__(st,size):    #__init__��ʼ������������   ������  ������
        st.stack=[];         #st.  ջ������ ������б�
        st.size=size;         #�涨ջ������   ��ֵ�� st.size
        st.top=-1;            #��ʼ��ջ����λ��
#��ջ
    def push(st,content):
        if st.Full():
            print "zhan man le "

        else:
            st.stack.append(content)
            st.top=st.top+1

    def out(st):    #��ջ
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
        

#��ջ
"""





#����



