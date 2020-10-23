class DataFrame:
    def __init__(self, data,  column_order = None):
        self.data_dict = data
        if column_order is not None:
            self.columns = column_order
        else:
            self.columns = [key for key in data.keys()]
        self.array = None

    def to_array(self):
        cols = [self.data_dict[key] for key in self.data_dict.keys()]
        self.array = [list(arr) for arr in zip(*cols)]
        return self.array

    def filter_columns(self, columns):
        new_dict = {}
        for key in self.data_dict.keys():
            if key in columns:
                new_dict.update({key : self.data_dict[key]})
        new_dataframe = DataFrame(new_dict, columns)
        return new_dataframe

    def apply(self, person, function):
        self.to_array()
        index = self.columns.index(person)
        for i in range(len(self.array)):
            self.array[i][index] = function(self.array[i][index])
            self.data_dict[person][i] = self.array[i][index]
        return self

    def append_pairwise_interactions(self):
        new_dict = self.data_dict
        new_names = []
        for i in range(len(self.columns)):
            for j in range(len(self.columns)):
                if j > i:
                    new_names.append(self.columns[i] + '_' + self.columns[j])
        new_arrays = []
        for i in range(len(self.columns)):
            for j in range(len(self.columns)):
                first_arr = self.data_dict[self.columns[i]]
                second_arr = self.data_dict[self.columns[j]]
                interaction_arr = []
                if j > i:
                    for k in range(len(first_arr)):
                        interaction_arr.append(first_arr[k] * second_arr[k])
                    new_arrays.append(interaction_arr)
        for i in range(len(new_names)):
            new_dict.update({new_names[i] : new_arrays[i]})
        new_columns = [column for column in self.columns]
        new_columns.extend(new_names)
        return DataFrame(new_dict, new_columns)

    def create_dummy_variables(self):
        new_dict = {key:val for key, val in self.data_dict.items() if key in self.columns} 
        new_data_cols = []
        for key in new_dict.keys():
            if key in self.columns:
                if isinstance(new_dict[key][0], int) is False:
                    new_data_cols.append(key)
        for key in new_data_cols:
            if isinstance(new_dict[key][0], str):
                for dummy in self.data_dict[key]:
                    new_dict.update({(key + "_" + dummy):[1 if dummy == data else 0 for data in self.data_dict[key]]})
            elif isinstance(new_dict[key][0], list):
                dummies = self.extract_dummies(new_dict[key])
                transformed_data = self.transform_data(dummies, new_dict[key])
                for i in range(len(dummies)):
                    new_dict.update({dummies[i]:transformed_data[i]})
            del new_dict[key]
        columns = [key for key in new_dict.keys()]
        return DataFrame(new_dict, columns)
    
    def remove_columns(self, columns):
        new_dict = {key:val for key, val in self.data_dict.items() if key not in columns} 
        new_cols = [key for key in new_dict.keys()]
        return DataFrame(new_dict, new_cols)

    def append_columns(self, new_data_dict):
        new_dict = self.data_dict
        for key in new_data_dict.keys():
            new_dict.update({key:new_data_dict[key]})
        new_cols = [key for key in new_dict.keys()]
        return DataFrame(new_dict, new_cols)

    def extract_dummies(self, arrays):
        dummies = []
        for arr in arrays:
            for a in arr:
                if a not in dummies:
                    dummies.append(a)
        return dummies

    def transform_data(self, dummies, data):
        new_data = [[] for i in range(len(dummies))]
        for arr in data:
            for dummy in dummies:
                ind_of_dummy = dummies.index(dummy)
                if dummy in arr:
                    new_data[ind_of_dummy].append(1)
                else:
                    new_data[ind_of_dummy].append(0)
        return new_data

data_dict = {
    'id': [1, 2, 3, 4],
    'color': ['blue', 'yellow', 'green', 'yellow']
}

# df1 = DataFrame(data_dict, column_order = ['id', 'color'])
# df2 = df1.create_dummy_variables()
# print(df2.to_array())
# print(df2.data_dict)

# df3 = df2.remove_columns(['id', 'color_yellow'])
# print(df3.columns)

