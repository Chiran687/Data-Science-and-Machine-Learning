import pandas as pd
import csv

path = "/home/chiran/KMC_Course/Data_Science_Machine_Learning/Week_4/Day_3/apple_quality.csv"


def mean_value(lst):
    return float(sum(lst)) / max(len(lst), 1)


def median_value(lst):
    lst.sort()
    if len(lst) % 2 == 0:
        median1 = lst[len(lst)//2]
        median2 = lst[len(lst)//2 - 1]
        median = (median1 + median2)/2
    else:
        median = lst[len(lst)//2]
    return median


def mode_value(lst):
    max = 0
    res = lst[0]
    for i in lst:
        freq = lst.count(i)
        if freq > max:
            max = freq
            res = i
    return res


with open(path) as csv_content:
    csv_reader = csv.reader(csv_content, delimiter=',')
    column_names = []
    for i in csv_reader:
        column_names.append(i)
        break
    new_column = column_names[0]
    new_column.pop()

    for x in column_names[0]:

        data = pd.read_csv(path, usecols=[x])
        data.dropna(subset=[x], inplace=True)
        list_data = data[x].tolist()
        print(x)
        print(f"Mean for {x} {mean_value(list_data)}")
        print(f"Median for {x}  {median_value(list_data)}")
        print(f"Mode for {x} {mode_value(list_data)} \n")
