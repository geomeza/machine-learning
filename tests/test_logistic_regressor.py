import sys
sys.path.append('src')
from logistic_regressor import LogisticRegressor
from dataframe import DataFrame

data_dict = {
    'beef': [0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5],
    'pb': [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5],
    'condiments': [[],['mayo'],['jelly'],['mayo','jelly'],
                   [],['mayo'],['jelly'],['mayo','jelly'],
                   [],['mayo'],['jelly'],['mayo','jelly'],
                   [],['mayo'],['jelly'],['mayo','jelly']],
    'rating': [1, 1, 4, 0, 4, 8, 1, 0, 5, 0, 9, 0, 0, 0, 0, 0]
}


df = DataFrame(data_dict, column_order = ['beef', 'pb', 'condiments'])
df = df.create_dummy_variables()
df = df.append_pairwise_interactions()
df = df.append_columns({
    'constant': [1 for _ in range(len(data_dict['rating']))],
    'rating': data_dict['rating']
})



df = df.apply('rating', lambda x: 0.1 if x==0 else x)

regressor = LogisticRegressor(df, prediction_column = 'rating', max_val = 10)

assert regressor.multipliers == [-0.039, -0.0205, 1.7483, -0.3978, 0.1497, -0.7485, 0.4682, 0.3296, -0.5288, 2.6441, 1.0125], 'Wong multipliers'

print(regressor.dataframe.to_array())

assert regressor.predict({
    'beef': 5,
    'pb': 5,
    'mayo': 1,
    'jelly': 1,
}) ==  0.02342,'Nah bruh'
assert regressor.predict({
    'beef': 0,
    'pb': 3,
    'mayo': 0,
    'jelly': 1,
}) == 7.37536

assert regressor.predict({
    'beef': 1,
    'pb': 1,
    'mayo': 1,
    'jelly': 0,
}) == 0.80757, 'Nah'

assert regressor.predict({
    'beef': 6,
    'pb': 0,
    'mayo': 1,
    'jelly': 0,
}) == 8.76987, 'Bruh Moment'

print('All Tests Passed')