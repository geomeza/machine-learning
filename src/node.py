import random
from dataframe import DataFrame

class Node:

    def __init__(self, df, split_metric, depth, check_splits = True):
        self.depth = depth
        self.df = df
        self.val = None
        self.low = None
        self.high = None
        self.row_indices = self.df.data_dict['indices']
        self.class_counts = self.count_classes()
        self.impurity = self.get_impurity()
        self.distinct_values = self.get_distinct_values()
        self.split_metric = split_metric
        self.final_split = False
        if self.impurity != 0 and check_splits:
            self.possible_splits = self.get_possible_splits()
            self.get_best_split()
        if self.impurity == 0:
            self.final_split = True
        

    def count_classes(self):
        unique = []
        for class_type in self.df.data_dict['class']:
            if class_type not in unique:
                unique.append(class_type)
        self.classes = unique
        counted = {class_type: self.df.data_dict['class'].count(class_type) for class_type in unique}
        return counted

    def get_impurity(self):
        node_classes = self.df.data_dict['class']
        return sum([(self.class_counts[class_type]/len(node_classes)) * (1 - (self.class_counts[class_type]/len(node_classes)) ) for class_type in self.class_counts.keys()])

    def get_distinct_values(self):
        distinct = [[] for axis in self.df.columns if axis != 'class' and axis != 'indices']
        for axis in self.df.columns:
            if axis != 'class' and axis != 'indices':
                for value in self.df.data_dict[axis]:
                    if value not in distinct[self.df.columns.index(axis)]:
                        distinct[self.df.columns.index(axis)].append(value)
        return distinct

    def get_possible_splits(self):
        axis = [axis for axis in self.df.columns if axis != 'class' and axis != 'indices']
        all_splits = []
        for i in range(len(self.distinct_values)):
            for j in range(len(self.distinct_values[i]) - 1):
                split_value = (self.distinct_values[i][j] + self.distinct_values[i][j+1])/2
                all_splits.append([axis[i],split_value, self.calc_goodness(split_value, i)])
        if self.split_metric == 'random':
            if len(list(set([split[0] for split in all_splits]))) == 0:
                return []
            random_choice = random.choice(list(set([split[0] for split in all_splits])))
            new_splits =  [split for split in all_splits if split[0] == random_choice]
            all_splits = new_splits
        return DataFrame.from_array(all_splits,['axis', 'split_value', 'goodness of split'])

    def calc_goodness(self, split, axis_index):
        goodness = self.impurity
        low = []
        high = []
        for point in self.df.to_array():
            if point[axis_index] < split:
                low.append(point)
            elif point[axis_index] >= split:
                high.append(point)
        low_node = Node(DataFrame.from_array(low, self.df.columns), self.split_metric, depth = int(self.depth) + 1, check_splits = False)
        high_node = Node(DataFrame.from_array(high, self.df.columns), self.split_metric, depth = (self.depth+1), check_splits = False)
        nodes = [low_node, high_node]
        for split_node in nodes:
            goodness -= (len(split_node.row_indices)/len(self.row_indices)) * split_node.impurity
        return goodness

    def get_best_split(self):
        if self.possible_splits == []:
            self.best_split = None
            self.final_split = True
            return
        goodness_of_all_splits = [split[2] for split in self.possible_splits.to_array()]
        best_split = max(goodness_of_all_splits)
        index = goodness_of_all_splits.index(best_split)
        self.best_split_index = self.df.columns.index(self.possible_splits.to_array()[index][0])
        self.best_split = (self.possible_splits.to_array()[index][0],self.possible_splits.to_array()[index][1])

    def split(self, if_once = False, depth_needed = None):
        if depth_needed is None or self.depth < depth_needed:
            if self.low is None and self.high is None:
                if self.final_split is False:
                    self.possible_splits = self.get_possible_splits()
                    self.get_best_split()
                    low = []
                    high = []
                    for entry in self.df.to_array():
                        if entry[self.best_split_index] < self.best_split[1]:
                            low.append(entry)
                        elif entry[self.best_split_index] >= self.best_split[1]:
                            high.append(entry)
                    self.low = Node(DataFrame.from_array(low, self.df.columns), self.split_metric, (self.depth+1))
                    self.high = Node(DataFrame.from_array(high, self.df.columns), self.split_metric, (self.depth+1))
                    if not if_once:
                        self.low.split(depth_needed = depth_needed)
                        self.high.split(depth_needed = depth_needed)
                else:
                    return
            else:
                if self.low is not None:
                    self.low.split(if_once,depth_needed = depth_needed)
                if self.high is  not None:
                    self.high.split(if_once,depth_needed = depth_needed)
                return
        else:
            return
            