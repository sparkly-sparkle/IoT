import time
import board
import busio
import adafruit_adxl34x
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
while True:
    print ("%f %f %f"%accelerometer.acceleration)
    time.sleep(0.5)
from datetime import datetime
current_date_and_time = datetime.now()

print("The current date and time is", current_date_and_time)
