import sys
sys.path.append('src')
from dataframe import DataFrame
from node import Node
from decision_tree import DecisionTree

pos_neg = [[x, y, 'POS'] if x > 0 and y > 0 else (x, y, 'NEG')
           for y in range(-5, 6) for x in range(-5, 6) if x*y != 0]


def into_observation(array):
    return {'x': array[0], 'y': array[1]}


df = DataFrame.from_array(pos_neg, columns=['x', 'y', 'class'])
r = DecisionTree('gini')
r.fit(df)
correct = 0
assert len(list(r.splits.values())) == 2,'WRONG SPLITS BRUH'
for i in range(len(pos_neg)):
    correct_class = pos_neg[i][2]
    observation = into_observation(pos_neg[i])
    classification = r.classify(observation)
    if classification == correct_class:
        correct += 1

assert correct/len(pos_neg) * 100 == 100, 'WRONG ACCURACY BRUH'


pos_neg = [[x, y, 'POS'] if x*y > 0 else (x, y, 'NEG')
           for y in range(-5, 6) for x in range(-5, 6) if x*y != 0]


def into_observation(array):
    return {'x': array[0], 'y': array[1]}


df = DataFrame.from_array(pos_neg, columns=['x', 'y', 'class'])
r = DecisionTree('gini')
r.fit(df)
correct = 0
for i in range(len(pos_neg)):
    correct_class = pos_neg[i][2]
    observation = into_observation(pos_neg[i])
    classification = r.classify(observation)
    if classification == correct_class:
        correct += 1

assert correct/len(pos_neg) * 100 == 100, 'WRONG ACCURACY BRUH'

points = [[x,y,'A'] for y in range(-5, 6) for x in range(-5, 6) if x*y != 0]
points.extend([[x,y,'B'] for y in range(1, 6) for x in range(1, 6) if x*y != 0])
points.extend([[x,y,'B'] for y in range(1, 6) for x in range(1, 6) if x*y != 0])

df = DataFrame.from_array(points, columns=['x', 'y', 'class'])
r = DecisionTree('gini')
r.fit(df)
correct = 0
for i in range(len(points)):
    correct_class = points[i][2]
    observation = into_observation(points[i])
    classification = r.classify(observation)
    if classification == correct_class:
        correct += 1

assert round(correct/len(points)*100,2) == 83.33, 'WRONG ACCURACY BRUH'

pos_neg = [[x, y, z, 'POS'] if x*y > 0 else (x, y, z,'NEG')
           for z in range(-5, 6)for y in range(-5, 6) for x in range(-5, 6) if x*y*z != 0]

def into_new_observation(array):
    return {'x': array[0], 'y': array[1], 'z' : array[2]}

df = DataFrame.from_array(pos_neg, columns=['x', 'y', 'z', 'class'])
r = DecisionTree('gini')
r.fit(df)
correct = 0
for i in range(len(pos_neg)):
    correct_class = pos_neg[i][3]
    observation = into_new_observation(pos_neg[i])
    classification = r.classify(observation)
    if classification == correct_class:
        correct += 1

assert correct/len(pos_neg) * 100 == 100, 'WRONG ACCURACY BRUH'

points = [[x,y,z,'A'] for z in range(-5,6) for y in range(-5, 6) for x in range(-5, 6) if x*y*z != 0]
points.extend([[x,y,z,'B'] for z in range(1,6) for y in range(1, 6) for x in range(1, 6) if x*y*z != 0])
points.extend([[x,y,z,'B'] for z in range(1,6) for y in range(1, 6) for x in range(1, 6) if x*y*z != 0])

df = DataFrame.from_array(points, columns=['x', 'y','z', 'class'])
r = DecisionTree('gini')
r.fit(df)
correct = 0

for i in range(len(points)):
    correct_class = points[i][3]
    observation = into_new_observation(points[i])
    classification = r.classify(observation)
    if classification == correct_class:
        correct += 1

assert correct/len(points) * 100 == 90, 'WRONG ACCURACY BRUH'

print('passed')