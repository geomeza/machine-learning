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
        new_dict_data = [element for elem in coeffs for element in elem]
        self.coefficients = {key: round(new_dict_data[i],4) for i, key in enumerate(self.dataframe.data_dict) if key != self.prediction}
        return self.coefficients

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
