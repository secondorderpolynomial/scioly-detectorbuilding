from ti_hub import *

# Connect to BB 5 (analog input) to measure voltage
voltage = analog_in("BB 5")

# Connect to BB 1, 2, and 3 (digital outputs) to control LEDs
red = digital("BB 1")
green = digital("BB 2")
blue = digital("BB 3")

voltage_red = (0.0, 0.75)
voltage_green = (0.75, 1.5)
voltage_blue = (1.5, 2.25)

# These variables are to calculate the average voltage
voltage_sum = 0
num_samples = 0

for i in range(10):
  # Turn off all LEDs first
  red.off()
  green.off()
  blue.off()

  # Measure the reading from voltage sensor
  measured_data = voltage.measurement()
  # Convert the reading to voltage
  measured_voltage = measured_data / 16384 * 3.3

  # Add the measured voltage to the sum for calculating average
  voltage_sum += measured_voltage
  num_samples += 1

  # Debug message to print the measured voltage
  print(measured_voltage)

  if measured_voltage >= voltage_red[0] and measured_voltage < voltage_red[1]:
    # Turn on red LED
    red.on()
  elif measured_voltage >= voltage_green[0] and measured_voltage < voltage_green[1]:
    # Turn on green LED
    green.on()
  elif measured_voltage >= voltage_blue[0] and measured_voltage < voltage_blue[1]:
    # Turn on blue LED
    blue.on()

  sleep(0.1)

print("Average measured voltage for ", num_samples, " samples: ", voltage_sum / num_samples, "V")
