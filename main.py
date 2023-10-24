import random as rand
import threading
import sys
from datetime import datetime
import time

score = 0
GAMEOVER = False

def timeElapsed(t0):
    t = datetime.now()
    return( t.second - t0.second)

def generateTest():
    i = 0
    start = 1
    stop = rand.randint(2,10)
    test = ""
    
    while(i <= rand.randrange(1,stop)):
        digit = rand.randint(0,10)
        test += str(digit)
        i += 1
        
    return test

def end_game():
    global GAMEOVER 
    GAMEOVER = True

timer = threading.Timer(10.0, end_game)

if __name__ == '__main__':
    userInput = ""
    test = ""
    timer.start()

    while(not GAMEOVER):
        test = generateTest()
        userInput = input(f'{test} ;\n')
        if(userInput == test):
            score += 1


    print(f"Score: {score}")

        
    
