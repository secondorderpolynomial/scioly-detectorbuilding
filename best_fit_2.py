import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from numpy.polynomial.polynomial import Polynomial

PLOYNOMIAL_DEGREE = 4
concentration_vs_color = {
'500': 'purple',
  '1000': 'brown',
  '1500': 'black',
  '2000': 'red',
  '2500': 'magenta',
  '3000': 'green',
  '3500': 'lime',
  '4000': 'blue',
  '4500': 'teal',
  '5000': 'orange'
}
#colors = ['purple', 'brown', 'black', 'red', 'magenta', 'green', 'lime', 'blue', 'teal', 'orange', 'coral', 'gold', 'navy', 'olive', 'orchid', 'plum', 'salmon', 'tan', 'turquoise', 'violet', 'wheat', 'yellowgreen']

def analyze_and_plot(file_names):
    plt.figure(figsize=(10, 6))
    color_cursor = 0

    for file in file_names:
      print('Analyzing file: ', file)
      # file is of the form '2000ppm.csv'
      concentration = file.split('ppm')[0]
      data = pd.read_csv(file, header=0)
      # data = data[data['timems'] < 125_000]

      timems = data['timems'].values
      timems = timems / 1000
      voltage = data['voltage'].values
      voltage = voltage * 1000

      poly4 = Polynomial.fit(timems, voltage, PLOYNOMIAL_DEGREE)

      # Plot
      color = concentration_vs_color[concentration]
      plt.scatter(timems, voltage, color=color, s=1)
      plt.plot(timems, poly4(timems), color=color, label=concentration + ' ppm')

      # label
      x1 = 125
      y1 = poly4(x1) + 1
      plt.text(x1, y1, concentration + ' ppm', color=color, va='center', ha='left')

      print(concentration + ' ppm: ', np.poly1d(np.polyfit(timems, voltage, PLOYNOMIAL_DEGREE)))
      color_cursor += 1

    plt.xlabel('time (seconds)')
    plt.ylabel('voltage (mV)')
    plt.title('Degree = ' + str(PLOYNOMIAL_DEGREE))
    plt.legend()
    plt.grid(True)
    plt.show()

# Usage
# analyze_and_plot(['2000ppm.csv', '3000ppm.csv', '4000ppm.csv', '5000ppm.csv'])
analyze_and_plot(['500ppm.csv', '1000ppm.csv', '1500ppm.csv', '2000ppm.csv', '2500ppm.csv', '3000ppm.csv', '3500ppm.csv', '4000ppm.csv', '4500ppm.csv', '5000ppm.csv'])
