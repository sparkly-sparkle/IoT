from sense_hat import SenseHat
sense = SenseHat()
sense.clear
temp = sense.get_temperature()
print(temp)



from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
humidity = sense.get_humidity()
print(humidity)



from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
pressure = sense.get_pressure()
print(pressure)



import time
import board
import busio
import adafruit_adxl34x
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
while True:
    print ("%f %f %f"%accelerometer.acceleration)
    time.sleep(2)
from datetime import datetime
current_date_and_time = datetime.now()
print("The current date and time is", current_date_and_time)
