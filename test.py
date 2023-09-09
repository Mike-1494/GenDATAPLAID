import pandas as pd 
import numpy as np
from scipy import fft
import matplotlib.pyplot as plt

df = pd.read_csv('D:\\LAB\\NILM\\DATA\\PLAID 2017 house2\\Air Conditioner (done)\\Frigidaire\\highcool\\1105.csv ')
i = df.iloc[:, [0]]
u = df.iloc[:, [1]]
i.values.ravel()
u.values.ravel()
i = i.transpose().values.tolist()
u = u.transpose().values.tolist()
#print(len(y))
i = i[0]
u = u[0]
U = np.array(u)
I = np.array(i)
instantaneous_power = U*I
i = i[155000:160000]
u = u[155000:160000]
import numpy as np


def power(voltage, current):
  """Calculates the active power from a list of instantaneous voltage and current measurements.

  Args:
    voltage: A list of voltage measurements.
    current: A list of current measurements.

  Returns:
    The active power.
  """

  vrms = np.sqrt(np.mean(voltage**2))
  irms = np.sqrt(np.mean(current**2))
  Vm = np.max(voltage)
  Im = np.max(current)
  cos_theta = np.mean(voltage * current) / (vrms * irms)
  theta = np.arccos(cos_theta)
  apparent_power = vrms * irms 
  active_power = vrms * irms *cos_theta
  reactive_power = vrms *irms *np.sin(theta)
  return apparent_power, active_power, reactive_power, cos_theta


def V_I(voltage, current):
  vrms = np.sqrt(np.mean(voltage**2))
  irms = np.sqrt(np.mean(current**2))
  Vm = np.max(voltage)
  Im = np.max(current)
  return vrms, irms, Vm, Im

# Generate some sample data
voltage = np.array(u)
current = np.array(i)

# Calculate the active power
S, P, Q , cos_theta = power(voltage, current)
vrms, irms, Vm, Im = V_I(voltage, current)
# Print the results
print("Vrms =", vrms)
print("Irms =",irms)
print("Vm =",Vm)
print("Im =",Im)
print("pf =", cos_theta)
print("Apparent Power =",S)
print("Reactive Power =",Q)
print("Active Power =",P)
print("I*cos(phi) =", irms*cos_theta)
plt.plot(voltage/100, label = "voltage")
plt.plot(current, 'r', label= "current")
plt.legend(loc="upper left")
plt.xlabel("Time (1/30000s)")
plt.ylabel("V (10^2 V)   I(A)")
plt.show()
plt.plot(instantaneous_power)
plt.xlabel("Time (1/30000s)")
plt.ylabel("Instantaneous Power (W)")
plt.show()