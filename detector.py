from ti_hub import *
import time

# Connect to BB 5 (analog input) to measure voltage
voltage_port = analog_in("BB 5")

# Connect to BB 1, 2, and 3 (digital outputs) to control LEDs
red = digital("BB 1")
green = digital("BB 2")
blue = digital("BB 3")

# Specify the voltage ranges for red, green and blue LEDs. This is in volts.
# Ranges are left-inclusive and right-exclusive
voltage_red = (0.0, 0.75)
voltage_green = (0.75, 1.5)
voltage_blue = (1.5, 2.25)

# These variables are to calculate the average voltage
voltage_sum = 0
num_samples = 0

ignore_samples = 15

# Wait for user to press any key to start the measurement
print("Press any key to start")
input()

tic = int(round(time.time() * 1000))
for i in range(900):
  # Turn off all LEDs first
  red.off()
  green.off()
  blue.off()

  # Measure the reading from voltage sensor
  measured_data = voltage_port.measurement()
  # Convert the reading to voltage
  measured_voltage = measured_data / 16384 * 3.3

  # Write the measured voltage to the file against the time
  toc = int(round(time.time() * 1000))
  time_taken = toc - tic
  # f.write(str(time_taken) + "," + str(measured_voltage) + "\n")
  print(str(time_taken) + "," + str(measured_voltage))

  num_samples += 1
  # # Add the measured voltage to the sum for calculating average
  # if i > ignore_samples and measured_voltage > 0:
  #   voltage_sum += measured_voltage
  #   num_samples += 1
  #   print(measured_voltage, "avg: ", voltage_sum / num_samples, "V")

  # Turn on the correct LED based on the measured voltage
  if measured_voltage >= voltage_red[0] and measured_voltage < voltage_red[1]:
    # Turn on red LED
    red.on()
  if measured_voltage >= voltage_green[0] and measured_voltage < voltage_green[1]:
    # Turn on green LED
    green.on()
  if measured_voltage >= voltage_blue[0] and measured_voltage < voltage_blue[1]:
    # Turn on blue LED
    blue.on()

  # Wait for 0.1 seconds before taking the next measurement
  time.sleep(0.1)

  # print("Average measured voltage for ", num_samples, " samples: ", voltage_sum / num_samples, "V")

  measured_voltage = voltage_sum / num_samples
  if measured_voltage >= voltage_red[0] and measured_voltage < voltage_red[1]:
    # Turn on red LED
    red.on()
  if measured_voltage >= voltage_green[0] and measured_voltage < voltage_green[1]:
    # Turn on green LED
    green.on()
  if measured_voltage >= voltage_blue[0] and measured_voltage < voltage_blue[1]:
    # Turn on blue LED
    blue.on()


def best_fit(x):
  return 6.105e+11 * x ** 3 - 1.088e+10 * x ** 2 + 6.591e+07 * x - 1.332e+05


print("Using equation: 6.105e+11 x^3 - 1.088e+10 x^2 + 6.591e+07 x - 1.332e+05")
avg_voltage = voltage_sum / num_samples
concentration = best_fit(avg_voltage)
print("Measured concentration as", concentration, "ppm")

