import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor
from matrix import Matrix
data = [(0,1), (1,2), (2,5), (3,10), (4,20), (5,30)]
coefficients = [[11.333333333333332], [-3.2380952380952412, 5.828571428571428], [1.107142857142763, -0.6892857142856474, 1.3035714285714226], [1.1349206349217873, -0.8161375661377197, 1.3730158730155861, -0.009259259259233155], [0.9999999917480108, -2.950000002085698, 6.9583333345161265, -3.9583333337779045, 1.0416666667658463, -0.09166666667401097]]

evals = [11.333333333333332,8.419047619047616,4.942857142857159,4.920634920634827,4.999999990103076]

for x in range(len(coefficients)):
    print('Polynomial Test:',x+1)
    if x == 4:
        constant_regressor = PolynomialRegressor(degree=5)
    else:
        constant_regressor = PolynomialRegressor(degree=x)
    constant_regressor.ingest_data(data)
    coeffs = constant_regressor.solve_coefficients()
    test_coeffs = [round(coeff, 6) for coeff in coeffs]
    real_coeffs = [round(coeff, 6) for coeff in coefficients[x]]
    assert test_coeffs == real_coeffs, ('Not Right coefficients got',test_coeffs,'should be',real_coeffs)
    constant_regressor.coefficients
    eval = round(constant_regressor.evaluate(2),6)
    real_eval = round(evals[x],6)
    assert eval == real_eval, ('Not right evaluation, got',eval,'should be',real_eval)
    print('passed')