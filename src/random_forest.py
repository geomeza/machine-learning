from dataframe import DataFrame
from decision_tree import DecisionTree
import collections

class RandomForest:

    def __init__(self, num_trees):
        self.num_trees = num_trees
        self.trees = [DecisionTree('random') for i in range(num_trees)]

    def fit(self, df):
        for tree in self.trees:
            tree.fit(df)

    def predict(self, observation):
        classifications = []
        for tree in self.trees:
            prediction = tree.classify(observation)
            classifications.append(prediction)
        counted = collections.Counter(classifications)
        return list(counted.keys())[0]