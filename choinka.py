import os
os.system("COLOR 02")
from colorama import init
from termcolor import colored
init()
print("\t              x")
print("\t             xxx")
print("\t            xx"+colored("x",'red')+"xx")
print("\t           xxxxxxx")
print("\t          xx"+colored("x",'red')+"x"+colored('x','blue')+colored('x','red')+"xxx")
print("\t         xxxxxxxxxxx")
print("\t        x"+colored('x','magenta')+"x"+colored('x','red')+"x"+colored('xxx','blue')+"x"+colored('x','red')+"x"+colored('x','magenta')+"x")
print("\t       xxxxxxxxxxxxxxx")
print(colored("\t             ||||",'white'))
print(colored("\t             ||||",'white'))
