import math, sys
sys.path.append('src')
from dataframe import DataFrame
from linear_regressor import LinearRegressor

def transform_data(data):
    trigonometry_dict = {str(i):[] for i in range(4)}
    trigonometry_dict.update({'y' : []})
    for x,y in data:
        adjusted_data = [math.ln(x), math.cos(x), math.sin(2*x), math.cos(2*x)]
        for i in range(len(adjusted_data)):
            trigonometry_dict[str(i)].append(adjusted_data[i])
        trigonometry_dict['y'].append(y)
    return trigonometry_dict


data = [(2, 27.0154), (3, 64.0912), (4, 159.817)]