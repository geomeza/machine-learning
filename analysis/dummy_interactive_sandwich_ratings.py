import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor
from matrix import Matrix

# B = slices roast beef
# P = tbsp peanut butter
# M = mayo
# J = jelly
# R = rating
 
#    B  P  M  J  R
# [[ 0, 0, 0, 0, 1 ],   1
#  [ 0, 0, 1, 0, 1 ],   2  
#  [ 0, 0, 0, 1, 4 ],   3
#  [ 0, 0, 1, 1, 0 ],   4
#  [ 5, 0, 0, 0, 4 ],   5
#  [ 5, 0, 1, 0, 8 ],   6
#  [ 5, 0, 0, 1, 1 ],   7
#  [ 5, 0, 1, 1, 0 ],   8
#  [ 0, 5, 0, 0, 5 ],   9
#  [ 0, 5, 1, 0, 0 ],   10
#  [ 0, 5, 0, 1, 9 ],   11
#  [ 0, 5, 1, 1, 0 ],   12
#  [ 5, 5, 0, 0, 0 ],   13
#  [ 5, 5, 1, 0, 0 ],   14
#  [ 5, 5, 0, 1, 0 ],   15
#  [ 5, 5, 1, 1, 0 ]]   16

#    B  P  M  J  BP  BM  BJ  PM  PJ  MJ  R
complete_sandwich_data = Matrix(elements = [[ 0, 0, 0, 0,  0,  0,  0,  0,  0,  0, 1 ],\
 [ 0, 0, 1, 0,  0,  0,  0,  0,  0,  0, 1 ],\
 [ 0, 0, 0, 1,  0,  0,  0,  0,  0,  0, 4 ],\
 [ 0, 0, 1, 1,  0,  0,  0,  0,  0,  1, 0 ],\
 [ 5, 0, 0, 0,  0,  0,  0,  0,  0,  0, 4 ],\
 [ 5, 0, 1, 0,  0,  5,  0,  0,  0,  0, 8 ],\
 [ 5, 0, 0, 1,  0,  0,  5,  0,  0,  0, 1 ],\
 [ 5, 0, 1, 1,  0,  5,  5,  0,  0,  1, 0 ],\
 [ 0, 5, 0, 0,  0,  0,  0,  0,  0,  0, 5 ],\
 [ 0, 5, 1, 0,  0,  0,  0,  5,  0,  0, 0 ],\
 [ 0, 5, 0, 1,  0,  0,  0,  0,  5,  0, 9 ],\
 [ 0, 5, 1, 1,  0,  0,  0,  5,  5,  1, 0 ],\
 [ 5, 5, 0, 0, 25,  0,  0,  0,  0,  0, 0 ],\
 [ 5, 5, 1, 0, 25,  5,  0,  5,  0,  0, 0 ],\
 [ 5, 5, 0, 1, 25,  0,  5,  0,  5,  0, 0 ],\
 [ 5, 5, 1, 1, 25,  5,  5,  5,  5,  1, 0 ]])


total = 0
for row in complete_sandwich_data.elements:
    for column in row:
        total += column
assert total == 313, 'Wrong inputs for sanwich data'

sandwich_data = Matrix(elements = [[1, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0],\
 [1, 0, 0, 1, 0,  0,  0,  0,  0,  0,  0],\
 [1, 0, 0, 0, 1,  0,  0,  0,  0,  0,  0],\
 [1, 0, 0, 1, 1,  0,  0,  0,  0,  0,  1],\
 [1, 5, 0, 0, 0,  0,  0,  0,  0,  0,  0],\
 [1, 5, 0, 1, 0,  0,  5,  0,  0,  0,  0],\
 [1, 5, 0, 0, 1,  0,  0,  5,  0,  0,  0],\
 [1, 5, 0, 1, 1,  0,  5,  5,  0,  0,  1],\
 [1, 0, 5, 0, 0,  0,  0,  0,  0,  0,  0],\
 [1, 0, 5, 1, 0,  0,  0,  0,  5,  0,  0],\
 [1, 0, 5, 0, 1,  0,  0,  0,  0,  5,  0],\
 [1, 0, 5, 1, 1,  0,  0,  0,  5,  5,  1],\
 [1, 5, 5, 0, 0, 25,  0,  0,  0,  0,  0],\
 [1, 5, 5, 1, 0, 25,  5,  0,  5,  0,  0],\
 [1, 5, 5, 0, 1, 25,  0,  5,  0,  5,  0],\
 [1, 5, 5, 1, 1, 25,  5,  5,  5,  5,  1]])

sandwich_ratings = Matrix(elements = [[1], [1], [4], [0], [4], [8], [1], [0], [5], [0], [9], [0],[0], [0], [0], [0]])

sandwich_regressor = PolynomialRegressor(10)
sandwich_regressor.solve_coefficients_with_inputs(sandwich_data, sandwich_ratings)

coeffs = sandwich_regressor.coefficients

terms = ['Bias Term', 'Beef Slices', 'Peanut Butter', 'Mayo', 'Jelly', 'Beef & PB', 'Beef & Mayo', 'Beef & Jelly',\
'PB & Mayo', 'PB & Jelly', 'Mayo & Jelly']

print('\nSandwich Rating Equation')
equation_str = 'Rating ='
coeffs = [round(coeffs[i], 5) for i in range(len(coeffs))]
for i in range(len(coeffs)):
    equation_str += ' '
    if i > 0:
        equation_str += '+ '
    equation_str += str(coeffs[i])
    equation_str += ' * '
    equation_str += '('
    equation_str += terms[i]
    equation_str += ')'
print('\n',equation_str)

for i in range(len(coeffs)):
    print('\n',terms[i], ': ', coeffs[i])

predictions_info = [[1,2,0,1,0,0,2,0,0,0,0], [1,2,0,0,1,0,0,2,0,0,0], [1,0,3,0,1,0,0,0,0,3,0], [1,0,3,1,1,0,0,0,3,3,1],\
[1,2,3,1,1,6,2,2,3,3,1]]
predictions_elems = ['2 Beef & Mayo:', '2 Beef & Jelly', '3 PB & Jelly', '3 PB & Jelly & Mayo', '2 Beef & 3 PB & Jelly & Mayo']

for i in range(len(predictions_elems)):
    print('-------------')
    print('\nRating Prediction:')
    print('\n',predictions_elems[i])
    print('\n',sandwich_regressor.evaluate_with_inputs(predictions_info[i]))
    print('\n')
    print('-------------')