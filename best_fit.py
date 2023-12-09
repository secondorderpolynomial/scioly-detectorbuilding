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
    poly2 = Polynomial.fit(voltage, concentration, 2)
    poly3 = Polynomial.fit(voltage, concentration, 3)

    # Correcting the Cubic Spline fit
    # Group by unique voltage and calculate average concentration
    unique_voltage, indices = np.unique(voltage, return_inverse=True)
    mean_concentration = np.array([concentration[indices == i].mean() for i in range(len(unique_voltage))])
    cs = CubicSpline(unique_voltage, mean_concentration, extrapolate=True)

    # Generating a range of voltage values for plotting
    voltage_range = np.linspace(voltage.min(), voltage.max(), 500)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(voltage, concentration, color='black', label='Data points')
    plt.plot(voltage_range, poly2(voltage_range), label='Polynomial (Degree 2)', color='blue')
    plt.plot(voltage_range, poly3(voltage_range), label='Polynomial (Degree 3)', color='green')
    plt.plot(voltage_range, cs(voltage_range), label='Cubic Spline (Averaged Data)', color='red', linestyle='--')
    plt.xlabel('Voltage')
    plt.ylabel('Concentration')
    plt.title('Curve Fitting to Data')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Print equations
    print("2nd Degree Polynomial: ", np.poly1d(np.polyfit(voltage, concentration, 2)))
    print("3rd Degree Polynomial: ", np.poly1d(np.polyfit(voltage, concentration, 3)))
    # Note: Printing the equation for a cubic spline is not straightforward due to its piecewise nature.

# Usage
analyze_and_plot('data.csv')
