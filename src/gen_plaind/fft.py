import csv 
from scipy import fft
from scipy.signal import find_peaks
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

def find_nearest_point(data, target):
    min = 10000
    ans = 0
    for i in range(len(data)):
        if(abs(data[i] - target) < min):
            ans = i
            min = abs(data[i] - target)
    return ans

data_file = open('data.csv', 'a')
path = "D:\\LAB\\NILM\\DATA\\PLAID 2017 house2\\Heater (done)\\low"
for dfile in os.listdir(path):
    df = pd.read_csv(os.path.join(path, dfile),header=None)
    df = df.iloc[:, [0]]
    df.values.ravel()
    y = df.transpose().values.tolist()
    y = y[0]
    signal = []
    for i in range(len(y)):
        if i % 40 == 0:
            signal.append(y[i])
    
    sample_rate = 750 #hz
    duration = len(signal)/sample_rate
    N = len(signal)

    yf = fft.fft(signal)
    xf = fft.fftfreq(N, 1/sample_rate)
    magnitude = np.abs(yf)
    xf = xf[:len(xf)//2]
    magnitude = magnitude[:len(magnitude)//2]
    print(dfile)
    ans = []
    for i in range(1,6,2):
        k = find_nearest_point(xf, 60*i)
        A_f = [round(xf[k],2), round(magnitude[k],2)]
        ans.append(A_f)
    print(ans)
    plt.plot(xf, magnitude, '.-', markersize = 2)

    plt.show()