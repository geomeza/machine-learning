class Matrix:
    def __init__(self, elements=None, shape=None, fill=0):
        self.elements = elements
        self.shape = shape
        self.final_determinant = 1
        if self.elements is not None:
            self.shape = (len(elements), len(elements[0]))
        if shape is not None:
            self.elements = []
            for rows in range(shape[0]):
                self.elements.append(([0 for c in range(shape[1])]))
        if fill == "diag":
            for r in range(len(self.elements)):
                for c in range(len(self.elements[0])):
                    if r <= c:
                        self.elements[r][r] = 1
        if fill == 1:
            for r in range(len(self.elements)):
                for c in range(len(self.elements[0])):
                    self.elements[r][c] = 1

    def show(self):
        for rows in range(len(self.elements)):
            print(self.elements[rows])

    def add(self, other):
        result = Matrix(shape=(len(self.elements), len(self.elements[0])))
        if self.shape == other.shape:
            for i in range(len(self.elements)):
                for j in range(len(self.elements[1])):
                    result.elements[i][j] = self.elements[i][j] + other.elements[i][j]
        else:
            print('Matrices are not same size')
            return None
        return result

    def subtract(self, other):
        result = Matrix(shape=self.shape)
        if self.shape == other.shape:
            for i in range(len(self.elements)):
                for j in range(len(self.elements[0])):
                    result.elements[i][j] = self.elements[i][j] - other.elements[i][j]
        else:
            print('Matrices are not same size')
            return None
        return result

    def scale(self, scalar):
        result = Matrix(shape=self.shape)
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                result.elements[i][j] = scalar*self.elements[i][j]
        return result

    def matrix_mult(self, other):
        if len(self.elements[0]) == len(other.elements):
            result = Matrix(shape=(len(self.elements), len(other.elements[0])))
        else:
            print('Matrices are not compatible')
            return None

        for i in range(len(self.elements)):
            for j in range(len(other.elements[0])):
                for k in range(len(other.elements)):
                    result.elements[i][j] += self.elements[i][k] * other.elements[k][j]
        return result

    def maximum(self):
        numInMatr = [j for i in self.elements for j in i]
        return max(numInMatr)

    def minimum(self):
        numInMatr = [j for i in self.elements for j in i]
        return min(numInMatr)

    def exponent(self, exponent):
        result = self.copy()
        for i in range(exponent - 1):
            result = result.matrix_mult(self)
        return result

    def transpose(self):
        result = Matrix(shape=(len(self.elements[0]), len(self.elements)))
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                result.elements[j][i] = self.elements[i][j]
        return result

    def isEqual(self, other):
        elems = len(self.elements) * len(self.elements[0])
        equals = 0
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                if self.elements[i][j] == other.elements[i][j]:
                    equals += 1
        if equals == elems:
            return True
        else:
            return False

    def getItem(self, coords):
        if isinstance(coords[0], int):
            if isinstance(coords[1], int):
                return self.elements[coords[0]][coords[1]]
            else:
                return self.elements[coords[0]]
        else:
            column = []
            for i in range(len(self.elements)):
                column.append(self.elements[i][coords[1]])
            return column

    def setItem(self, coords, val):
        if isinstance(coords[0], int):
            if isinstance(coords[1], int):
                self.elements[coords[0]][coords[1]] = val
            else:
                self.elements[coords[0]] = val
        else:
            for r in range(len(self.elements[0])):
                self.elements[r][coords[1]] = val[r]

    def get_pivot_row(self, column):
        for i in range(len(self.elements)):
            zeros = 0
            if self.elements[i][column] != 0:
                for j in range(len(self.elements[0])):
                    if j > column:
                        break
                    if self.elements[i][j] == 0:
                        zeros += 1
                if zeros == column:
                    return i
        return None

    def swap_rows(self, row1, row2):
        result = self.copy()
        self.final_determinant *= -1
        result.final_determinant *= -1
        rowSwap = result.elements[row1]
        result.elements[row1] = result.elements[row2]
        result.elements[row2] = rowSwap
        return result

    def scale_row(self, row_index):
        new_matrix = self.copy()
        non_zero_entry = 0
        divide = 0
        row_lenth = 0
        bruh = 0
        for r in range(len(new_matrix.elements[0])):
            if new_matrix.elements[row_index][r] != 0 and divide == 0:
                non_zero_entry = new_matrix.elements[row_index][r]
                divide = 1
            if divide == 1:
                new_matrix.elements[row_index][r] = new_matrix.elements[row_index][r] / non_zero_entry
        self.final_determinant *= non_zero_entry
        new_matrix.final_determinant *= non_zero_entry
        return new_matrix

    def clear_below(self, row_index):
        new_matrix = self.copy()
        clear_bottom = 0
        column = 0
        for c in range(len(new_matrix.elements[row_index])):
            if new_matrix.elements[row_index][c] != 0 and clear_bottom == 0:
                column = c
                clear_bottom = 1
        if clear_bottom == 1:
            for r in range(len(new_matrix.elements)):
                if r > row_index:
                    divisor = new_matrix.elements[r][column] / new_matrix.elements[row_index][column]
                    for c in range(len(new_matrix.elements[0])):
                        new_matrix.elements[r][c] -= divisor*new_matrix.elements[row_index][c]
        return new_matrix

    def clear_above(self, row_index):
        new_matrix = self.copy()
        clear_above = 0
        column = 0
        for c in range(len(new_matrix.elements[row_index])):
            if new_matrix.elements[row_index][c] != 0 and clear_above == 0:
                column = c
                clear_above = 1
        if clear_above == 1:
            for r in range(len(new_matrix.elements)):
                if r < row_index:
                    divisor = new_matrix.elements[r][column] / new_matrix.elements[row_index][column]
                    for c in range(len(new_matrix.elements[0])):
                        new_matrix.elements[r][c] -= divisor*new_matrix.elements[row_index][c]
        return new_matrix

    def rref(self):
        new_matr = self.copy()
        column_big = 0
        for r in range(len(self.elements[0])):
            if r == len(self.elements):
                break
            pivot = new_matr.get_pivot_row(r)
            if pivot is None:
                pass
            elif pivot != r:
                new_matr = new_matr.swap_rows(pivot, r)
            new_matr = new_matr.scale_row(r)
            new_matr = new_matr.clear_above(r)
            new_matr = new_matr.clear_below(r)
        self.final_determinant = new_matr.final_determinant
        return new_matr

    def solve(self, column):
        for i in range(len(column)):
            self.elements[i].append(column[i])
        self.rref()
        solved = []
        for i in range(len(column)):
            solved.append(self.elements[i][len(self.elements[i]) - 1])
        return solved

    def determinant(self):
        ID = Matrix(shape=(len(self.elements), len(self.elements[0])), fill='diag')
        if self.shape == (2, 2):
            det = (self.elements[0][0] * self.elements[1][1]) - (self.elements[0][1] * self.elements[1][0])
            return det
        reducer = self.copy()
        reduced = reducer.rref()
        boolean = ID.isEqual(reduced)
        copy = self.copy()
        copy.final_determinant = 1
        if len(copy.elements) == len(copy.elements[0]) and boolean is True:
            copy = copy.rref()
            return copy.final_determinant
        else:
            print('No determinant')

    def minor(self, row, col):
        minor_matr = []
        for r in range(len(self.elements) - 1):
            minor_matr.append([])
            for c in range(len(self.elements) - 1):
                minor_matr[r].append(0)
        for r in range(len(self.elements)):
            if r == row:
                pass
            else:
                for c in range(len(self.elements[0])):
                    if c == col:
                        pass
                    else:
                        if r > row:
                            if c > col:
                                minor_matr[r-1][c-1] = self.elements[r][c]
                            else:
                                minor_matr[r-1][c] = self.elements[r][c]
                        else:
                            if c > col:
                                minor_matr[r][c-1] = self.elements[r][c]
                            else:
                                minor_matr[r][c] = self.elements[r][c]
        minor_matr = Matrix(elements=minor_matr)
        return minor_matr

    def recursive_det(self):
        n = len(self.elements)
        row = 0
        det = 0
        if n == len(self.elements[0]):
            if n == 1:
                return self.elements[0][0]
            for col in range(n):
                A = self.minor(row, col)
                det += ((-1)**(row+col))*(self.elements[row][col])*(A.recursive_det())
            return det
        else:
            print('No determinant')

    def copy(self):
        result = Matrix(shape=(len(self.elements), len(self.elements[0])))
        for r in range(result.shape[0]):
            for c in range(result.shape[1]):
                result.elements[r][c] = self.elements[r][c]
        result.final_determinant = self.final_determinant
        return result

    def inverse(self):
        copy = self.copy()
        reducer = self.copy()
        reducer = reducer.rref()
        if len(self.elements) == len(self.elements[0]):
            inv = Matrix(shape=self.shape, fill='diag')
            if reducer.isEqual(inv):
                for i in range(len(self.elements)):
                    for j in range(len(self.elements[0])):
                        copy.elements[i].append(inv.elements[i][j])
                copy = copy.rref()
                for i in range(len(self.elements)):
                    for j in range(len(self.elements[0]), len(copy.elements[0])):
                        inv.elements[i][j - len(self.elements)] = copy.elements[i][j]
                return inv
            else:
                print('Not Invertible')
                return None
        else:
            print('Not Invertible')
            return None

    def inverse_by_minors(m):
        det = m.recursive_det()
        if len(m.elements) == 2 and len(m.elements[0]) == 2:
            determinant = ((m.elements[0][0]*m.elements[1][1]) - (m.elements[0][1]*m.elements[1][0]))
            return Matrix(elements=[[m.elements[1][1]/determinant, -1*m.elements[0][1]/determinant], [-1*m.elements[1][0]/determinant, m.elements[0][0]/determinant]])
        if len(m.elements[0]) == len(m.elements):
            inverse = []
            for r in range(len(m.elements)):
                row = []
                for c in range(len(m.elements[0])):
                    minor = m.minor(r, c)
                    row.append(((-1)**(r+c)) * minor.recursive_det())
                inverse.append(row)
            inverse = Matrix(inverse)
            inverse = inverse.transpose()
            for r in range(len(inverse.elements)):
                for c in range(len(inverse.elements[0])):
                    elem = inverse.elements[r][c]
                    inverse.elements[r][c] = elem/det
            return inverse
        else:
            print('No inverse')
            return None

    def round(self):
        copy = self.copy()
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                copy.elements[i][j] = round(self.elements[i][j], 6)
        return copy

    def __add__(self, B):
        return self.add(B)

    def __sub__(self, B):
        return self.subtract(B)

    def __mul__(self, B):
        return self.scale(B)

    def __matmul__(self, B):
        return self.matrix_mult(B)

    def __eq__(self, other):
        return self.isEqual(other)

    def __getitem__(self, coords):
        return self.getItem(coords)

    def __setitem__(self, coords, val):
        return self.setItem(coords, val)
