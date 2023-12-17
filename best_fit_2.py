import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from numpy.polynomial.polynomial import Polynomial

PLOYNOMIAL_DEGREE = 2
def analyze_and_plot(file_names):
    plt.figure(figsize=(10, 6))
    colors = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'pink', 'brown', 'black', 'gray']
    color_cursor = 0

    for file in file_names:
      # file is of the form '2000ppm.csv'
      concentration = file.split('ppm')[0]
      data = pd.read_csv(file, header=0)
      timems = data['timems'].values
      voltage = data['voltage'].values
      voltage = voltage * 1000

      poly4 = Polynomial.fit(timems, voltage, PLOYNOMIAL_DEGREE)

      # Generating a range of voltage values for plotting
      voltage_range = np.linspace(voltage.min(), voltage.max(), 500)

      # Plot
      plt.plot(timems, poly4(timems), color=colors[color_cursor], label=concentration + ' ppm')
      print(concentration + ' ppm: ', np.poly1d(np.polyfit(timems, voltage, PLOYNOMIAL_DEGREE)))

      color_cursor += 1

    plt.xlabel('time (millis)')
    plt.ylabel('voltage (volts)')
    plt.title('Degree = ' + str(PLOYNOMIAL_DEGREE))
    plt.legend()
    plt.grid(True)
    plt.show()

# Usage
analyze_and_plot(['2000ppm.csv', '3000ppm.csv', '4000ppm.csv', '5000ppm.csv'])
