import RPi.GPIO as GPIO
from matrix_lite import led
import time

toggle = 100
everloop = ['black'] * led.length

GPIO.setmode(GPIO.BOARD)

GPIO.setup(33, GPIO.OUT)

print(GPIO.input(33))

GPIO.output(33, GPIO.HIGH)

while True:
    everloop[0] = {'b':toggle}
    if toggle == 100:
        toggle = 0
    else:
        toggle = 100
    led.set(everloop)
    time.sleep(1)
    