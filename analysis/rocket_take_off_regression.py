import sys
sys.path.append('src')
from polynomial_regressor import polynomial_regressor
from matrix import Matrix

data = [(1, 3.1), (2, 10.17), (3, 20.93), (4, 38.71), (5, 60.91), (6, 98.87), (7, 113.92), (8, 146.95), (9, 190.09), (10, 232.65)]

constant_regressor = polynomial_regressor(degree=2)
constant_regressor.ingest_data(data)
constant_regressor.solve_coefficients()
output = [constant_regressor.coefficients, constant_regressor.evaluate(200)]
print('Quadratic:')
print('Coefficients:',output[0],'\nApprox Pos:',output[1])
print('Error:',constant_regressor.sum_squared_error())


constant_regressor = polynomial_regressor(degree=3)
constant_regressor.ingest_data(data)
constant_regressor.solve_coefficients()
output = [constant_regressor.coefficients, constant_regressor.evaluate(200)]
print('\nCubic:')
print('Coefficients:',output[0],'\nApprox Pos:',output[1])
print('Error:',constant_regressor.sum_squared_error())

print('\nIm not sure which is better, the cubic gives me a smaller error but its also negative so I dont know whats going on there')