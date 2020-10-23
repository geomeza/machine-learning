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

arr = [[1, 2, 3], [0, 1, 1], [1, 0, 4], [0, 2, 0]]
print(df1.to_array())
assert df1.array == arr, 'Wrong Array'
print('Array Test Passed')
assert df1.columns == ['Pete', 'John', 'Sara'], 'Wrong Columns'
print('column test passed')

# df2 = df1.filter_columns(['Sara', 'Pete'])
# arr = [[3, 1],[1, 0],[4, 1],[0, 0]]
# df2.to_array()
# assert df2.array == arr, 'Wrong Array'
# print('Array Test Passed')
# assert df2.columns == ['Sara', 'Pete'], 'Wrong Columns'
# print('Column Test Passed')

# def multiply_by_4(x):
#     return 4*x
# df2 = df1.apply('John', multiply_by_4)
# df2.to_array()

# arr = [[1, 8, 3], [0, 4, 1], [1, 0, 4], [0, 8, 0]]
# assert df2.array == arr, 'Wrong array'
# print('Array Test Passed')

# arr = [[1, 2, 3, 2, 3, 6], [0, 1, 1, 0, 0, 1], [1, 0, 4, 0, 4, 0], [0, 2, 0, 0, 0, 0]]
# data_dict = {
#     'Pete': [1, 0, 1, 0],
#     'John': [2, 1, 0, 2],
#     'Sara': [3, 1, 4, 0]
# }
# df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sara'])
# df2 = df1.append_pairwise_interactions()
# df2.to_array()
# assert df2.array == arr,'Wrong Array'
# print('Array Test Passed')
# print('All tests Passed')

# print('Append and delete and dummy tests')

# data_dict = {
#     'id': [1, 2, 3, 4],
#     'color': ['blue', 'yellow', 'green', 'yellow']
# }

# df1 = DataFrame(data_dict, column_order = ['id', 'color'])
# df2 = df1.create_dummy_variables()

# assert df2.columns == ['id', 'color_blue', 'color_yellow', 'color_green'], 'Wrong columns'

# df3 = df2.remove_columns(['id', 'color_yellow'])
# assert df3.columns == ['color_blue', 'color_green'], 'Wrong columns'

# df4 = df3.append_columns({
#     'name': ['Anna', 'Bill', 'Cayden', 'Daphnie'],
#     'letter': ['a', 'b', 'c', 'd']
# })
# assert df4.columns == ['color_blue', 'color_green', 'name', 'letter'], 'Wrong Columns'

# df4.to_array()
# assert df4.array == [[1, 0, 'Anna', 'a'], [0, 0, 'Bill', 'b'], [0, 1, 'Cayden', 'c'], [0, 0, 'Daphnie', 'd']], 'Wrong Array'

# print('Passed')
# print('--------------------------')
# data_dict = {
#     'beef': [0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5],
#     'pb': [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5],
#     'condiments': [[],['mayo'],['jelly'],['mayo','jelly'],
#                    [],['mayo'],['jelly'],['mayo','jelly'],
#                    [],['mayo'],['jelly'],['mayo','jelly'],
#                    [],['mayo'],['jelly'],['mayo','jelly']],
#     'rating': [1, 1, 4, 0, 4, 8, 1, 0, 5, 0, 9, 0, 0, 0, 0, 0]
# }

# df = DataFrame(data_dict, column_order = ['beef', 'pb', 'condiments'])
# print(df.columns)
# df.to_array()
# print(df.array)
# df = df.create_dummy_variables()
# print(df.columns)
# df.to_array()
# print(df.array)
# df = df.append_columns({
#     'constant': [1 for _ in range(len(data_dict['rating']))],
#     'rating': data_dict['rating']
# })
# print(df.columns)
# df.to_array()
# print(df.array)