from dataframe import DataFrame
from matrix import Matrix

class LinearRegressor:

    def __init__(self, data_frame, prediction_column):
        self.dataframe = data_frame
        self.prediction = prediction_column
        self.coefficients = self.solve_coefficients()
        self.current_input = None

    def approx(self):
        x_matr = self.dataframe.remove_columns([self.prediction]).to_array()
        y_matr = self.dataframe.remove_columns([key for key in self.dataframe.data_dict if key != self.prediction]).to_array()
        X = Matrix(x_matr)
        Y = Matrix(y_matr)
        x_transpose = X.transpose()
        square = x_transpose.matrix_mult(X)
        inverse = square.inverse()
        matr  = x_transpose.matrix_mult(Y)
        return inverse.matrix_mult(matr)

    def solve_coefficients(self):
        coeffs = self.approx().elements
        new_dict_data = []
        keys = [key for key in self.dataframe.data_dict.keys() if key != self.prediction]
        for elem in coeffs:
            for element in elem:
                new_dict_data.append(element)
        coeffs_dict = {}
        for i in range(len(keys)):
            coeffs_dict.update({keys[i]:round(new_dict_data[i], 4)})
        self.coefficients = coeffs_dict
        return coeffs_dict

    def gather_all_inputs(self, input_dict):
        col_order = [key for key in input_dict.keys()]
        for key,data in input_dict.items():
            input_dict.update({key : [data]})
        data = DataFrame(input_dict, col_order)
        data.append_pairwise_interactions()
        data.append_columns({'constant' : [1]})
        self.current_input = data
        return data.data_dict

    def predict(self, input_dict):
        self.current_input = self.gather_all_inputs(input_dict)
        coeffs = [val for val in self.coefficients.values()]
        inputs = []
        for val in self.current_input.values():
            inputs.append(val[0])
        return sum([coeffs[i]*inputs[i] for i in range(len(coeffs))])

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
# # ['beef', 'pb', 'condiments']

# df = df.create_dummy_variables()
# df = df.append_pairwise_interactions()
# df = df.append_columns({
#     'constant': [1 for _ in range(len(data_dict['rating']))],
#     'rating': data_dict['rating']
# })
# print(df.columns)
# ['beef', 'pb', 'mayo', 'jelly',
#  'beef_pb', 'beef_mayo', 'beef_jelly', 'pb_mayo', 'pb_jelly', 'mayo_jelly'
#  'constant', 'rating']

# linear_regressor = LinearRegressor(df, prediction_column = 'rating')
# print(linear_regressor.coefficients)

# linear_regressor.gather_all_inputs({
#     'beef': 5,
#     'pb': 5,
#     'mayo': 1,
#     'jelly': 1,
# })
# print(linear_regressor.current_input.data_dict)

# print(linear_regressor.predict({
#     'beef': 5,
#     'pb': 5,
#     'mayo': 1,
#     'jelly': 1,
# }))

# print(linear_regressor.predict({
#     'beef': 0,
#     'pb': 3,
#     'mayo': 0,
#     'jelly': 1,
# }))

# print(linear_regressor.predict({
#     'beef': 1,
#     'pb': 1,
#     'mayo': 1,
#     'jelly': 0,
# })
# )
# print(linear_regressor.predict({
#     'beef': 6,
#     'pb': 0,
#     'mayo': 1,
#     'jelly': 0,
# }))
        
        

