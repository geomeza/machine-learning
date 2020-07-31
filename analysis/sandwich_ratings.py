import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor
from matrix import Matrix

#   1 * beta_0 + 0 * beta_1 + 0 * beta_2 = 1
#   1 * beta_0 + 1 * beta_1 + 0 * beta_2 = 2
#   1 * beta_0 + 2 * beta_1 + 0 * beta_2 = 4
#   1 * beta_0 + 4 * beta_1 + 0 * beta_2 = 8
#   1 * beta_0 + 6 * beta_1 + 0 * beta_2 = 9
#   1 * beta_0 + 0 * beta_1 + 2 * beta_2 = 2
#   1 * beta_0 + 0 * beta_1 + 4 * beta_2 = 5
#   1 * beta_0 + 0 * beta_1 + 6 * beta_2 = 7
#   1 * beta_0 + 0 * beta_1 + 8 * beta_2 = 6

#   [[1, 0, 0],                   [[1],
#    [1, 1, 0],                    [2],
#    [1, 2, 0],                    [4],
#    [1, 4, 0],    [[beta_0],      [8],
#    [1, 6, 0],     [beta_1],  =   [9],     
#    [1, 0, 2],     [beta_2]]      [2],
#    [1, 0, 4],                    [5],
#    [1, 0, 6],                    [7],
#    [1, 0, 8]]                    [6]]

sandwich_data  = Matrix(elements = [[1,0,0],[1,1,0],[1,2,0],[1,4,0],[1,6,0],[1,0,2],[1,0,4],[1,0,6],[1,0,8]])
sandwich_ratings = Matrix(elements = [[1],[2],[4],[8],[9],[2],[5],[7],[6]])

sandwich_regressor = PolynomialRegressor(2)
sandwich_regressor.solve_coefficients_with_inputs(sandwich_data, sandwich_ratings)

coeffs = sandwich_regressor.coefficients

print('Sandwich Rating Equation')
print('Rating = ',coeffs[0], '+',coeffs[1], '* (Slices of Beef) +', coeffs[2], '* (Tbsp of peanut butter)')
print('\n')
rating = sandwich_regressor.evaluate_with_inputs([1,5,5])
print('Predicted Rating With 5,5 of peanut butter and beef:')
print(rating)
print('\n')
rating = sandwich_regressor.evaluate_with_inputs([1,5,0])
print('Predicted Rating With 5 of beef:')
print(rating)
print('\n')
print('The company probably should not trust this because there are no')
print('samples with both beef and peanut butter which as a human')
print('I can say they probably do not taste good')
print('So these predictions may not be suer accurate')