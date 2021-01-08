import sys
sys.path.append('src')
from dataframe import DataFrame
from decision_tree import DecisionTree
from random_forest import RandomForest

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
        [4,10.5,'A'],
        [3, 9.5, 'A'],
        [2,10,'A']]

df = DataFrame.from_array(data, columns = ['x', 'y', 'class'])

r = RandomForest(10)
r.fit(df)
print(r.predict({'x': 3, 'y': 10}))