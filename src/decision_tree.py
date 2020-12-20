from dataframe import DataFrame
from node import Node

class DecisionTree:

    def __init__(self):
        self.df = None
        self.root = None

    def split(self):
        self.root.split(if_once = True)
    
    def fit(self, df):
        self.initialize(df)
        self.root.split()

    def initialize(self, df):
        self.df = df
        self.df = self.df.append_columns({'indices': [i for i in range(len(df.to_array()))]})
        self.root = Node(self.df)

    def classify(self, point, node = None):
        if node is None:
            node = self.root
        else:
            node = node
        if node.impurity == 0:
            class_type = list(node.class_counts)[0]
            return class_type
        split_val = node.best_split[0]
        if point[split_val] < node.best_split[1]:
            return self.classify(point, node = node.low)
        if point[split_val] >= node.best_split[1]:
            return self.classify(point, node = node.high)