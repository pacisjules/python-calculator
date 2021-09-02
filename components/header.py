import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)
#Header
def heading():
    print(Fore.YELLOW + '*********************************')
    print(Fore.YELLOW + '*                               *')
    print(f"{Fore.CYAN}*  Calculate more with python   *")
    print(Fore.YELLOW + '*                               *')
    print(Fore.YELLOW + '*********************************\n')

    print(Fore.YELLOW + '****** Menu choosen number ******\n')