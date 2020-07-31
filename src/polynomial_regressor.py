from matrix import Matrix

class PolynomialRegressor:

    def __init__(self,degree):
        self.deg = degree
        self.coefficients = [0 for i in range(degree + 1)]
        self.data = None

    def ingest_data(self,data):
        self.data = data

    def evaluate(self, num):
        equation = []
        for i in range(len(self.coefficients)):
            equation.append((num**i) * self.coefficients[i])
        return sum(equation)

    def sum_squared_error(self):
        squared_errors = []
        for (x,y) in self.data:
            squared_errors.append((self.evaluate(x) - y)**2)
        return sum(squared_errors)

    def solve_coefficients (self):
        coeff = self.linear_approx(self.data, self.deg).elements
        self.coefficients = []
        for elem in coeff:
            for element in elem:
                self.coefficients.append(element)
        return self.coefficients
  
    def linear_approx(self,data, deg):
        X = Matrix(shape = (len(data),deg + 1))
        Y = Matrix(shape = (len(data),1))
        for i,(x,y) in enumerate(data):
            X.elements[i] = [x**i for i in range(deg + 1)]
            Y.elements[i] = [y]
        x_transpose = X.transpose()
        square = x_transpose.matrix_mult(X)
        inverse = square.inverse()
        matr  = x_transpose.matrix_mult(Y)
        return inverse.matrix_mult(matr)

    def approx_with_inputs(self, X, Y):
        x_transpose = X.transpose()
        square = x_transpose.matrix_mult(X)
        inverse = square.inverse()
        matr  = x_transpose.matrix_mult(Y)
        return inverse.matrix_mult(matr)

    def solve_coefficients_with_inputs(self, X, Y):
        coeff = self.approx_with_inputs(X, Y).elements
        self.coefficients = []
        for elem in coeff:
            for element in elem:
                self.coefficients.append(element)
        return self.coefficients

    def evaluate_with_inputs(self, input):
        evaluation = 0
        for i in range(len(self.coefficients)):
            evaluation += self.coefficients[i] * input[i]
        return evaluation

    def plot(self):
        Title = 'y = {} + {}x + {}x^2'.format(round(self.coeff[0],2), round(self.coeff[1],2), round(self.coeff[2],2))
        plot_approximation(self.evaluate, self.coeff[0], self.coeff[1], self.coeff[2], self.data, Title)
