import sys
sys.path.append('src')
from gradient_descent import gradient_descent

def single_variable_function(x):
    return (x-1)**2
def two_variable_function(x, y):
    return (x-1)**2 + (y-1)**3
def three_variable_function(x, y, z):
   return (x-1)**2 + (y-1)**3 + (z-1)**4
def six_variable_function(x1, x2, x3, x4, x5, x6):
   return (x1-1)**2 + (x2-1)**3 + (x3-1)**4 + x4 + 2*x5 + 3*x6

functions = [single_variable_function,two_variable_function,three_variable_function,six_variable_function]
gradients = [[-2.0000000000000018],[-2.0000000000000018, 3.0001000000000055],[-2.0000000000000018, 3.0001000000000055, -4.0004000000000035],[-2.0000000000000018, 3.0001000000000055, -4.0004000000000035, 1.0000000000000009, 2.0000000000000018, 3.0000000000000027]]
minims = [[0.0020000000000000018],[0.0020000000000000018, -0.0030001000000000055],[0.0020000000000000018, -0.0030001000000000055, 0.004000400000000004],[0.0020000000000000018, -0.0030001000000000055, 0.004000400000000004, -0.0010000000000000009, -0.0020000000000000018, -0.0030000000000000027]]
grids = [[[0, 0.25, 0.75]], [[0, 0.25, 0.75], [0.9, 1, 1.1]],[[0, 0.25, 0.75], [0.9, 1, 1.1], [0, 1, 2, 3]], [[0, 0.25, 0.75], [0.9, 1, 1.1], [0, 1, 2, 3],[-2, -1, 0, 1, 2], [-2, -1, 0, 1, 2], [-2, -1, 0, 1, 2]]]
grid_minims = [[0.75],[0.75, 0.9], [0.75, 0.9, 1], [0.75, 0.9, 1, -2, -2, -2]]

for f in functions:
	indx = functions.index(f)
	print('Gradient and Minim Test',indx + 1)
	minimizer = gradient_descent(f)
	grad = minimizer.compute_gradient(delta = 0.01)
	minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=1)
	assert grad == gradients[indx],'wrong gradient'
	assert minimizer.minim == minims[indx],'wrong minim'
	print('passed')

for f in functions:
    indx = functions.index(f)
    print('Grid Search Test',indx + 1)
    minimizer = gradient_descent(f)
    minimizer.grid_search(grids[indx])
    assert minimizer.minim == grid_minims[indx],'wrong grid minim'
    print('passed')

