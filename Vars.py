# vars
import time
import random
import os
import subVars
TDays = 7
TAmount = 15
check = True
Balance = 30
Pay = 20
No1 = 1
No2 = 2
BNo1 = random.randint(1,2)
BNo2 = random.randint(1,2)
# functions
def play():
    global check
    global BNo1
    global BNo2
    global No1
    global No2
    global Balance
    while check:
        Balance = Balance - 5
        if Balance <= 0:
            Balance = 0
        subVars.checkBreaker()
        subVars.choose()
        subVars.checkBreaker()
        subVars.Randomize()
        subVars.checkBreaker()
        subVars.Results()
        subVars.checkBreaker()
        subVars.Taxes()
        subVars.checkBreaker()
        subVars.Summary()
        print("=========================================================================================================")
        os.system('cls')
    else:
        print("You lost. Thanks for playing! If there is a bug, please hit me up @ MiddleAncient#2269 as I am \nconstantly looking to fix bugs. I also take suggestions. Thank you!!")
