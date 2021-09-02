import sys
import os


from services import our_services as srvs
from components.header import heading
from components.functions import borncalculator,engineercalc,largeformat,multipletable,randomyearmarriage




# Header
heading()

# Service Menu
def menu():
    a = 0
    for i in sorted(srvs):
        a += 1
        print(str(a)+". >> "+str(i))
menu()

print('\n******** --------------- ********\n')

chooser = input("Enter choosen number: ")
def getnumber():
    # ask and input choosen number
    

    # Get menu numbers you have
    numbers = []
    a = 0
    for i in srvs:
        a += 1
        numbers.append(a)

    # check if is integer
    try:
        val=int(chooser)
        exists = int(chooser) in numbers
        if exists:
            return True
        else:
            return False
    except ValueError:
        print("Please use number to choose")

if getnumber()==True:
    #os.system('cls')
    set = int(chooser)
    if set==1:
        borncalculator()
    elif set==2:
        engineercalc()
    elif set==3:
        largeformat()
    elif set==4:
        multipletable()
    elif set==5:
        randomyearmarriage()

else:
    os.system('cls')
    print("\nPlease Choose number from menu\n")
    

    
    
