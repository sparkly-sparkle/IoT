from gpiozero import MotionSensor
pir = MotionSensor(8)
while True:
   print("continue scanning for humans")
   pir.wait_for_motion()
   print("moving human detected!scream")
   pir.wait_for_no_motion()
   print("human deactivated")

