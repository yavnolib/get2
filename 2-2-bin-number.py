import RPi.GPIO as GPIO
import time

dac =  [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 1, 0, 1, 1, 1, 1, 0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, number)
time.sleep(15)
GPIO.output(dac, 0)
GPIO.cleanup()

##############################################
# number_2 = [0, 0, 0, 0, 0, 0, 1, 0]
# number_255 = [0, 1, 1, 1, 1, 1, 1, 1]
# number_127 = [0, 0, 1, 1, 1, 1, 1, 1]
# number_64 = [0, 0, 1, 0, 0, 0, 0, 0]
# number_32 = [0, 0, 0, 1, 0, 0, 0, 0]
# number_5 = [0, 0, 0, 0, 0, 1, 0, 1]
# number_0 = [0, 0, 0, 0, 0, 0, 0, 0]
# number_256 = [1, 0, 0, 0, 0, 0, 0, 0]
##############################################

