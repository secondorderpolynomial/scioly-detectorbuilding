import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from numpy.polynomial.polynomial import Polynomial

def analyze_and_plot(file_name):
    # Read data from CSV
    data = pd.read_csv(file_name)
    voltage = data['voltage'].values
    concentration = data['concentration'].values

    # Polynomial fit (degree 2 and 3)
    poly1 = Polynomial.fit(voltage, concentration, 1)
    poly2 = Polynomial.fit(voltage, concentration, 2)
    poly3 = Polynomial.fit(voltage, concentration, 3)
    poly4 = Polynomial.fit(voltage, concentration, 4)

    # Generating a range of voltage values for plotting
    voltage_range = np.linspace(voltage.min(), voltage.max(), 500)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(voltage, concentration, color='black', label='Data points')
    plt.plot(voltage_range, poly1(voltage_range), label='Polynomial (Degree 1)', color='red')
    plt.plot(voltage_range, poly2(voltage_range), label='Polynomial (Degree 2)', color='blue')
    plt.plot(voltage_range, poly3(voltage_range), label='Polynomial (Degree 3)', color='green')
    plt.plot(voltage_range, poly4(voltage_range), label='Polynomial (Degree 4)', color='orange')
    plt.xlabel('Voltage')
    plt.ylabel('Concentration')
    plt.title('Curve Fitting to Data')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Print equations
    print("1st Degree Polynomial: ", np.poly1d(np.polyfit(voltage, concentration, 1)))
    print("2nd Degree Polynomial: ", np.poly1d(np.polyfit(voltage, concentration, 2)))
    print("3rd Degree Polynomial: ", np.poly1d(np.polyfit(voltage, concentration, 3)))
    print("4th Degree Polynomial: ", np.poly1d(np.polyfit(voltage, concentration, 4)))
    # Note: Printing the equation for a cubic spline is not straightforward due to its piecewise nature.

# Usage
analyze_and_plot('data.csv')
