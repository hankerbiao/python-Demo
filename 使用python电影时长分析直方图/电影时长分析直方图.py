from matplotlib import pyplot as plt
from matplotlib import font_manager

font = r'C:\Windows\Fonts\FZSTK.TTF'  # 字体

# 有中文的话，设置字体格式，否则会乱码
myfont = font_manager.FontProperties(fname=font, size=20)

#打开文件，读取出爬取的数据
with open("1.txt", 'r') as file:
    data = file.readlines()
a = list()
for i in data:
    a.append(int(i.replace("\n", "")))
#d
d = 5
num_bins = (max(a) - min(a)) // d
plt.figure(figsize=(15, 8), dpi=80)
plt.title("5000部电影,电影时长分析直方图", fontproperties=myfont)
plt.hist(a, num_bins, normed=True, color='orange')
# 设置x轴的刻度
plt.xticks(range(min(a), max(a), d))
plt.xlabel("电影时常 minute", fontproperties=myfont)
plt.ylabel("百分率 %", fontproperties=myfont)
plt.grid()

plt.savefig('./电影时长分析直方图.png')
plt.show()
