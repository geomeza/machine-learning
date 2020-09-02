import sys
sys.path.append('src')
from matrix import Matrix
import matplotlib.pyplot as plt
import math
plt.style.use('bmh')

def approximation(data): ## CALCULATING PSUEDOINVERSE
    X_data = [[1,x] for x,y in data]
    Y_data = [[math.log((1/(y)) - 1)] for x,y in data]
    X = Matrix(elements = X_data)
    Y = Matrix(elements = Y_data)
    x_transpose = X.transpose()
    square = x_transpose.matrix_mult(X)
    inverse = square.inverse()
    matr  = x_transpose.matrix_mult(Y)
    return inverse.matrix_mult(matr)

def solve_coefficients(data):## Putting Coefficients in neat single array
    coeff = approximation(data).elements
    coefficients = []
    for elem in coeff:
        for element in elem:
            coefficients.append(element)
    return coefficients


## Win Rate DATA
data = [(0, 0.01), (0, 0.01), (0, 0.05), (10, 0.02), (10, 0.15), (50, 0.12), (50, 0.28), (73, 0.03), (80, 0.10), (115, 0.06), (150, 0.12), (170, 0.30), (175, 0.24), (198, 0.26), (212, 0.25), (232, 0.32), (240, 0.45), (381, 0.93), (390, 0.87), (402, 0.95), (450, 0.98), (450, 0.85), (450, 0.95), (460, 0.91), (500, 0.95)]

coefficients = solve_coefficients(data)

def win_probability(coefficients, hours_played):## Using Coefficients and hours_played input to calculate win rate 
    exponential = coefficients[0] + coefficients[1] * hours_played## with that amount of hours playes
    e_value = math.exp(exponential)
    return 1/(1 + e_value)

win_rate = round(win_probability(coefficients,300),3) ## rounding to three places
print('\nWin Probabilty Against AVG Player with 300 Hrs Played:')
print('\n', win_rate * 100, 'Percent') ## Multiplied by 100 so it's closer to a percentage

x_coords = [i for i in range(751)] ## All the x _coordinates for the plot
win_rates = [win_probability(coefficients, x) * 100 for x in x_coords] ## Calculating win rate with every x_coord(AKA Hours Played)
plt.plot(x_coords, win_rates, linewidth=2.5) ## Actually plotting the data calculated
plt.legend(['Win Rate Vs Avg Player']) ##  Labeling the grid with everything needed
plt.xlabel('Number of Hours Played')
plt.ylabel('Win Rate')
plt.title('Win Rate Against Players')
plt.savefig('wins.png')
plt.show() ## Showing the graph
