import numpy as np
import pandas as pd

def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))

    test_set_size = int(len(data)) * test_ratio

    print(test_set_size)

    test_indices = shuffled_indices[:test_set_size]

    train_indices = shuffled_indices[test_set_size:]

    return data.iloc[train_indices], data.iloc[test_indices]

housing = pd.DataFrame([{1, 2, 3}, {1, 2, 3}])

train_set, test_set = split_train_test(housing, 0.2)

len(train_set)

len(test_set)