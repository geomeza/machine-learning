import sys
sys.path.append('src')
from dataframe import DataFrame
from node import Node
from decision_tree import DecisionTree

# df = DataFrame.from_array(
# [[1, 11, 'A'],
# [1, 12, 'A'],
# [2, 11, 'A'],
# [1, 13, 'B'],
# [2, 13, 'B'],
# [3, 13, 'B'],
# [3, 11, 'B']],
# columns = ['x', 'y', 'class'])

# dt = DecisionTree(df)
# dt.split()


# print('\nTesting root indices')
# assert dt.root.row_indices == [0, 1, 2, 3, 4, 5, 6]
# print('passed')

# print('\nTesting root class counts')
# assert dt.root.class_counts == {'A': 3,'B': 4}
# print('passed')

# print('\nTesting root impurity')
# assert round(dt.root.impurity,3) == 0.490
# print('passed')

# print('\nTesting root possible splits')
# rounded = [[entry[0], entry[1], round(entry[2],3)] for entry in dt.root.possible_splits.to_array()]
# assert rounded ==  [['x', 1.5,  0.085], ['x', 2.5,  0.147],['y', 11.5, 0.085], ['y', 12.5, 0.276]]
# print('passed')

# print('\nTesting root best_split')
# assert dt.root.best_split == ('y', 12.5)
# print('passed')

# print('\nTesting root low indices')
# assert dt.root.low.row_indices == [0, 1, 2, 6]
# print('passed')

# print('\nTesting root high indices')
# assert dt.root.high.row_indices == [3, 4, 5]
# print('passed')

# print('\nTesting root low impurity')
# assert round(dt.root.low.impurity,3) == 0.375
# print('passed')

# print('\nTesting root high impurity')
# assert dt.root.high.impurity == 0
# print('passed')

# print('\nTesting root low possible splits')
# rounded = [[entry[0], entry[1], round(entry[2], 3)] for entry in dt.root.low.possible_splits.to_array()]
# assert rounded == [['x', 1.5,  0.125], ['x', 2.5,  0.375], ['y', 11.5, 0.042]]
# print('passed')

# print('\nTesting root low best split')
# assert dt.root.low.best_split == ('x', 2.5)
# print('passed')

# print('\nTesting root low low indices')
# dt.split()
# assert dt.root.low.low.row_indices == [0, 1, 2]
# print('passed')

# print('\nTesting root low high indices')
# assert dt.root.low.high.row_indices == [6]
# print('passed')

# print('\nTesting root low low impurity')
# assert dt.root.low.low.impurity == 0
# print('passed')

# print('\nTesting root low high impurity')
# assert dt.root.low.high.impurity == 0
# print('passed')

print('Splitting Tests')
df = DataFrame.from_array(
    [[1, 11, 'A'],
    [1, 12, 'A'],
    [2, 11, 'A'],
    [1, 13, 'B'],
    [2, 13, 'B'],
    [3, 13, 'B'],
    [3, 11, 'B']],
    columns = ['x', 'y', 'class']
)

dt = DecisionTree()
dt.initialize(df)
dt.split()
dt.split()

assert dt.root.high.row_indices == [3, 4, 5]
assert dt.root.low.low.row_indices == [0, 1, 2]
assert dt.root.low.high.row_indices == [6]
print('passed')
dt = DecisionTree()
dt.fit(df)
assert dt.root.high.row_indices == [3, 4, 5]
assert dt.root.low.low.row_indices == [0, 1, 2]
assert dt.root.low.high.row_indices == [6]
print('passed')

print('Classification Tests')
df = DataFrame.from_array(
    [[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],
    [3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],
    [2,12,'B'],[2,12,'B'],
    [3,12,'A'],[3,12,'A'],
    [3,11,'A'],[3,11,'A'],
    [3,11.5,'A'],[3,11.5,'A'],
    [4,11,'A'],[4,11,'A'],
    [4,11.5,'A'],[4,11.5,'A'],
    [2,10.5,'A'],[2,10.5,'A'],
    [3,10.5,'B'],
    [4,10.5,'A']],
    columns = ['x', 'y', 'class']
)
dt = DecisionTree()
dt.fit(df)

assert dt.classify({'x': 2, 'y': 11.5}) == 'B', 'Wrong Classification'
assert dt.classify({'x': 2.5, 'y': 13}) == 'B', 'Wrong Classification'
assert dt.classify({'x': 4, 'y': 12}) == 'A', 'Wrong Classification'
assert dt.classify({'x': 3.25, 'y': 10.5}) == 'B', 'Wrong Classification'
assert dt.classify({'x': 3.75, 'y': 10.5}) == 'A', 'Wrong Classification'

print('passed')
