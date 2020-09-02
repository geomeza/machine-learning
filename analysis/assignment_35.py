import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor
from matrix import Matrix
import math

data = [[ 1, 0,  0,  0,  0,   0,  0,  0,  0,  0,  0,  1],
        [ 1, 0,  0,  1,  0,    0,  0,  0,  0,  0,  0,  1],
        [ 1, 0,  0,  0,  1,    0,  0,  0,  0,  0,  0,  4],
        [ 1, 0,  0,  1,  1,   0,  0,  0,  0,  0,  1,  0.1],
        [ 1, 5,  0,  0,  0,    0,  0,  0,  0,  0,  0,  4],
        [ 1, 5,  0,  1,  0,     0,  5,  0,  0,  0,  0,  8],
        [ 1, 5,  0,  0,  1,     0,  0,  5,  0,  0,  0,  1],
        [ 1, 5,  0,  1,  1,    0,  5,  5,  0,  0,  1,  0.1],
        [ 1, 0,  5,  0,  0,     0,  0,  0,  0,  0,  0,  5],
        [ 1, 0,  5,  1,  0,    0,  0,  0,  5,  0,  0,  0.1],
        [ 1, 0,  5,  0,  1,      0,  0,  0,  0,  5,  0,  9],
        [ 1, 0,  5,  1,  1,    0,  0,  0,  5,  5,  1,  0.1],
        [ 1, 5,  5,  0,  0,   25,  0,  0,  0,  0,  0,  0.1],
        [ 1, 5,  5,  1,  0,   25,  5,  0,  5,  0,  0,  0.1],
        [ 1, 5,  5,  0,  1,   25,  0,  5,  0,  5,  0,  0.1],
        [ 1, 5,  5,  1,  1,   25,  5,  5,  5,  5,  1,  0.1]]

def split_data(data):
    results = []
    new_data = []
    for i in range(len(data)):
        new_data.append([])
        for j in range(len(data[0])):
            if j == len(data[0]) - 1:
                results.append([math.log((10/data[i][j]) - 1)])
            else:
                new_data[i].append(data[i][j])
    return [new_data, results]

split = split_data(data)
sandwich_data = Matrix(elements = split[0])
sandwich_ratings = Matrix(elements = split[1])

regressor = PolynomialRegressor(2)

regressor.solve_coefficients_with_inputs(sandwich_data, sandwich_ratings)

coeffs = regressor.coefficients

def make_interactions(starters):
    all_interactions = []
    for i in range(len(starters)):
        all_interactions.append(starters[i])
    for i in range(len(starters)):
        for j in range(len(starters)):
            if j > i:
                all_interactions.append(starters[i] * starters[j])
    all_interactions.insert(0,1)
    return all_interactions

def assertion(prediction, solution):
    assert prediction == solution, ('Wrong Should Be',solution,'Got',prediction)
    print('\n   Passed')

tests = [[0,0,0,0], [0,0,1,0], [0,0,1,1], [5,0,1,0], [0,5,0,1], [5,5,1,1]]

solutions = [2.66, 0.59, 0.07, 7.64, 8.94, 0.02]

elems = [' Beef & ', ' PB & ', 'Mayo & ', 'Jelly ']

for i in range(len(tests)):
    print('\n---------------------------------')
    title = 'Testing '
    for j in range(len(tests[i])):
        if j < 2:
            title += str(tests[i][j])
        title += elems[j]
    print('\n',title)
    data = make_interactions(tests[i])
    evaluation = round(regressor.evaluate_with_inputs(data),2)
    assertion(evaluation, solutions[i])
    print('\n---------------------------------')

