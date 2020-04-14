import RPi.GPIO as GPIO
from matrix_lite import led
import time

everloop = ['black'] * led.length

GPIO.setmode(GPIO.BOARD)

GPIO.setup(33, GPIO.OUT)

GPIO.output(33, GPIO.LOW)

led.set(everloop)
    