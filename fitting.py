import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('eos.csv')

# Extract Volume and Energy values
V = data['Volume (A^3/atom)'].values
E = data['Energy (eV/atom)'].values

# Define the function E(V)
def E_func(V, a, b, c, d):
    return a + b * V**(-2/3) + c * V**(-4/3) + d * V**(-6/3)

# Fit the function to the data
params, params_covariance = curve_fit(E_func, V, E)

# Print the fitted parameters
print("Fitted parameters:")
print(f"a = {params[0]}")
print(f"b = {params[1]}")
print(f"c = {params[2]}")
print(f"d = {params[3]}")

# Plot the data and the fitted curve
plt.scatter(V, E, label='Data')
plt.plot(V, E_func(V, *params), label='Fitted function', color='red')
plt.xlabel('Volume (A^3/atom)')
plt.ylabel('Energy (eV/atom)')
plt.legend()
plt.show()
