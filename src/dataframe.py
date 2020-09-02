data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sara': [3, 1, 4, 0]
}

class DataFrame:
    def __init__(self, data,  column_order):
        self.data_dict = data
        self.columns = column_order
        self.array = None

    def transform_to_array(self, column_order):
        columns = []
        for i in range(len(self.data_dict[column_order[0]])):
            columns.append([])
            for j in self.data_dict.keys():
                columns[i].append(0)
        for key in self.data_dict.keys():
            index = column_order.index(key)
            val_index = 0
            for value in self.data_dict[key]:
                columns[val_index][index] = self.data_dict[key][val_index]
                val_index += 1
        return columns

    def to_array(self):
        if self.array is None:
            self.array = self.transform_to_array(self.columns)
        return self.array

    def filter_columns(self, columns):
        new_dict = {}
        for key in self.data_dict.keys():
            if key in columns:
                new_dict.update({key : self.data_dict[key]})
        new_dataframe = DataFrame(new_dict, columns)
        return new_dataframe

    def apply(self, person, function):
        print(person, 'Person')
        index = self.columns.index(person)
        for i in range(len(self.array)):
            self.array[i][index] = function(self.array[i][index])
            self.data_dict[person][i] = self.array[i][index]
        return self
