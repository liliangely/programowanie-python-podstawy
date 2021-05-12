'''from colorama import init
from termcolor import colored
init()
print(colored('Hejka!', 'yellow'))

for i in range(10):
    print(i)


cyfra=0
while cyfra!=10:
    print(cyfra)
    cyfra+=1



znak=''
print("Aby zakończyć program wciśnij 'q'")
while znak!='q':
    print("Nie wcisnąłeś 'q'")
    znak=input()



print("Aby zakończyć program wciśnij 'q'")
while True:
    znak= input()
    if znak!='q':
        print("Nie wcisnąłeś 'q'")
    else:
        break



import os
while True:
    os.system('cls')
    print("Aby zakończyć program wciśnij 'q'")
    print("Aby wyświetlić imię wciśnij 'i'")
    print("Aby wyświetlić nazwę przedmiotu wciśnij 'n'")
    znak=input()
    if znak=='i':
        print("X")
    elif znak=='n':
        print("Kogni")
    elif znak=='q':
        break
    else:
        print("Nieprawidłowy znak")


for i in range(1,4):
    for j in range(1,5):
        print("To jest", i,"wykonanie zew pętli i", j,"wew pętli.")




zad1

print("Podaj pierwszą liczbę")
liczbaa=float(input())
print("Podaj drugą liczbę")
liczbab=float(input())
print("Jaka operacja ma być wykonana?")
operacja=input()
if operacja=='dodawanie':
    print("Wynik dodawania:", liczbaa+liczbab)
elif operacja=='odejmowanie':
    print("Wynik odejmowania:", liczbaa-liczbab)
elif operacja=='mnożenie':
    print("Wynik mnożenia:", liczbaa*liczbab)
elif operacja=='dzielenie':
    print("Wynik dzielenia:", liczbaa/liczbab)
else:
    print("Nie wybrano operacji.")
print("Aby zakończyć program wciśnij 'q'")
while True:
    znak=input()
    if znak!='q':
        print("Nie wcisnąłeś 'q'")
    else:
        break


zad2

suma=0
for i in range(51):
    suma+=i
    print(suma)

suma=0
cyfra=0
while cyfra!=51:
    print(suma)
    cyfra+=1
    suma+=cyfra




zad3
'''
'''
k=57


for i in range(101):
    if i==4:
        print("")
    if i==34:
        print("")
    while k!=74:
        print()
    else:
        print(i)
'''



'''

zad4

from colorama import init
from termcolor import colored
init()
print(colored('\t       x','green'))
print(colored('\t      xxx','green'))
print(colored('\t     xx','green') + colored('x','red') + colored('xx','green'))
print(colored('\t    xxxxxxx','green'))
print(colored('\t   xx','green') + colored('x','red') + colored('x','green') + colored('x', 'blue') + colored('x','green') + colored('x','red') + colored('xx','green'))
print(colored('\t  xxxxxxxxxxx','green'))
print(colored('\t x','green') + colored('x','magenta') + colored('x','green') + colored('x','red') + colored('x','green') + colored('xxx','blue') + colored('x','green') + colored('x','red') + colored('x','green') + colored('x','magenta') + colored('x','green'))
print(colored('\txxxxxxxxxxxxxxx','green'))
print("\t     ||||")
print("\t     ||||")





zad5

for i in range(0,1000):
    for j in range(0,10000):
        for k in range(0,10000):
            print(i, j, k)





zad6

for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            print(i, j, k)


zad7


suma=0
for i in range(25,51):
    suma=suma+i
    print(suma)

cyfra=25
sumka=0
while cyfra!=51:
    sumka=sumka+cyfra
    print(sumka)
    cyfra+=1






zad8

suma=0
for i in range(26,51,2):
    suma=suma+i
    print(suma)


cyfra=26
sumka=0
while cyfra!=51:
    sumka=sumka+cyfra
    print(sumka)
    cyfra+=1





zad9


for i in range(1,10):
    for j in range(2,20,2):
        for k in range(3,30,3):
            for l in range(4,40,4):
                for m in range(5,50,5):
                    print(i,j,k,l,m)






zad10


print("Z ilu jajek?")
liczbajajek=int(input())
for i in range(0,liczbajajek):
    print("Wybij jajko na patelnie.")
print("Dodaj sól.")
print("Mieszaj.")
print("Gotowe.")


zad11
'''
while True:
    print("Aby zakończyć program wciśnij 'q'")
    print("Aby wyświetlić imię wciśnij 'i'")
    print("Aby wyświetlić nazwę przedmiotu wciśnij 'n'")
    print("Aby wyświetlić sumę wciśnij 's'")
    print("Aby wyświetlić choinkę wciśnij 'h'")
    znak=input()
    if znak=='i':
        print("X")
    elif znak=='n':
        print("Kogni")
    elif znak=='q':
        break
    elif znak=='s':
        suma=0
        for i in range(51):
            suma+=i
            print(suma)
    elif znak=='h':
        from colorama import init
        from termcolor import colored
        init()
        print(colored('\t       x','green'))
        print(colored('\t      xxx','green'))
        print(colored('\t     xx','green') + colored('x','red') + colored('xx','green'))
        print(colored('\t    xxxxxxx','green'))
        print(colored('\t   xx','green') + colored('x','red') + colored('x','green') + colored('x', 'blue') + colored('x','green') + colored('x','red') + colored('xx','green'))
        print(colored('\t  xxxxxxxxxxx','green'))
        print(colored('\t x','green') + colored('x','magenta') + colored('x','green') + colored('x','red') + colored('x','green') + colored('xxx','blue') + colored('x','green') + colored('x','red') + colored('x','green') + colored('x','magenta') + colored('x','green'))
        print(colored('\txxxxxxxxxxxxxxx','green'))
        print("\t     ||||")
        print("\t     ||||")
    else:
        print("Nieprawidłowy znak")
