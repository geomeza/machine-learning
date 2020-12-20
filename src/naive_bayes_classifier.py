class NaiveBayesClassifier:

    def __init__(self, df, dependent_variable):
        self.df = df
        self.dep_var = dependent_variable

    def probability(self, column, boolean):
        stats = self.df.data_dict[column]
        return stats.count(boolean)/len(stats)

    def conditional_probability(self, probability, given):
        all_given = self.df.select_rows_where(lambda x: x[given[0]] == given[1])
        true_conditions = self.df.select_rows_where(lambda x: x[given[0]] == given[1] and x[probability[0]] == probability[1])
        return len(true_conditions.to_array())/len(all_given.to_array())

    def likelihood(self,probability,observed_features):
        result = self.probability(probability[0], probability[1])
        for entry in observed_features:
            result *= self.conditional_probability((entry, observed_features[entry]), given = probability)
        return result

    def classify(self, observed_features):
        true_classified = self.likelihood((self.dep_var, True), observed_features)
        false_classified = self.likelihood((self.dep_var, False), observed_features)
        return true_classified >= false_classified
    