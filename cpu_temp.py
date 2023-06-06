from gpiozero import CPUTemperature
from time import sleep, strftime, time

cpu = CPUTemperature()

with open("/home/pi/cpu_temp.csv", "a") as log:
	while True:
		temp = cpu.temperature
		log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
		sleep(1)

