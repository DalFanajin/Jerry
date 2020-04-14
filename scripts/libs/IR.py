import os

def IRSend(command):
    IRPath = "../res/IRs/"
    IRName = command
    os.system('/home/pi/Jerry/scripts/libs/ir_remote.py -p -g13 -f ' + IRPath + IRName + '.json ' + IRName)
