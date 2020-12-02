from dataframe import DataFrame
from node import Node

class DecisionTree:

    def __init__(self, df):
        self.df = df
        self.df = self.df.append_columns({'indices': [i for i in range(len(df.to_array()))]})
        self.root = Node(self.df)

    def split(self):
        self.root.split()