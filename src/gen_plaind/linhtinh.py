import math
import matplotlib.pyplot as plt
signal = []
x = []
for i in range(-20,21,1):
    signal.append(math.cos(2*math.pi*i))
    x.append(i)
print(x)
plt.plot(x,signal, '.-')
plt.show()