# -*- coding: cp936 -*-
# ��ε���ģ��
import math
    math.pi
#sysģ��
#python�ٷ��ṩ���Դ���ģ��

#һ��
#1.��β鿴ϵͳ��Ϣ
sys.version
'2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)]'
#2.�鿴��ǰ�༭Ŀ¼�ĵ�ַ
sys.executable
'C:\\Python27\\pythonw.exe'
#3.�鿴Windows �汾һЩ��Ϣ
sys.getwindowsversion()
sys.getwindowsversion(major=6, minor=2, build=9200, platform=2, service_pack='')
#4.�鿴�Ѿ������ģ��ؼ���
sys.modules.keys()
['heapq', 'code', 'tkFileDial �ȵ�

#�����ֽڱ���
#1. .pyc�ļ����Ǿ���������ģ���Ӧ��Ϊ�������ļ�
#2. �ֽڱ�������������


#from...import ʹ��
python�е���һ��ģ��ķ�������ʹ��import������importֻ�ǵ��������ģ��
����û�е�������ģ���ĳ�����Ի򷽷���������Ҫ��������һ��ģ�飬���е���ģ���ж�
��Ӧ��һ�����ܣ����ǿ���ʹ��from������import��䡣
from sys import version
    version
'2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)]'

#ѧ��ʹ��from...import*
���������һ���԰����ģ������й��ܣ�Ҳ�������е������з���������Ļ������ǿ���ʹ��
from...import*���
