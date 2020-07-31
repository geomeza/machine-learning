class gradient_descent():

    def __init__(self, f):
        self.f = f
        self.num_vars = f.__code__.co_argcount
        self.minimum = [0 for i in range(self.num_vars)]

    def compute_gradient(self, delta = 0.01):
        gradient = []
        for i in range(len(self.minim)):
            forward_args = [0 for i in range(len(self.minimum))]
            backward_args = [0 for i in range(len(self.minimum))]
            for j in range(len(self.minimum)):
                forward_args[j] = self.minimum[j]
                backward_args[j] = self.minimum[j]
            forward_args[i] += delta
            backward_args[i] -= delta
            forward_comp = self.f(*forward_args)
            back_comp = self.f(*backward_args)
            gradient.append((forward_comp - back_comp)/(2 * delta))
        return gradient

    def cartesian_product(self,arrays):
        result = []
        temp = []
        for i in range(len(arrays)):
            temp = result
            result = []
            for j in arrays[i]:
                if i > 0:
                    for k in temp:
                        result.append(k + [j])
                else:
                    result.append([j])
        return result

    def grid_search(self,arrays):
        grid = self.cartesian_product(arrays)
        self.minimum = grid[0]
        for g in grid:
            if self.f(*g) < self.f(*self.minim):
                for i in range(len(g)):
                    self.minimum[i] = g[i]
        return self.minimum

    def descend(self, scaling_factor = 0.001, delta = 0.001, num_steps = 10, logging = False):
        for i in range(num_steps):
            grad = self.compute_gradient()
            for j in range(len(self.minimum)):
                self.minimum[j] -= scaling_factor * grad[j]
            if logging is True:
                print(self.minimum)
