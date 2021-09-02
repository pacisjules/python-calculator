
import colorama
from colorama import Back, Fore, Style
import datetime
now = datetime.datetime.now()
import random



#Born calculate
def borncalculator():
    print("\n*** Born Calculator ***\n")
    this_year=int(now.year)
    your_age=input("Enter your age here: ")
    result=this_year-int(your_age)
    print("You born in "+str(result))
#borncalculator()

#Enginner calculate
def engineercalc():
    print("\n*** Engineer Calculator ***\n")
    
#engineercalc()

#Largeformat calculate
def largeformat():
    print("\n*** Large format square meter accounting***\n")

    client_name=input("Enter name of client:")
    material_type=input("Material type:")
    cash_of_mat=input("Enter charged money on Square meter:")
    widht=input("Enter width in cm:")
    height=input("Enter heigth in cm:")

    #Check if used the numbers
    cashmat=cash_of_mat.isnumeric()
    w=widht.isnumeric()
    h=height.isnumeric()

    def checking_nums():
        if cashmat==False or w==False or h==False:
            print('Please use the numbers')
            return False
    if checking_nums()==False:
        return False
    else:
        result_sq=(float(widht)*float(height))/10000
        result_cash=result_sq*float(cashmat)
        print("\nMr/Miss "+client_name+"he will pay "+str(result_sq)+" of "+material_type+" Payment of "+str(result_cash)+" Rwfs")
        return True
#largeformat()

#Multiple Table
def multipletable():
    print("\n*** Multiple table***\n")
    table=input('Enter number of table you want to run:')
    numbers=0

    print(Fore.CYAN+"\n*** Multiple table of "+table+" ***\n............................")
    for i in range(12):
        numbers+=1
        print(str(numbers)+" X "+str(table)+" = "+str(int(numbers)*int(table)))

#multipletable()

#Random mariage
def randomyearmarriage():
    print("\n*** Random year for your marriage***\n")
    name=input("Give your name: ")
    your_age=input("Enter your age: ")
    your_agenda=input("Enter your gender [F].Female or [M]Male: ")

    if your_agenda=="M":
        this_year=int(now.year)
        result=random.randint(int(your_age), 44)
        year_for=int(result)-int(your_age)
        print("Mr "+name+" you can get marriage on "+str(result)+" year old in "+str(int(year_for)+int(this_year))+" Year remain "+str(year_for)+" years")
    if your_agenda=="F":
        this_year=int(now.year)
        
        result=random.randint(int(your_age), 38)
        year_for=int(result)-int(your_age)
        print("\nMiss "+name+" you can get marriage on "+str(result)+" year old in "+str(int(year_for)+int(this_year))+" Year remain "+str(year_for)+" years")

#randomyearmarriage()