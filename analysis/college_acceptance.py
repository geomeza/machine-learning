import math, sys
sys.path.append('src')
from dataframe import DataFrame
from logistic_regressor import LogisticRegressor



students_dict = {'ACT':[33, 34, 35, 30, 36, 29, 36, 31, 36, 32],
'extra': [1, 0, 1, 1, 1, 1, 1, 1, 0, 0], 'Bias':[1,1,1,1,1,1,1,1,1,1]
}

students_dict.update({'interaction': [students_dict['ACT'][i] * students_dict['extra'][i] for i in range(len(students_dict['ACT']))]})

students_dict.update({'accepted': [0.95, 0.001, 0.95, 0.001, 0.95, 0.001, 0.95, 0.001, 0.95, 0.001]})

df = DataFrame(students_dict)

regressor = LogisticRegressor(df, 'accepted', 0.999)

# predictor = {'ACT': 36, 'extra': 0}

# df_bruh = DataFrame(predictor)
# print(df_bruh.gather_all_inputs())
# print(regressor.predict(predictor))
print(regressor.multipliers)