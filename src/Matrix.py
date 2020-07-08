class Matrix:
    def __init__(self, elements=None, shape=None, fill=0):
        self.elements = elements
        self.shape = shape
        self.final_determinant = 1
        if shape is not None:
            self.elements = []
            for rows in range(shape[0]):
                self.elements.append(([0 for c in range(shape[1])]))
        if fill == "diag":
            for r in range(len(self.elements)):
                for c in range(len(self.elements[0])):
                    self.elements[r][r] = 1
        if fill == 1:
            for r in range(len(self.elements)):
                for c in range(len(self.elements[0])):
                    self.elements[r][c] = 1
        self.ID = None

    def show(self):
        for rows in range(len(self.elements)):
            print(self.elements[rows])

    def add(matr1, matr2):
        result = []
        if range(len(matr1.elements)) == range(len(matr2.elements)):
            for r in range(len(matr1.elements)):
                result.append([])
                for m in range(len(matr1.elements[0])):
                    result[r].append(0)

            for a in range(len(matr1.elements)):
                for b in range(len(matr2.elements[0])):
                    for c in range(len(matr2.elements)):
                        result[a][b] = matr1.elements[a][b] + matr2.elements[a][b]
            return Matrix(result)

    def sub(matr1, matr2):
        result = []
        if range(len(matr1.elements)) == range(len(matr2.elements)):
            for r in range(len(matr1.elements)):
                result.append([])
                for m in range(len(matr1.elements[0])):
                    result[r].append(0)

        for a in range(len(matr1.elements)):
            for b in range(len(matr2.elements[0])):
                for c in range(len(matr2.elements)):
                    result[a][b] = matr1.elements[a][b] - matr2.elements[a][b]
        return Matrix(result)

    def scale(self, scalar):
        result = []
        for r in range(len(self.elements)):
            result.append([])
            for m in range(len(self.elements[0])):
                result[r].append(0)

        for a in range(len(self.elements)):
            for b in range(len(self.elements[0])):
                result[a][b] = scalar*self.elements[a][b]
        return Matrix(result)

    def matmult(A,B):
        if range(len(A.elements[0])) == range(len(B.elements)):
            result = Matrix(shape = (len(A.elements), len(B.elements[0])))

        for i in range(len(A.elements)):
            for j in range(len(B.elements[0])):
                for k in range(len(B.elements)):
                    result.elements[i][j] += A.elements[i][k] * B.elements[k][j]
        return result

    def maximum(self):
        numInMatr = []
        for i in self.elements:
            for j in i:
                numInMatr.append(j)
        print(max(numInMatr))

    def minimum(self):
        numInMatr = []
        for i in self.elements:
            for j in i:
                numInMatr.append(j)
        print(min(numInMatr))

    def exponent(matr1, exponent):
        result = []
        for r in range(len(matr1.elements)):
            result.append([])
            for m in range(len(matr1.elements[0])):
                result[r].append(0)

        for a in range(len(matr1.elements)):
            for b in range(len(matr1.elements[0])):
                result[a][b] = matr1.elements[a][b]**exponent
        return Matrix(result)

    def transpose(self):
        result = Matrix(shape = (len(self.elements[0]),len(self.elements)))

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
        print(coords)
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
            if isinstance(coords[1], splice):
                self.elements[coords[0]] = val
        if isinstance(coords[0], splice):
            for r in range(len(self.elements[0])):
                self.elements[r][coords[1]] = val[r]

    def get_pivot_row(self, column):
        row_counter = 0
        for rows in range(len(self.elements)):
            zeros = 0
            if self.elements[rows][column] != 0:
                for col in range(len(self.elements[0])):
                    if self.elements[rows][col] == 0:
                        zeros += 1
                if zeros == column:
                    return rows
            else:
                row_counter += 1
        if(row_counter == len(self.elements)):
            return None

    def swap_rows(self, row1, row2,inv_matrix = False):
        self.final_determinant *= -1
        rowSwap = self.elements[row1]
        self.elements[row1] = self.elements[row2]
        self.elements[row2] = rowSwap
        if inv_matrix is True:
            row_swap = self.ID.elements[row1]
            self.ID.elements[row1] = self.ID.elements[row2]
            self.ID.elements[row2] = row_swap

    def scale_row(self, row_index,inv_matrix = False):
        new_matrix = self.copy()
        non_zero_entry = 0
        divide = 0
        row_lenth = 0
        for r in range(len(new_matrix.elements[0])):
            if new_matrix.elements[row_index][r] != 0 and divide == 0:
                non_zero_entry = new_matrix.elements[row_index][r]
                divide = 1
            if divide == 1:
                if inv_matrix is True:
                    self.ID.elements[row_index][r] = self.ID.elements[row_index][r] / non_zero_entry
                new_matrix.elements[row_index][r] = new_matrix.elements[row_index][r] / non_zero_entry
        self.final_determinant *= non_zero_entry

    def clear_below(self, row_index,inv_matrix = False):
        new_matrix = self
        clear_bottom = 0
        column = 0
        for c in range(len(new_matrix.elements[row_index])):
            if new_matrix.elements[row_index][c] != 0 and clear_bottom == 0:
                column = c
                clear_bottom = 1
        if clear_bottom == 1:
            for r in range(len(new_matrix.elements)):
                if r > row_index:
                    # if inv_matrix is True:
                    #     inv_divisor = 
                    divisor = new_matrix.elements[r][column] / new_matrix.elements[row_index][column]
                    for c in range(len(new_matrix.elements[0])):
                        if inv_matrix is True:
                            self.ID.elements[r][c] -= divisor*self.ID.elements[row_index][c]
                        new_matrix.elements[r][c] -= divisor*new_matrix.elements[row_index][c]
        return new_matrix.elements

    def clear_above(self, row_index, inv_matrix = False):
        new_matrix = self
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
                        if inv_matrix is True:
                            self.ID.elements[r][c] -= divisor*self.ID.elements[row_index][c]
                        new_matrix.elements[r][c] -= divisor*new_matrix.elements[row_index][c]
        return new_matrix.elements

    def rref(self, invert_matrix=False):
        new_matrix = self.copy()
        if invert_matrix is True:
            new_matrix.ID = Matrix(shape = (len(self.elements),len(self.elements[0])), fill = 'diag')
        column_big = 0
        for r in range(len(new_matrix.elements[0])):
            if r == len(new_matrix.elements):
                column_big = 1
                pass       
            if new_matrix.get_pivot_row(r) is None:
                pass
            elif(new_matrix.get_pivot_row(r) != r) and column_big != 1:
                # if invert_matrix is True:
                new_matrix.swap_rows(r,new_matrix.get_pivot_row(r),inv_matrix = invert_matrix)
                # if invert_matrix is False:
                #     new_matrix.swap_rows(r, new_matrix.get_pivot_row(r))
            if column_big == 0:
                new_matrix.scale_row(r, inv_matrix = invert_matrix)
                new_matrix.clear_above(r, inv_matrix = invert_matrix)
                new_matrix.clear_below(r, inv_matrix = invert_matrix)
        if invert_matrix is True:
            self.ID = new_matrix.ID
        return new_matrix

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
        copy = self.copy()
        if len(copy.elements) == 2 and len(copy.elements[0]) == 2:
            print((copy.elements[0][0] * copy.elements[1][1]) - (copy.elements[0][1] * copy.elements[1][0]))
        reducer = self.copy()
        reducer.rref()
        if len(copy.elements) == len(copy.elements[0]) and ID == reducer:
            copy.rref()
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
        result = Matrix(shape = ( len(self.elements), len(self.elements[0]) ) )
        for r in range(len(self.elements)):
            for m in range(len(self.elements[0])):
                result.elements[r][m] = self.elements[r][m]
        return result

    def inverse(self):
        copy = self.copy()
        copy.ID = Matrix(shape = (len(self.elements),len(self.elements[0])), fill = 'diag') 
        copy.rref(invert_matrix = True)
        return Matrix(copy.ID.elements)

    def inverse_by_minors(m):
        det = m.recursive_det()
        if len(m.elements) == 2 and len(m.elements[0]):
            return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                    [-1*m[1][0]/determinant, m[0][0]/determinant]]
        inverse = []
        for r in range(len(m.elements)):
            row = []
            for c in range(len(m.elements[0])):
                minor = m.minor(r,c)
                row.append(((-1)**(r+c)) * minor.recursive_det())
            inverse.append(row)
        inverse = Matrix(inverse)
        inverse = inverse.transpose()
        for r in range(len(inverse.elements)):
            for c in range(len(inverse.elements[0])):
                elem = inverse.elements[r][c]
                inverse.elements[r][c] = elem/det
        return inverse

    def linear_approx(self,data,deg):
        X = Matrix(shape = (len(data),deg + 1))
        Y = Matrix(shape = (len(data),1))
        for i,(x,y) in enumerate(data):
            X.elements[i] = [x**i for i in range(deg + 1)]
            Y.elements[i] = [y]
        x_transpose = X.transpose()
        inverse = x_transpose.matmult(X).inverse_by_minors()
        matr  = x_transpose.matmult(Y)
        return inverse.matmult(matr)


    def __add__(self, B):
        return self.add(B)

    def __sub__(self, B):
        return self.sub(B)

    def __mul__(self, B):
        return self.scale(B)

    def __matmul__(self, B):
        return self.matmult(B)

    def __eq__(self, other):
        return self.isEqual(other)

    def __getitem__(self, coords):
        return self.getItem(coords)

    def __setitem__(self, coords, val):
        return self.setItem(coords, val)