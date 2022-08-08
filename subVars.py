# vars
# Functions
import random
import os
import Vars

# BETTING NUMBER CHOOSER
def checkBreaker():
    if Vars.Balance <= 0:
        Vars.check = False
def choose():
    Ch1 = input("Choose a number between 1-2 *FIRST NUMBER*\n")
    if Ch1.isdigit():
        NCH1 = int(Ch1)
        if NCH1 == 1 or NCH1 == 2:
            Vars.No1 = NCH1
        elif NCH1 > 2 or NCH1 < 1:
            print("This isn't a number between 1 and 2. Using the last number you used...")
    elif Ch1.isdigit() == False:
        print("Can't use character, please use a number. Using the last number (or default number) you used...")
    Ch2 = input("Choose a number between 1-2 *SECOND NUMBER*\n")
    if Ch2.isdigit():
        NCH2 = int(Ch2)
        if NCH2 == 1 or NCH2 == 2:
            Vars.No2 = NCH2
        elif NCH2 > 2 or NCH2 < 1:
            print("This isn't a number between 1 and 2. Using the last number you used...")
    elif Ch2.isdigit() == False:
        print("Can't use character, please use a number. Using the last number (or default number) you used...")
    print("=======BETS========")
    print(Vars.No1, "and", Vars.No2)
# RANDOMIZE
def Randomize():
    Vars.BNo1 = random.randint(1, 2)
    Vars.BNo2 = random.randint(1, 2)
# RESULTS
def Results():
    # CHECK NUMBER ONE, CHECKS IF THE FIRST NUMBER IS THE SAME AS THE FIRSTNUMBER PUT ON BY THE HOUSE!
    print("======BETTING RESULT 1======")
    if Vars.No1 == Vars.BNo1:
        print("Your bet, ", Vars.No1, " matches with the number chosen by the house.")
        print("This means you won the first bet.")
    else:
        print("Your bet didn't match with the number chosen by the house.",Vars.No1,"was your bet,",Vars.BNo1,"was the number chosen by the house.")
    Cont = input("Press anything to continue.")
    print("======BETTING RESULT 2======")
    if Vars.No2 == Vars.BNo2:
        print("Your bet, ", Vars.No2, " matches with the number chosen by the house.")
        print("This means you won the second bet.")
    else:
        print("Your bet didn't match with the number chosen by the house.\n", Vars.No2, "was your bet,", Vars.BNo2,
              "was the number chosen by the house.")
    Cont = input("Press anything to continue.")
    print("====== Result ======")
    if Vars.No2 == Vars.BNo2 and Vars.No1 == Vars.BNo1:
        print("All bets were won. Awarding your pay of ", Vars.Pay)
        Vars.Balance = Vars.Balance + Vars.Pay
    else:
        print("Not all the bets were won. You did not win anything.")
def Summary():
    Cont = input("Press anything to continue to the summary...")
    print("======SUMMARY======")
    print("Your balance is now", Vars.Balance)
    print("Your taxes are due in", Vars.TDays, "days.")
    print(f"You will pay {Vars.TAmount}$ in taxes.")
    Vars.TDays = Vars.TDays - 1
def Taxes():
    if Vars.Balance <= 50:
        Vars.TAmount = 20
    elif Vars.Balance >= 50:
        Vars.TAmount = 30
    if Vars.TDays == 0:
        Vars.TDays = 7
        Vars.Balance = Vars.Balance - Vars.TAmount
def clear():
    command = 'cls'
    if os.name != 'nt':
    	command = 'clear'
    os.system(command)