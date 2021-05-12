'''import time
cyfra=0
start=time.clock()
while cyfra!=1:
    cyfra=int(input("Nie wcisnąłeś '1'\n"))
koniec=time.clock()
czastrwania=koniec-start
print("Na wciśnięcie '1' potrzebowałeś: ", czastrwania)



import time
print("Początek: ", time.ctime())
time.sleep(4)
print("Koniec: ", time.ctime())






#zad1
import time
print("UWAGA!")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("BOOOOOOOM")






#zad6


import random
import time
print("Wpisz wylosowaną literę jak najszybciej")
litera="abcdefghijklmnoprstuwxyzvq"
wylosowana=random.choice(litera)
print(wylosowana)
start=time.clock()
wpisanalitera=input()
while wpisanalitera!=wylosowana:
    wpisanalitera=input("Nie wpisałeś poprawnej litery\n")
koniec=time.clock()
czastrwania=koniec-start
print("Wpisanie litery zajęło ci: ", czastrwania)


#zad7



import random
import time
print("Wpisz wylosowaną literę jak najszybciej.")
litera="abcdefghijklmnoprstuwxyzvq"
kolejka=0
zliczanieczasutrwania=0
while kolejka!=5:
    wylosowana=random.choice(litera)
    print(wylosowana)
    start=time.clock()
    wpisanalitera=input()
    while wpisanalitera!=wylosowana:
        wpisanalitera=input("Nie wpisałeś poprawnej litery.\n")
    kolejka+=1
    koniec=time.clock()
    czastrwania=koniec-start
    print("Wpisanie litery zajęło ci: ", czastrwania)
    zliczanieczasutrwania+=czastrwania
sredniaczas=zliczanieczasutrwania/5
print("Śrenio potrzebowałeś: ", sredniaczas)



#zad12

import time
print("Od ilu zacząć odlicznie?")
odlicznie=int(input())
time.sleep(1)
while odlicznie!=0:
    odlicznie-=1
    print(odlicznie)
    time.sleep(1)
print("Koniec odliczania.")
'''




#menu proba
import time
import os
while True:
    os.system('cls')
    print("Aby stoper wciśnij 'a'")
    print("Aby imie wciśnij 'b'")
    print("Aby wyjść wciśnij 'q'")
    znak=input()
    if znak=='a':
        print("Od ilu zacząć odlicznie?")
        odlicznie=int(input())
        time.sleep(1)
        while odlicznie!=0:
            odlicznie-=1
            print(odlicznie)
            time.sleep(1)
        print("Koniec odliczania.")
    elif znak=='b':
        print("X")
    elif znak=='q':
        break
    else:
        print("Nieprawidłowy znak.")
    input()
