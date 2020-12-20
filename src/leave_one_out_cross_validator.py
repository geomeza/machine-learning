from dataframe import DataFrame
from k_nearest_neighbors import KNearestNeighborsClassifier

class LeaveOneOutCrossValidator:

    def __init__(self,classifier, dataframe, prediction_column):
        self.knn = classifier
        self.df = dataframe
        self.prediction_column = prediction_column
    
    def accuracy(self):
        correct = 0
        for i in range(len(self.df.to_array())):
            observation = {column:self.df.data_dict[column][i] for column in self.df.columns if column != self.prediction_column}
            removed_df = self.remove_row(i)
            self.knn.fit(removed_df, self.prediction_column)
            if self.knn.classify(observation) == self.df.data_dict[self.prediction_column][i]:
                correct+=1
        return correct/len(self.df.to_array())

    def remove_row(self, index):
        data = self.df.to_array()
        del data[index]
        return DataFrame.from_array(data, self.df.columns)
