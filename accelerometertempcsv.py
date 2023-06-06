import time
import board
import busio
import adafruit_adxl34x
import csv
from datetime import datetime
from sense_hat import SenseHat

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
sense = SenseHat()
sense.clear()

# Open a new CSV file for writing
filename = "accelerometer_data_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"
with open(filename, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    

# Write a header row to the CSV file
    writer.writerow(["Timestamp", "X", "Y", "Z", "temperature"])
  
# Continuously read and write accelerometer data to the CSV file
while True:
    # Read accelerometer data
    x, y, z = accelerometer.acceleration
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    # write temperature data to the CSV file
    temp = sense.get_temperature()
    writer.writerow([timestamp, x, y, z, temp])
        
    # Print and write the accelerometer data to the CSV file
    print("%s, %f, %f, %f" % (timestamp, x, y, z, temp))

    # Wait for half a second before reading the accelerometer again
    time.sleep(0.5)
csvfile.close()