import matplotlib.pyplot as plt
import math
import random

random.seed(0)
# construt fake data
s = 3
num = 30
x1 = [random.random()*s+5 for _ in range(num)]
y1 = [random.random()*s+5 for _ in range(num)]
x2 = [random.random()*s+10 for _ in range(num)]
y2 = [random.random()*s+10 for _ in range(num)]
x3 = [random.random()*s+5 for _ in range(num)]
y3 = [random.random()*s+10 for _ in range(num)]

data_x = x1 + x2 + x3
data_y = y1 + y2 + y3


# start to clustering
init_points = 3
stop_distance = 0.1  # 如果所有点移动的平均距离小于该值，终止迭代
center_points = [(random.choice(data_x),random.choice(data_y)) for _ in range(init_points)]

while True:
    # 计算距离
    print(center_points)
    distances = [[] for _ in range(init_points)]
    for (x, y) in zip(data_x, data_y):
        temp_dis = []
        for (center_x, center_y) in center_points:
            d = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            temp_dis.append(d)
        max_index = temp_dis.index(min(temp_dis))
        distances[max_index].append((x, y))
    # 重新计算中心点
    new_center_points = []
    for index, block in enumerate(distances):
        temp_x = sum([item[0] for item in block])/(len(block)+0.000001)
        temp_y = sum([item[1] for item in block])/(len(block)+0.000001) #稳定数值
        new_center_points.append((temp_x, temp_y))
    # 计算点移动距离是否满足终止条件
    stop_value = 0
    for i in range(init_points):
        stop_value = stop_value + math.sqrt((center_points[index][0]-new_center_points[index][0])**2+
        (center_points[index][1]-new_center_points[index][1])**2)
    center_points = new_center_points
    if stop_value < stop_distance:
        break
plt.scatter(data_x, data_y, c='b')
cluster_x = [item[0] for item in center_points]
cluster_y = [item[1] for item in center_points]
#plt.scatter(cluster_x, cluster_y, c='r')
plt.show()