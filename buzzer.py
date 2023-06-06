import time
from grovepi import *
led = 4
button = 2
buzzer = 3
ultrasonic=8
pinMode(buzzer,"OUTPUT")
pinMode(led,"OUTPUT")
time.sleep(1)
while True:
    try:
        print("It is running")
        distance = ultrasonicRead(ultrasonic)
        print("Distance is Cm", distance)
        if distance<=10:
            digitalWrite(led,1)
            digitalWrite(buzzer,1)
            print("led and buzzer are ON!!!")
        else:
            digitalWrite(led,0)
            digitalWrite(buzzer,0)
            print("They are off :(")
            
    except KeyboardInterrupt:
        digitalWrite(led,0)
        digitalWrite(buzzer,0)
        break
    except IOError:
        print("error")
                