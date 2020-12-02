import matplotlib.pyplot as plt
import sys
sys.path.append('src')
from k_nearest_neighbors import KNearestNeighborsClassifier
from dataframe import DataFrame


data = [['Shortbread'  ,     0.14     ,       0.14     ,      0.28     ,     0.44      ],
['Shortbread'  ,     0.10     ,       0.18     ,      0.28     ,     0.44      ],
['Shortbread'  ,     0.12     ,       0.10     ,      0.33     ,     0.45      ],
['Shortbread'  ,     0.10     ,       0.25     ,      0.25     ,     0.40      ],
['Sugar'       ,     0.00     ,       0.10     ,      0.40     ,     0.50      ],
['Sugar'       ,     0.00     ,       0.20     ,      0.40     ,     0.40      ],
['Sugar'       ,     0.02     ,       0.08     ,      0.45     ,     0.45      ],
['Sugar'       ,     0.10     ,       0.15     ,      0.35     ,     0.40      ],
['Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
['Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
['Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
['Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
['Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
['Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
['Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ],
['Shortbread'  ,     0.05     ,       0.12     ,      0.28     ,     0.55      ],
['Shortbread'  ,     0.14     ,       0.27     ,      0.31     ,     0.28      ],
['Shortbread'  ,     0.15     ,       0.23     ,      0.30     ,     0.32      ],
['Shortbread'  ,     0.20     ,       0.10     ,      0.30     ,     0.40      ]]
df_columns = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour']

# df = DataFrame.from_array(columns = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour'], data)
# k_classifier = KNearestNeighborsClassifier(df, 'Cookie Type')

accuracy = [0]

def copy(arr):
    copy = []
    for elem in arr:
        copy.append(elem)
    return copy

for i in range(1, len(data)):
    correct_observations = 0
    for j in range(len(data)):
        correct = data[j][0]
        data_copy = copy(data)
        copy_info = {df_columns[i]:data_copy[j][i] for i in range(1, len(df_columns))}
        random = data_copy[j]
        del data_copy[j]
        copy_df = DataFrame.from_array(data_copy, df_columns)
        copy_classifier = KNearestNeighborsClassifier(i)
        copy_classifier.fit(copy_df, 'Cookie Type')
        # copy_classifier = KNearestNeighborsClassifier(copy_df, 'Cookie Type')
        if copy_classifier.classify(copy_info) == correct:
            correct_observations += 1
    accuracy.append(correct_observations/len(data))


x_points = [x for x in range(0, len(data))]
plt.plot(x_points, accuracy,linewidth = 1)
plt.xlabel('k')
plt.ylabel('Percent Accuracy')
plt.savefig('best_k_accuracy.png')
plt.show()

print('MY GRAPH IS NOT THE SAME AND I DONT KNOW WHY')
print('But anyways, my graph shows that accuracy is lowest at the endpoint, more so towards too many inputs so yes my graph makes sense according to what I new')
print('I think a good estimate would be like 1/4th of the graph to 1/3rd of it. Notice how the highest spikes are around 4-5 and the accuracy is still relatively high at 6 as well. So I think a good k size would be 25-34 Percent of the graph')