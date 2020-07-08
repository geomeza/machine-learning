import inspect

def f(x,y):
    return 1 + (x-1)**2 + (y+5)**2

class GradientDescent():
    
    def __init__(self, f):
        self.f = f
        self.num_vars = len(inspect.getfullargspec(self.f).args)
        self.minim = [0 for i in range(self.num_vars)]

    def comp_gradient(self, delta = 0.01):
        gradient = []
        for i in range(len(self.minim)):
            forward = [0 for i in range(len(self.minim))]
            backward = [0 for i in range(len(self.minim))]
            for j in range(len(self.minim)):
                forward[j] = self.minim[j]
                backward[j] = self.minim[j]
            forward[i] += delta
            backward[i] -= delta
            forward_comp = self.f(*forward)
            back_comp = self.f(*backward)
            gradient.append((forward_comp - back_comp)/(2 * delta))
        return gradient

    def descend(self, scaling_factor = 0.001, delta = 0.001, num_steps = 10, logging = True):
        for i in range(num_steps):
            grad = self.comp_gradient()
            for j in range(len(self.minim)):
                self.minim[j] -= scaling_factor * grad[j]
            if logging is True:
                print(self.minim)

    def grid_search(self, ranges):
        status = False
        output = [0 for i in range(len(ranges))]
        iterations = [0 for i in range(len(ranges))]
        while status is not True:
        #(-----------------------)
            all = 0
            for i in range(len(ranges)):
                if ranges[i] == iterations[i]:
                    all += 1
            if all == len(ranges):
                status = True
        #This is the check to see when the loop should be finished
        #(-----------------------)
            iterator = len(ranges) - 1
            change = True
            while change is True and iterator >= 0:
                if iterations[iterator] + 1 > ranges[iterator]:
                    iterations[iterator] = 0
                    output[iterator] = 0
                    change = True
                else:
                    iterations[iterator] += 1
                    output[iterator] += 1
                    change = False
                iterator -= 1
        if self.f(*output) < self.f(*minim):
            for i in range(len(output)):
                self.minim[i] = output[i]
        return self.minim

    def real_grid_search(self, ranges):
        status = False
        output = [ranges[i][0] for i in range(len(ranges))]
        iterations = [0 for i in range(len(ranges))]
        num_iterators = [len(elem) for elem in ranges]
        while status is not True:
        #(-----------------------)
            all = 0
            for i in range(len(ranges)):
                if num_iterators[i] == iterations[i]:
                    all += 1
            if all == len(ranges):
                status = True
        #This is the check to see when the loop should be finished
        #(-----------------------)
            if self.f(*output) < self.f(*self.minim):
                for i in range(len(output)):
                    self.minim[i] = output[i]
        #(-----------------------)
            iterator = len(ranges) - 1
            change = True
            while change is True and iterator >= 0:
                if iterations[iterator] + 1 > num_iterators[iterator]:
                    iterations[iterator] = 0
                    output[iterator] = ranges[iterator][0]
                    change = True
                else:
                    iterations[iterator] += 1
                    output[iterator] = ranges[iterator][iterations[iterator] - 1]
                    change = False
                iterator -= 1
        return self.minim
