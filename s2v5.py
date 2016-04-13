from s2v4 import *

def find_min(data_sample, col):
    temp_list = []
    for row in data_sample:
        price = float(row[col])
        temp_list.append(price)
    return min(temp_list)

def find_max(data_sample, col):
    temp_list = []
    for row in data_sample:
        price = float(row[col])
        temp_list.append(price)
    return max(temp_list)

def find_max_min(data_sample, col, m='max'):
    temp_list = []
    val = 0
    for row in data_sample:
        price = float(row[col])
        temp_list.append(price)
    if m == 'max':
        val = max(temp_list)
    elif m == 'min':
        val = min(temp_list)
    else:
        pass
    return val
print(find_max_min(data_from_csv[1:], 2, 'min'))
print('The cheapest tie in the data set is: $' + str(find_min(data_from_csv[1:], 2)))
print('The most expensive tie in the data set is: $' + str(find_max(data_from_csv[1:], 2)))
