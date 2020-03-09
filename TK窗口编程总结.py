# -*- coding: utf-8 -*-
import tkinter as tk  # 使用Tkinter前需要先导入


def Test():
    pass


# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

# 第4步，在图形界面上设定标签
Label = tk.Label(window, text='这是一个标签', bg='green', font=('微软雅黑', 12), width=30, height=2)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

# 第5步，放置标签
Label.pack()  # Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();

# 其他组件

Button = tk.Button(window, text="这是一个按钮", width=10, height=1, command=Test())
Button.place(x=100, y=100)
Entry1 = tk.Entry(window, show='*', font=('Arial', 14))  # 显示成密文形式
Entry2 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
Entry1.pack()
Entry2.pack()
window.mainloop()
