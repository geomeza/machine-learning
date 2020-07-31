from matrix import Matrix

##TESTING GROUNDS FOR EXPERIMENTAL CODE

def assertion(function,input,result):
    assert function(input).round() == result,('\nError, Output:',function(input),'Did not Match Result:',result)
    print('\nPassed')
bruh = Matrix(elements = [[6,2],[3,2]])
breh = Matrix(elements = [[3,2],[5,6]])

bruh = Matrix(elements = [[3,7,11],[28,31,12],[11,11,43]])
tester = Matrix(elements = [[3,0,0],[0,3,0],[0,0,3]])
new_bruh = Matrix(elements = [[7,22,13],[12,4,4],[0,8,8]])

ID = Matrix(shape = (3,3),fill = 'diag')
matrices = [bruh,tester,new_bruh]

for i in range(len(matrices)):
    print('\nInverse Test:',i+1)
    matrix = matrices[i]
    assertion(matrix.matrix_mult,matrix.inverse(),ID)
    print('\nInverse By Minors Test:',i+1)
    matrix = matrices[i]
    assertion(matrix.matrix_mult,matrix.inverse_by_minors(),ID)






