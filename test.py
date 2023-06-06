import socket
import time


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
import csv
from datetime import datetime

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)


# Open a new CSV file for writing
filename = "test_data_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"
with open(filename, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write a header row to the CSV file
    writer.writerow(["Timestamp", "X", "Y", "Z"])

    # Continuously read and write accelerometer data to the CSV file
    while True:
        # Read accelerometer data
        x, y, z = accelerometer.acceleration
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

        # Print and write the accelerometer data to the CSV file
        print("%s, %f, %f, %f" % (timestamp, x, y, z))
        writer.writerow([timestamp, x, y, z])
        
        # Wait for half a second before reading the accelerometer again
        time.sleep(0.5)

               

bufferSize=1024
ServerIP='192.168.0.102'
ServerPort=2222
RPIServer=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
RPIServer.bind((ServerIP,ServerPort))
print('server is listening')
while True:
    cmd,address=RPIServer.recvfrom(bufferSize)
    cmd=cmd.decode('utf-8')
    print(cmd)
    print('Client Address',address[0])
    if cmd=='GO':
        result=SenseHat()
        if result.is_valid():
            data=str(result.temperature)+':'+str(result.humidity)+':'+str(result.pressure)
            data=data.encode('utf-8')
            RPIServer.sendto(data,address)