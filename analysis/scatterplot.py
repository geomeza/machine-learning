import matplotlib.pyplot as plt

data = [[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],
    [3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],
    [2,12,'B'],[2,12,'B'],
    [3,12,'A'],[3,12,'A'],
    [3,11,'A'],[3,11,'A'],
    [3,11.5,'A'],[3,11.5,'A'],
    [4,11,'A'],[4,11,'A'],
    [4,11.5,'A'],[4,11.5,'A'],
    [2,10.5,'A'],[2,10.5,'A'],
    [3,10.5,'B'],
    [4,10.5,'A']]


points = {}

for point in data:
    if point[2] == 'B':
        color = 'red'
    if point[2] == 'A':
        color = 'blue'
    if (point[0], point[1], color) in points:
        points[(point[0], point[1], color)].append(point)
    else:
        points[(point[0], point[1], color)] = [point]

red_x = []
red_y = []
red_size = []

blue_x = []
blue_y = []
blue_size = []
for coords, points in points.items():
    # print(coords, points)
    if coords[2] == 'red':
        red_x.append(coords[0])
        red_y.append( coords[1])
        red_size.append(30*len(points))
    elif coords[2] == 'blue':
        blue_x.append(coords[0])
        blue_y.append(coords[1])
        blue_size.append(30*len(points))

plt.scatter(x=red_x, y=red_y, s= red_size, c='blue')
plt.scatter(x=blue_x, y=blue_y, s=blue_size, c='red')
plt.savefig('scatter.png')
plt.show()
