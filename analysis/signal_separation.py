import math, sys
sys.path.append('src')
from dataframe import DataFrame
from linear_regressor import LinearRegressor

def transform_polynomial_data(data, degree):
    polynomial_dict = {str(i):[] for i in range(degree + 1)}
    polynomial_dict.update({'y': []})
    for x,y in data:
        adjusted_data = [x**i for i in range(degree + 1)]
        for i in range(degree + 1):
            polynomial_dict[str(i)].append(adjusted_data[i])
        polynomial_dict['y'].append(y)
    return polynomial_dict
        
def transform_trigonometric_data(data):
    trigonometry_dict = {str(i):[] for i in range(4)}
    trigonometry_dict.update({'y' : []})
    for x,y in data:
        adjusted_data = [math.sin(x), math.cos(x), math.sin(2*x), math.cos(2*x)]
        for i in range(len(adjusted_data)):
            trigonometry_dict[str(i)].append(adjusted_data[i])
        trigonometry_dict['y'].append(y)
    return trigonometry_dict

polynomial_data = [(0.0, 4.0),
 (0.2, 8.9),
 (0.4, 17.2),
 (0.6, 28.3),
 (0.8, 41.6),
 (1.0, 56.5),
 (1.2, 72.4),
 (1.4, 88.7),
 (1.6, 104.8),
 (1.8, 120.1),
 (2.0, 134.0),
 (2.2, 145.9),
 (2.4, 155.2),
 (2.6, 161.3),
 (2.8, 163.6),
 (3.0, 161.5),
 (3.2, 154.4),
 (3.4, 141.7),
 (3.6, 122.8),
 (3.8, 97.1),
 (4.0, 64.0),
 (4.2, 22.9),
 (4.4, -26.8),
 (4.6, -85.7),
 (4.8, -154.4)]

trigonometry_data = [(0.0, 7.0),
 (0.2, 5.6),
 (0.4, 3.56),
 (0.6, 1.23),
 (0.8, -1.03),
 (1.0, -2.89),
 (1.2, -4.06),
 (1.4, -4.39),
 (1.6, -3.88),
 (1.8, -2.64),
 (2.0, -0.92),
 (2.2, 0.95),
 (2.4, 2.63),
 (2.6, 3.79),
 (2.8, 4.22),
 (3.0, 3.8),
 (3.2, 2.56),
 (3.4, 0.68),
 (3.6, -1.58),
 (3.8, -3.84),
 (4.0, -5.76),
 (4.2, -7.01),
 (4.4, -7.38),
 (4.6, -6.76),
 (4.8, -5.22)]

adjusted_polynomial_data = transform_polynomial_data(polynomial_data, 3)
df = DataFrame(adjusted_polynomial_data)
regressor = LinearRegressor(df, 'y')
print(regressor.coefficients)

adjusted_trigonometric_data = transform_trigonometric_data(trigonometry_data)
df = DataFrame(adjusted_trigonometric_data)
regressor = LinearRegressor(df, 'y')
print(regressor.coefficients)
