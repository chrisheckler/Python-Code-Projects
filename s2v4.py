from s2v3 import *

def find_average(data_sample, header=False):
    if header:
        data_sample = data_sample[1:]
    total = calculate_sum(data_sample)
    size = number_of_records(data_sample)
    average = total / size
    return average

average_price = find_average(data_from_csv, True)
print("Average = ", average_price)
print('{:03.2f}'.format(average_price))
