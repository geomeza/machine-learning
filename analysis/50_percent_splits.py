import sys
sys.path.append('src')
from dataframe import DataFrame
from decision_tree import DecisionTree
from node import Node
from random_forest import RandomForest
import math

# path_to_datasets = 'C:/Users/mezag/Documents/Github/machine_learning/datasets/'
path_to_datasets = './datasets/'
filename = 'freshman_lbs.csv' 
filepath = path_to_datasets + filename
df = DataFrame.from_csv(filepath)
df = df.filter_columns(['Sex', 'Weight (lbs, Sep)', 'BMI (Sep)'])
df = df.swap_columns(0,2)
df = df.swap_columns(0,1)
df = df.rename_columns(['weight', 'bmi', 'class'])

df = df.apply('weight', lambda x: float(x))
df = df.apply('bmi', lambda x: float(x))
df.apply('class', lambda x: x.strip('"'))

# def split_sets(data, num_sets):
#     training_sets = []
#     testing_sets = []
#     interval = math.ceil(len(data)/num_sets)
#     for i in range(num_sets):
#         training = []
#         testing = []
#         starter = i*interval
#         cutoff = i*interval + interval
#         for j in range(len(data)):
#             if j > starter and j <= cutoff:
#                 testing.append(data[j])
#             else:
#                 training.append(data[j])
#         testing_sets.append(testing)
#         training_sets.append(training)
#     return training_sets,testing_sets

def split_in_two(data):
    first_half = []
    second_half = []
    split_num = math.ceil(len(data)/2)
    for i in range(len(data)):
        if i < split_num:
            first_half.append(data[i])
        else:
            second_half.append(data[i])
    return first_half, second_half


# splits = split_sets(df.to_array(), 2)
splits = split_in_two(df.to_array())
indices = []
def run_tests(training_set, testing_set, decision_tree, forest = False):
    correct = 0
    training_df = DataFrame.from_array(training_set, ['bmi', 'weight', 'class'])
    decision_tree.fit(training_df)
    for test in testing_set:
        test_dict = {'bmi' : test[0], 'weight' : test[1]}
        if forest:
            prediction = decision_tree.predict(test_dict)
        else:
            prediction = decision_tree.classify(test_dict)
        if prediction == test[2]:
            correct += 1
        else:
            indices.append(df.to_array().index(test))
    return correct,len(testing_set)

dt = DecisionTree('gini', max_depth =4)

total_correct = 0
total = 0
# for i in range(len(splits[0])):
#     if i == 0:
# print(len(splits[1][i]))
# print(i+1,'testing set')
print('HALFWAY TRAINING SET')
results = run_tests(splits[0], splits[1], dt)
total += results[1]
total_correct += results[0]

dt_results = {}

dt_results['dt_gini'] =  round(total_correct/total,4)
print(total_correct, total, round(total_correct/total,4),  indices)

# print(dt.splits)


# print(dt_results)


# forests = [1,10,100,1000]

# for num in forests:
#     dt = RandomForest(num, depth = None)
#     total_correct = 0
#     total = 0
#     for i in range(len(splits[0])):
#         print(i+1,'testing set with', num, 'trees')
#         results = run_tests(splits[0][i], splits[1][i], dt, True)
#         total += results[1]
#         total_correct += results[0]
#     dict_key = 'random_dt_' + str(num)
#     dt_results.update({dict_key :  round(total_correct/total,4)})
#     print(total_correct, total, num, round(total_correct/total,4))