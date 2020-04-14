nbVal = 0
valNotFinished = False
letsGo = False
nextNum = ''

fileR = open('codes.json','r')
fileW = open('soundUP2.txt','w')

fileW.write('             ')

while True:
    c = fileR.read(1)
    if c == ']':
        break
    if c != ' ' and c != ',' and letsGo:
        nextNum = nextNum + c
    if c == ',' and letsGo:
        nbVal += 1
        if nbVal < 6:
            if len(nextNum) == 3:
                nextNum = ' ' + nextNum
            fileW.write(nextNum + '    ')
            nextNum = ''
        if nbVal == 6:
            if len(nextNum) == 3:
                nextNum = ' ' + nextNum
            fileW.write(nextNum + '\n             ')
            nextNum = ''
            nbVal = 0
    if c == '[':
        letsGo = True

fileR.close()
fileW.close()