import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

# GPIO.output(leds[0], 1)
for i in leds:
	GPIO.output(i, 1)
	time.sleep(0.2)
	GPIO.output(i, 0)

count = 0
while (count < 3):
	for i in leds:
		GPIO.output(i, 1)
		time.sleep(0.2)
		GPIO.output(i, 0)
GPIO.output(leds, 0)
