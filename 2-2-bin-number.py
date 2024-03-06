import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
numbers = [1, 0, 1, 1, 1, 1, 1, 0]

for i in range(8): GPIO.setup(dac[i], GPIO.OUT)
for i in range(8): GPIO.output(dac[i], numbers[i])

time.sleep(5)

for i in range(8): GPIO.output(dac[i], 0)

GPIO.cleanup()
