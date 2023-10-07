import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# 生成数据
x = np.arange(0, 6, 0.1)  # 以0.1为单位，生成0到6的数据
y = np.sin(x)
print(x, y)
# 绘制图形
plt.plot(x, y)
plt.show()

y2 = np.cos(x)
# 绘制图形
plt.plot(x, y, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")  # line style用虚线绘制 label标签
plt.xlabel("x")  # x轴标签
plt.ylabel("y")  # y轴标签
plt.title('sin & cos')  # 标题
plt.legend()
plt.show()

# 显示图像 imread读取图像
img = imread('szyf.png')  # 读入图像（设定合适的路径！）
plt.imshow(img)
plt.show()
