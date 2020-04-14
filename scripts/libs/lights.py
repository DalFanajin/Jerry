from matrix_lite import led
from time import sleep
from math import pi, sin
import threading

def lightsOff():
    everloop = ['black'] * led.length

    led.set(everloop)
    
def flashLights(color, times, intensity):
    everloop = ['black'] * led.length
    led.set(everloop)
    
    for i in range(0,times):        
        for j in range(len(everloop)):
            everloop[j] = {color:intensity}


        led.set(everloop)
        sleep(0.2)
        
        everloop = ['black'] * led.length
        led.set(everloop)
        
        sleep(0.2)

#l = loopFlicker()
#t = threading.Thread(target = l.flicker, args=('b',1,35,30))
#t.start()
#l.isRunning = False
class loopFlicker(object):

    def __init__(self):
        self.isRunning = True

    def flicker(self, color, minHue, maxHue, speed):
        everloop = ['black'] * led.length

        adjustedColor = 0

        asc = True

        while self.isRunning:
            
            if asc and adjustedColor != maxHue:
                adjustedColor += 1
            elif asc and adjustedColor == maxHue:
                adjustedColor -=1
                asc = not asc
            elif not asc and adjustedColor != minHue:
                adjustedColor -= 1
            elif not asc and adjustedColor == minHue:
                adjustedColor +=1
                asc = not asc
                    
            for i in range(len(everloop)):
                everloop[i] = {color:adjustedColor}


            led.set(everloop)

            sleep(1/speed)
