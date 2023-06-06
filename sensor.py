import time
from grovepi import *
led = 4
pinMode(led, "OUTPUT")
time.sleep(1)
while True:
    try:
        print("It is running ..")
        digitalWrite(led,1)
        time.sleep(1)
        digitalWrite(led,0)
        time.sleep(1)
    except KeyboardInterrupt:
        digitalWrite(led,0)
        break
    except IOError:
        print("Error")