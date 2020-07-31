import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor
from matrix import Matrix

sandwich_data  = Matrix(elements = [[1,0,0],[1,1,0],[1,2,0],[1,4,0],[1,6,0],[1,0,2],[1,0,4],[1,0,6],[1,0,8],[1,2,2],[1,3,4]])
sandwich_ratings = Matrix(elements = [[1],[2],[4],[8],[9],[2],[5],[7],[6],[0],[0]])

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
print('The company probably should still not trust this because')
print('while previously it was a rating of 12.5 and now its 8')
print('I can say sandwiches with both still probably do not taste good')
print('and that is a really high rating, the test samples that came in rated any combinations')
print('of beef and peanut butter to be zero but the algorithm still came up with high score')
print('so this probably still can not be trusted')


sandwich_data  = Matrix(elements = [[1,0,0,0],[1,1,0,0],[1,2,0,0],[1,4,0,0],[1,6,0,0],[1,0,2,0],[1,0,4,0],[1,0,6,0],[1,0,8,0],[1,2,2,4],[1,3,4,12]])
sandwich_ratings = Matrix(elements = [[1],[2],[4],[8],[9],[2],[5],[7],[6],[0],[0]])

sandwich_regressor = PolynomialRegressor(2)
sandwich_regressor.solve_coefficients_with_inputs(sandwich_data, sandwich_ratings)

coeffs = sandwich_regressor.coefficients
# QUESTION 4
# Fill out the table with the additional interaction term:
 
# (slices beef) | (tbsp peanut butter) | (slices beef)(tbsp peanut butter) | Rating |
# -----------------------------------------------------------------------------------
#       0       |           0          |                 0                 |    1   |
#       1       |           0          |                 0                 |    2   |
#       2       |           0          |                 0                 |    4   |
#       4       |           0          |                 0                 |    8   |
#       6       |           0          |                 0                 |    9   |
#       0       |           2          |                 0                 |    2   |
#       0       |           4          |                 0                 |    5   |
#       0       |           6          |                 0                 |    7   |
#       0       |           8          |                 0                 |    6   |
#       2       |           2          |                 4                 |    0   | 
#       3       |           4          |                 12                |    0   |

# QUESTION 5
# What is the system of equations?
 
#   (1 * beta_0) + (0 * beta_1) + (0 * beta_2) + (0 * beta_3) = 1
#   (1 * beta_0) + (1 * beta_1) + (0 * beta_2) + (0 * beta_3) = 2
#   (1 * beta_0) + (2 * beta_1) + (0 * beta_2) + (0 * beta_3) = 4
#   (1 * beta_0) + (4 * beta_1) + (0 * beta_2) + (0 * beta_3) = 8
#   (1 * beta_0) + (6 * beta_1) + (0 * beta_2) + (0 * beta_3) = 9
#   (1 * beta_0) + (0 * beta_1) + (2 * beta_2) + (0 * beta_3) = 2
#   (1 * beta_0) + (0 * beta_1) + (4 * beta_2) + (0 * beta_3) = 5
#   (1 * beta_0) + (0 * beta_1) + (6 * beta_2) + (0 * beta_3) = 7
#   (1 * beta_0) + (0 * beta_1) + (8 * beta_2) + (0 * beta_3) = 6
#   (1 * beta_0) + (2 * beta_1) + (2 * beta_2) + (4 * beta_3) = 0
#   (1 * beta_0) + (3 * beta_1) + (4 * beta_2) + (12 * beta_3) = 0

# QUESTION 6
# What is the matrix equation?
 
#   [[1, 0, 0, 0],                   [[1],
#    [1, 1, 0, 0],                    [2],
#    [1, 2, 0, 0],                    [4],
#    [1, 4, 0, 0],    [[beta_0],      [8],
#    [1, 6, 0, 0],     [beta_1],  =   [9],     
#    [1, 0, 2, 0],     [beta_2],      [2],
#    [1, 0, 4, 0],     [beta_3]]      [5],
#    [1, 0, 6, 0],                    [7],
#    [1, 0, 8, 0],                    [6],
#    [1, 2, 2, 4],                    [0],
#    [1, 3, 4, 12],                   [0]]

# QUESTION 7
# What is the model?

print('\nSandwich Rating Equation With Interactive')
print('Rating = ',coeffs[0], '+',coeffs[1], '* (Slices of Beef) +', coeffs[2], '* (Tbsp of peanut butter) +',coeffs[3],'* (Slices of Beef)(Tbsp of peanut butter)')

# QUESTION 8
# What is the predicted rating of a sandwich with 5 slices of roast beef AND 
# 5 tablespoons of peanut butter (on the same sandwich)?

print('\n')
rating = sandwich_regressor.evaluate_with_inputs([1,5,5,25])
print('Predicted Rating With 5,5 of peanut butter and beef using interactive:')
print(rating)

# QUESTION 9
# How does this prediction compare to that from the previous assignment? Did 
# including interaction term make the prediction trustworthy? Why or why not?

print('\n')
print('For starters, this prediction is negative and it is way worse than the')
print('previous ratings of 12 and 8. Including the')
print('interactive I would say  made it pretty trustworthy.')
print('As extreme as a negative rating for a sandwich is,')
print('A sandwich with 5 slices of roast beef and 5 tbsp of peanut butter')
print('would probably be pretty bad so yes this is probably trustworthy')
