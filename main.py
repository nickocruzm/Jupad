import random as rand
from datetime import datetime
import time

score = 0

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


if __name__ == '__main__':
    userInput = ""
    test = ""
    
    #t0 = time.gmtime(time.gmtime())
    start_time = time.time()
    end_time = start_time + 50
    

    
    
    while(0 <= (end_time - time.time()) ):
        test = generateTest()
        userInput = input(f'{test} ; \t {end_time - time.time()}\n')
        if(userInput == test):
            score += 1
    
    print("score: ", score)


    # t1 = time.time()
    # print("score: ",score," ", (t1 - t0), " seconds")
        
    


    
