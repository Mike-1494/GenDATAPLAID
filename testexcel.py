import csv 
from scipy import fft
import pandas as pd
import numpy as np
import os

data_file = open('data.csv', 'a')
path = "D:\\LAB\\NILM\\Idea\\PLAID 2017 house2\\Compact Lamp (done)\\1155.csv "

df = pd.read_csv(path ,header=None)
df = df.iloc[:, [0]]
df.values.ravel()
y = df.transpose().values.tolist()
y = y[0]
I = y[20000:]

writer = csv.writer(data_file)
for i in range(len(I)):
    row = []
    if i % 60 == 0:
        row.append(I[i])
        print(row)
        writer.writerow(row)