import time
from grovepi import *
button = 2
buzzer = 8

pinMode(buzzer, "OUTPUT")
pinMode(button, "INPUT")

while True:
    try:
        button_status=digitalRead(button)
        if button_status:
            digitalWrite(buzzer,1)
            print("I can hear the sound :)")
        else:
            digitalWrite(buzzer,0)
            print("Press the Button for a Buzzer...")

    except KeyboardInterrupt:
        digitalWrite(buzzer,0)
        print("The system is interrupted, exiting now...")
        break
    except (IOError, TypeError) as e:
        print("Something wrong with the IO of the Pi")



