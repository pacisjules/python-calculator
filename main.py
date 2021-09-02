from services import our_services as srvs
from components.header import heading


#Header
heading()



#Service Menu
def menu():
    a=0
    for i in srvs:
        a+=1
        print(str(a)+". >> "+str(i))

menu()

print('\n******** --------------- ********\n')

#ask and input choosen number
chooser = input("Enter choosen number: ")

#Get menu numbers you have
numbers=[]
a=0
for i in srvs:
        a+=1
        numbers.append(a)

#check if is integer
try:
    val=int(chooser)
    if val>0 and val<numbers:
        print("Correct")

        #Actions Here

except ValueError:
    print("Please use number to choose")
