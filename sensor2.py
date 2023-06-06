import time
import datetime
from grovepi import *
from grove_rgb_lcd import *
import grovepi
led=8
buzzer=3
temp_humidity_sensor=4
pinMode(led,"OUTPUT")
pinMode(buzzer,"OUTPUT")
while True:
    try:
        print("It is running")
        [temp,hum]=grovepi.dht(temp_humidity_sensor,0)
        t = str(temp)
        h = str(hum)
        
        setRGB(0,255,100)
        if math.isnan(temp) == False and math.isnan(hum) == False:
            print("Timestamped:", datetime.datetime.now(), "Temperature =", temp, "Humidity =", hum)
            setText("Temp:" + t + "c" + "\nHumidity:" + h + "%")
            
            if temp >= 25:
                setRGB(255,20,1)
                digitalWrite(led,1)
                digitalWrite(buzzer,1)
                print("Watch out the temperatre is high")
                setText("Temp:" + t + "c" + "\nHumidity" + h +"%")
                
                time.sleep(1)
            else:
                  digitalWrite(led,0)
                  digitalWrite(buzzer,0)
        else:
            continue
    except KeyBoardInterrupt or IOerror:
                  print("interrupted or IOError")
                  digitalWrite(led,0)
                  digitalWrite(buzzer,0)
                  break