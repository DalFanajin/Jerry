from libs.lights import *

l = loopFlicker()
t = threading.Thread(target = l.flicker, args=('b',1,35,30))
t.start()
#l.isRunning = False