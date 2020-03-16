import numpy as np
import time
# 二分查找算法


def binary_search(list, item):
    low = 0  # 第一个值的下坐标
    hight = len(list) - 1  # 最后一个值下的坐标

    while low <= hight:
        mid = round((low + hight) / 2)  # 中间值坐标位置
        # guss表示程序猜的数
        guss = list[mid]  # 从列表中间开始猜，把列表中间位置的元素值赋值给guss
        # guss开始猜
        if guss == item:  # 如果程序猜的值和输入的值相等
            return mid  # 返回此值的下坐标
        if guss > item:
            hight = mid - 1  # 如果猜的值大于输入的值，则猜的值-1当做最大值
        if guss < item:
            low = mid + 1  # 如果猜的值小于输入的值，则猜的值+1为当做最小值
    return None  # 没有值的话返回空

if __name__ == '__main__':
    list = np.arange(1000000000)
    start_time = time.time()
    print(binary_search(list, 125695246))
    end_time = time.time()
    print(end_time - start_time)

