from dataframe import DataFrame
from linear_regressor import LinearRegressor
import math

class LogisticRegressor(LinearRegressor):

    def __init__(self, data_frame, prediction_column, max_val):
        self.dataframe = data_frame
        self.prediction = prediction_column
        self.current_input = None
        self.max_val = max_val
        # print(math.log((0.999/0.95) - 1))
        self.dataframe.data_dict[prediction_column] = [math.log((max_val/y) - 1) for y in self.dataframe.data_dict[prediction_column]]
        # self.coefficients = self.solve_coefficients()
        self.multipliers = [val for val in self.solve_coefficients().values()]


    def predict(self, input_dict):
        self.current_input = self.gather_all_inputs(input_dict)
        inputs = [val[0] for val in self.current_input.values()]
        return round(self.max_val/(1+ math.exp(sum([inputs[i]*self.multipliers[i] for i in range(len(self.multipliers))]))), 5)
