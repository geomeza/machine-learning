from dataframe import DataFrame
from node import Node

class DecisionTree:

    def __init__(self, split_metric, max_depth = None):
        self.df = None
        self.root = None
        self.split_metric = split_metric
        self.max_depth = max_depth
        self.splits = {'0': []}

    def split(self):
        self.root.split(if_once = True)
    
    def fit(self, df):
        self.initialize(df)
        self.root.split(depth_needed = self.max_depth)

    def initialize(self, df):
        self.df = df
        self.df = self.df.append_columns({'indices': [i for i in range(len(df.to_array()))]})
        self.root = Node(self.df, self.split_metric,depth = 0, check_splits = False, tree = self)

    def show_tree(self, current_node = None, iter = 0):
        if current_node is None and iter == 0:
            current_node = self.root
        if current_node.impurity == 0:
            return
        print(current_node.best_split)
        print(current_node.impurity)
        iter += 1
        self.show_tree(current_node.low, iter)
        self.show_tree(current_node.high, iter)

    def classify(self, point, node = None):
        if node is None:
            node = self.root
        else:
            node = node
        if node.impurity == 0:
            class_type = list(node.class_counts)[0]
            return class_type
        if node.best_split is not None and (self.max_depth is None or node.depth != self.max_depth):
            split_val = node.best_split[0]
            if point[split_val] < node.best_split[1]:
                return self.classify(point, node = node.low)
            if point[split_val] >= node.best_split[1]:
                return self.classify(point, node = node.high)
        else:
            class_types = list(node.class_counts.keys())
            class_counts = list(node.class_counts.values())
            return class_types[class_counts.index(max(class_counts))]
            