from dataframe import DataFrame

class KNearestNeighborsClassifier:

    def __init__(self, k):
        self.k = k
        self.dataframe = None
        self.prediction = None

    def fit(self, df, prediction):
        self.dataframe = df
        self.prediction = prediction

    def compute_distances(self, observation):
        data_arr = self.dataframe.to_array()
        data_dict = self.dataframe.data_dict
        distances = []
        for i in range(len(data_arr)):
            distances.append([sum([(observation[entry] - data_dict[entry][i])**2 for entry in observation])**(0.5), data_arr[i][0]])
        return DataFrame.from_array(distances, ['Distance', 'Cookie Type'])

    def nearest_neighbors(self, observation):
        return self.compute_distances(observation).order_by('Distance')

    def compute_average_distances(self, observation):
        distances = self.compute_distances(observation).to_array()
        cookie_types = {distance[1]: None for distance in distances}
        for cookie in cookie_types:
            cookie_distances = []
            for distance in distances:
                if distance[1] == cookie:
                    cookie_distances.append(distance[0])
            cookie_types[cookie] = sum(cookie_distances)/len(cookie_distances) 
        return cookie_types

    def classify(self, observation):
        closest_cookies = [self.nearest_neighbors(observation).to_array()[i][1] for i in range(self.k)]
        count_cookie_types = {cookie: closest_cookies.count(cookie) for cookie in closest_cookies}
        cookie_types = list(count_cookie_types.keys())
        cookie_counts = list(count_cookie_types.values())
        return cookie_types[cookie_counts.index(max(cookie_counts))]
        


# df = DataFrame.from_array(
#     ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour' ],
#     [['Shortbread'  ,     0.14     ,       0.14     ,      0.28     ,     0.44      ],
#     ['Shortbread'  ,     0.10     ,       0.18     ,      0.28     ,     0.44      ],
#     ['Shortbread'  ,     0.12     ,       0.10     ,      0.33     ,     0.45      ],
#     ['Shortbread'  ,     0.10     ,       0.25     ,      0.25     ,     0.40      ],
#     ['Sugar'       ,     0.00     ,       0.10     ,      0.40     ,     0.50      ],
#     ['Sugar'       ,     0.00     ,       0.20     ,      0.40     ,     0.40      ],
#     ['Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
#     ['Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
#     ['Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
#     ['Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
#     ['Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
#     ['Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
#     ['Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ]]
#     )

# knn = KNearestNeighborsClassifier(df, prediction_column = 'Cookie Type')

# observation = {
#     'Portion Eggs': 0.10,
#     'Portion Butter': 0.15,
#     'Portion Sugar': 0.30,
#     'Portion Flour': 0.45
# }

# # print(knn.compute_distances(observation).to_array())
# print(knn.nearest_neighbors(observation).to_array())
# # knn.compute_average_distances(observation)
# print(knn.classify(observation))