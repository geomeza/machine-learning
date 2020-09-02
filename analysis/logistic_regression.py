import sys
sys.path.append('src')
from matrix import Matrix
import math
import matplotlib.pyplot as plt

def approximation(data):
    X_data = [[1,x] for x,y in data]
    Y_data = [[math.log((1/(y)) - 1)] for x,y in data]
    X = Matrix(elements = X_data)
    Y = Matrix(elements = Y_data)
    x_transpose = X.transpose()
    square = x_transpose.matrix_mult(X)
    inverse = square.inverse()
    matr  = x_transpose.matrix_mult(Y)
    return inverse.matrix_mult(matr)

def solve_coefficients(data):
    coeff = approximation(data).elements
    coefficients = []
    for elem in coeff:
        for element in elem:
            coefficients.append(element)
    return coefficients


data = [(10, 0.05), (100, 0.35), (1000, 0.95)]

coefficients = solve_coefficients(data)

def win_probability(coefficients, hours_played):
    exponential = coefficients[0] + coefficients[1] * hours_played
    e_value = math.exp(exponential)
    return 1/(1 + e_value)

def average_hours_played(coefficients, win_probability):
    value = math.log((1/win_probability) - 1)
    return (value - coefficients[0])/coefficients[1]

print('\nWin Probabilty Against AVG Player with 500 Hrs Played:')
print('\n', round(win_probability(coefficients, 500), 2) * 100, 'Percent')

print('\nAvg Hours Played For AVG Player:')
print('\n',round(average_hours_played(coefficients, 0.5), 2))
