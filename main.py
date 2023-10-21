import random as rand
import time

score = 0


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
    
    while(usrInput == test):
        test = generateTest()
        userInput = input(f'{test}\n')
        if(userInput == test):
            score += 1
    
    # t1 = time.time()
    # print("score: ",score," ", (t1 - t0), " seconds")
        
    


    