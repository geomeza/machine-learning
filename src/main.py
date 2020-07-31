from gradient_descent import gradient_descent
from matrix import matrix 
from polynomial_regressor import polynomial_regressor

def single_variable_function(x):
        return (x-1)**2
def two_variable_function(x, y):
        return (x-1)**2 + (y-1)**3
def three_variable_function(x, y, z):
        return (x-1)**2 + (y-1)**3 + (z-1)**4
def six_variable_function(x1, x2, x3, x4, x5, x6):
        return (x1-1)**2 + (x2-1)**3 + (x3-1)**4 + x4 + 2*x5 + 3*x6
 
minimizer = GradientDescent(single_variable_function)
print(minimizer.minim)
# (0)
print(minimizer.comp_gradient(delta=0.01))
# [-2.0000000000000018]
minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=1, logging=True)
# (0.0020000000000000018)
 
minimizer = GradientDescent(two_variable_function)
print(minimizer.minim)
# (0, 0)
print(minimizer.comp_gradient(delta=0.01))
# [-2.0000000000000018, 3.0001000000000055]
minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=1, logging=True)
# (0.0020000000000000018, -0.0030001000000000055)
 
minimizer = GradientDescent(three_variable_function)
print(minimizer.minim)
# (0, 0, 0)
print(minimizer.comp_gradient(delta=0.01))
# [-2.0000000000000018, 3.0001000000000055, -4.0004000000000035]
minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=1, logging=True)
(0.0020000000000000018, -0.0030001000000000055, 0.004000400000000004)
 
minimizer = GradientDescent(six_variable_function)
print(minimizer.minim)
# (0, 0, 0, 0, 0, 0)
print(minimizer.comp_gradient(delta=0.01))
# [-2.0000000000000018, 3.0001000000000055, -4.0004000000000035, 1.0000000000000009, 2.0000000000000018, 3.0000000000000027]
minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=1, logging=True)
# (0.0020000000000000018, -0.0030001000000000055, 0.004000400000000004, -0.0010000000000000009, -0.0020000000000000018, -0.0030000000000000027)