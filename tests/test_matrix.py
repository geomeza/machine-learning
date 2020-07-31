import sys
sys.path.append('src')

from matrix import Matrix

def assertion(input = None,result = None):
    assert input == result,('\nError, Output:', input,'Did not Match Result:',result)
    print('\nPassed')

A = Matrix(elements = [[1,2,3,2,3],[2,4,6,4,5],[3,6,12,6,8]])
B = Matrix(elements = [[23,12,0,2,4],[34,0,3,4,5],[19,34,56,0,18]])
C = Matrix(elements = [[2,3,4],[1,4,7],[3,6,7],[1,4,7],[1,4,7]])
D = Matrix(elements = [[10,2,1],[5,1,7],[15,3,5]])
E = Matrix(elements = [[2,2,2],[4,4,4],[9,0,9]])
F = Matrix(elements = [[2,3,4,4],[1,4,7,4],[3,6,7,4],[1,4,7,4],[1,4,7,4]])

off_matrices = [A,B,C,D,E,F]

matr1 = Matrix(elements = [[1, 2, 3, 4], [5, 0, 6, 0], [0, 7, 0, 8], [9, 0, 0, 10]])
matr2 = Matrix(elements = [[1.2, 5.3, 8.9, -10.3, -15], [3.14, 0, -6.28, 0, 2.71], [0, 1, 1, 2, 3], [5, 8, 13, 21, 34], [1, 0,0.5, 0, 0.1]])
matr3 = Matrix(elements = [[7,22,13],[12,4,4],[0,8,8]])

inv_matrices = [matr1,matr2,matr3]

for i in range(len(inv_matrices)):
    matrix = inv_matrices[i]
    ID = Matrix(shape = (len(matrix.elements),len(matrix.elements[0])),fill = 'diag')
    print('-----------------------')
    print('\nInverse Test:',i+1)
    assertion(matrix.matrix_mult(matrix.inverse()).round(),ID)
    print('\nInverse By Minors Test:',i+1)
    assertion(matrix.matrix_mult(matrix.inverse_by_minors()).round(),ID)
    print('\nRREF Test:',i+1)
    assertion(matrix.rref().round(),result = ID)
    print('\nDeterminant Test & Recursive Det Test:',i+1)
    assertion(round(matrix.determinant(),6),round(matrix.recursive_det(),6))
    print('\n-----------------------')

for i in range(len(off_matrices)):
    print('-----------------------')
    matrix = off_matrices[i]
    print('\nOff Matrix RREF Test:', i+1)
    matrix.rref().round().show()
    print('\nOff Matrix Inverse Test:', i+1)
    assertion(matrix.inverse(), None)
    print('\n-----------------------')


# print('\nAddition Test:')
# A.add(B).show()

# print('\nSubtraction Test:')
# A.subtract(B).show()

# print('\nScale Test:')
# A.scale(2).show()

# print('\nMatrix Multiplication Test:')
# A.matrix_mult(B).show()

# print('\nTranspose Test:')
# B.transpose().show()

