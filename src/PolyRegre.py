import Matrix from Matrix.py

class PolynomialRegressor():

    def __init__(self,degree):
        self.deg = degree
        self.coeff = [0 for i in range(degree + 1)]
        self.data = None

    def ingest_data(self,data):
        self.data = data

    def evaluate(self, num):
        equation = []
        for i in range(len(self.coeff)):
            equation.append((num**i) * self.coeff[i])
        return sum(equation)

    def sum_squared_error(self):
        squared_errors = []
        for (x,y) in data:
            squared_errors.append((self.evaluate(x) - y)**2)
        return sum(squared_errors)

    def solve_coeff(self):
        m = Matrix(shape = (1,1))
        coeff = m.linear_approx(self.data, self.deg).elements
        self.coeff = []
        for elem in coeff:
            for element in elem:
                self.coeff.append(element)

    def plot(self):
        Title = 'y = {} + {}x + {}x^2'.format(round(self.coeff[0],2), round(self.coeff[1],2), round(self.coeff[2],2))
        plot_approximation(self.evaluate, self.coeff[0], self.coeff[1], self.coeff[2], self.data, Title)
