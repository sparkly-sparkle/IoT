import time

from grovepi import *
led = 4
buzzer = 3

ultrasonic = 8

pinMode(led, "OUTPUT")
pinMode(buzzer, "OUTPUT")

time.sleep(1)

while True:
    try:
        print("It is running...")

        distance = ultrasonicRead(ultrasonic)
        print("Distance is cm:", distance)
        if distance<=10:
            digitalWrite(led,1)
            digitalWrite(buzzer,1)
            print("IoT LED and Buzzer is ON")
        else:
            digitalWrite(led,0)
            digitalWrite(buzzer,0)
            print("LED and Buzzer is OFF, Come Closer:")

    except KeyboardInterrupt:
        digitalWrite(led,0)
        digitalWrite(buzzer,0)
        break
    except IOError:
        print("Error")

