import sys
sys.path.append('src')
from dataframe import DataFrame
from decision_tree import DecisionTree
from decision_tree import Node
from random_forest import RandomForest

path_to_datasets = '/home/runner/machine-learning/datasets/'
filename = 'freshman_lbs.csv' 
filepath = path_to_datasets + filename
df = DataFrame.from_csv(filepath)
df = df.filter_columns(['Sex', 'Weight (lbs, Sep)', 'BMI (Sep)'])
df = df.swap_columns(0,2)
df = df.rename_columns(['bmi', 'weight', 'class'])

df = df.apply('weight', lambda x: float(x))
df = df.apply('bmi', lambda x: float(x))
df.apply('class', lambda x: x.strip('"'))

def split_sets(data, num_sets):
    training_sets = []
    testing_sets = []
    interval = len(data)//num_sets
    for i in range(num_sets):
        training = []
        testing = []
        starter = i*interval
        cutoff = i*interval + interval
        for j in range(len(data)):
            if j > starter and j <= cutoff:
                testing.append(data[j])
            else:
                training.append(data[j])
        testing_sets.append(testing)
        training_sets.append(training)
    return training_sets, testing_sets


splits = split_sets(df.to_array(), 5)

def run_tests(training_set, testing_set, decision_tree, forest = False):
    correct = 0
    training_df = DataFrame.from_array(training_set, ['bmi', 'weight', 'class'])
    print('fitting')
    decision_tree.fit(training_df)
    print('fitted')
    for test in testing_set:
        print('new test')
        test_dict = {'bmi' : test[0], 'weight' : test[1]}
        if forest:
            prediction = decision_tree.predict(test_dict)
        else:
            prediction = decision_tree.classify(test_dict)
        if prediction == test[2]:
            correct += 1
    return correct,len(testing_set)

dt = DecisionTree('gini')
total_correct = 0
total = 0
for i in range(len(splits[0])):
    print(i+1,'testing set')
    results = run_tests(splits[0][i], splits[1][i], dt)
    total += results[1]
    total_correct += results[0]

print(total_correct, total)

