import sys
sys.path.append('src')
from dataframe import DataFrame

data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sara': [3, 1, 4, 0]
}

df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sara'])

assert df1.data_dict == data_dict, 'Wrong Dictionary'

arr = [[1, 2, 3],[0, 1, 1],[1, 0, 4],[0, 2, 0]]
df1.to_array()
assert df1.array == arr, 'Wrong Array'
print('Array Test Passed')
assert df1.columns == ['Pete', 'John', 'Sara'], 'Wrong Columns'
print('column test passed')

df2 = df1.filter_columns(['Sara', 'Pete'])
arr = [[3, 1],[1, 0],[4, 1],[0, 0]]
df2.to_array()
assert df2.array == arr, 'Wrong Array'
print('Array Test Passed')
assert df2.columns == ['Sara', 'Pete'], 'Wrong Columns'
print('Column Test Passed')

def multiply_by_4(x):
    return 4*x
df2 = df1.apply('John', multiply_by_4)
df2.to_array()

arr = [[1, 8, 3], [0, 4, 1], [1, 0, 4], [0, 8, 0]]
assert df2.array == arr, 'Wrong array'
print('Array Test Passed')