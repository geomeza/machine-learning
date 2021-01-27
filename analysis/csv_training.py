import sys
sys.path.append('src')
from dataframe import DataFrame
from decision_tree import DecisionTree
from node import Node
from random_forest import RandomForest

path_to_datasets = 'C:/Users/mezag/Documents/Github/machine_learning/datasets/'
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
    decision_tree.fit(training_df)
    for test in testing_set:
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

dt_results = {}

dt_results['dt_gini'] =  round(total_correct/total,4)
print(total_correct, total, round(total_correct/total,4))

forests = [1,10,100,1000]

for num in forests:
    dt = RandomForest(num, depth = None)
    total_correct = 0
    total = 0
    for i in range(len(splits[0])):
        print(i+1,'testing set with', num, 'trees')
        results = run_tests(splits[0][i], splits[1][i], dt, True)
        total += results[1]
        total_correct += results[0]
    dict_key = 'random_dt_' + str(num)
    dt_results.update({dict_key :  round(total_correct/total,4)})
    print(total_correct, total, num, round(total_correct/total,4))

print(dt_results)


