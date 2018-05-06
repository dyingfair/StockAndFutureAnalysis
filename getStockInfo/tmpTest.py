import pandas as pd
import numpy as np
import pandas as pd

def get_history_date_mean(data):
    len_data = len(data)
    history_mean = []
    for i in range(len(data)) :
        history_mean.append(np.mean(data[0:i+1]))
    return history_mean

a = [1,2,3,4,5]
print(get_history_date_mean(a))
