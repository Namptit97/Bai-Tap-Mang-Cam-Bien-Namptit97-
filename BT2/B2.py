from random import randint
from time import sleep
print("Random")
try:
	while(1):	
		temperature = randint(28,30)
		humidity = randint(80,90)
		print("Temp: %s" %str(temperature))
		print("Hum: %s" %str(humidity))
		sleep(1)
except KeyboardInterrupt:
	print("Chuong trinh ket thuc")
