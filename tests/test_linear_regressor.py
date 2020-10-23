import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
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
assert df.columns == ['beef', 'pb', 'condiments'], 'Wrong columns'

df = df.create_dummy_variables()
df = df.append_pairwise_interactions()
df = df.append_columns({
    'constant': [1 for _ in range(len(data_dict['rating']))],
    'rating': data_dict['rating']
})
assert df.columns == ['beef', 'pb', 'mayo', 'jelly', 'beef_pb', 'beef_mayo', 'beef_jelly', 'pb_mayo', 'pb_jelly', 'mayo_jelly', 'constant', 'rating'], 'Wrong Columns'

linear_regressor = LinearRegressor(df, prediction_column = 'rating')
coeffs = {
    'beef': 0.25,
    'pb': 0.4,
    'mayo': -1.25,
    'jelly': 1.5,
    'beef_pb': -0.21,
    'beef_mayo': 1.05,
    'beef_jelly': -0.85,
    'pb_mayo': -0.65,
    'pb_jelly': 0.65,
    'mayo_jelly': -3.25,
    'constant': 2.1875
}

assert linear_regressor.coefficients == coeffs, 'Wrong Coeffs'
linear_regressor.gather_all_inputs({
    'beef': 5,
    'pb': 5,
    'mayo': 1,
    'jelly': 1,
})

input_dict = {
    'beef': [5],
    'pb': [5],
    'mayo': [1],
    'jelly': [1],
    'beef_pb': [25],
    'beef_mayo': [5],
    'beef_jelly': [5],
    'pb_mayo': [5],
    'pb_jelly': [5],
    'mayo_jelly': [1],
    'constant': [1]
}

assert linear_regressor.current_input.data_dict == input_dict, 'Wrong INputs'

assert linear_regressor.predict({
    'beef': 5,
    'pb': 5,
    'mayo': 1,
    'jelly': 1,
}) == -1.8125, 'Nah'

assert linear_regressor.predict({
    'beef': 0,
    'pb': 3,
    'mayo': 0,
    'jelly': 1,
}) == 6.8375, 'Nah'

assert linear_regressor.predict({
    'beef': 1,
    'pb': 1,
    'mayo': 1,
    'jelly': 0,
}) == 1.7775, 'Nah'

assert linear_regressor.predict({
    'beef': 6,
    'pb': 0,
    'mayo': 1,
    'jelly': 0,
}) == 8.7375, 'Nah'
print('Passed')