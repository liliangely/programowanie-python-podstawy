'''import random
wylos=random.randint(1,10)
print(wylos)


import random
wyl=random.random()*10-5
print(wyl)

import random
wylosowana=random.random()
print(wylosowana)

zaokraglona=round(wylosowana,2)
print(zaokraglona)

print("%.2f"%wylosowana)



import random
slowo="kognitywistyka"
wylosowana=random.choice(slowo)
print(wylosowana)
'''
#zad1

import time
print("Uwaga!")
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
print("BOOM!")




'''




zad4
import random
wylosowana=random.randint(1,48)
print(wylosowana)
import random
wylosowana=random.randint(1,48)
print(wylosowana)
import random
wylosowana=random.randint(1,48)
print(wylosowana)
import random
wylosowana=random.randint(1,48)
print(wylosowana)
import random
wylosowana=random.randint(1,48)
print(wylosowana)
import random
wylosowana=random.randint(1,48)
print(wylosowana)



zad5


import random
wylosowana=random.randint(1,49)
print(wylosowana)
wylosowana2=random.randint(1,49)
if wylosowana2!=wylosowana:
    print(wylosowana2)
wylosowana3=random.randint(1,49)
if wylosowana3!=wylosowana:
    print(wylosowana3)
elif wylosowana3!=wylosowana2:
    print(wylosowana3)
wylosowana4=random.randint(1,49)
if wylosowana4!=wylosowana:
    print(wylosowana4)
elif wylosowana4!=wylosowana2:
    print(wylosowana3)
elif wylosowana4!=wylosowana3:
    print(wylosowana4)
wylosowana5=random.randint(1,49)
if wylosowana5!=wylosowana:
    print(wylosowana5)
elif wylosowana5!=wylosowana2:
    print(wylosowana5)
elif wylosowana5!=wylosowana3:
    print(wylosowana5)
elif wylosowana5!=wylosowana4:
    print(wylosowana5)
wylosowana6=random.randint(1,49)
if wylosowana6!=wylosowana:
    print(wylosowana6)
elif wylosowana6!=wylosowana2:
    print(wylosowana6)
elif wylosowana6!=wylosowana3:
    print(wylosowana6)
elif wylosowana6!=wylosowana4:
    print(wylosowana6)
elif wylosowana6!=wylosowana5:
    print(wylosowana6)

'''

#zad6
print("Wpisz wylosowan?? liter?? jak najszybciej.")
import random
literaaa="abcdefghijklmnoprstuwxyzvq"
wylosowanaaa=random.choice(literaaa)
print(wylosowanaaa)
import time
litera2=input()
start=time.clock()
while litera2!=wylosowanaaa:
    litera2=input("Nie wcisn????e?? odpowiedniej litery!\n")
koniec=time.clock()
czas=koniec-start
print("Na wci??ni??cie potrzebowa??e??: ", czas)




#zad8

import time
start=time.clock()
import random
wylosowanka=random.randint(1,99)
while wylosowanka < 90:
    print(wylosowanka)
    wylosowanka=random.randint(1,99)
else:
    print(wylosowanka)
    koniec=time.clock()





#zad9


import random
print("Podaj liczb?? z zakresu od 0 do 100.")
podanaa=int(input())
kompus=random.randint(0,100)
print(kompus)
if podanaa>kompus:
    print("Wygra??e??! :)")
else:
    print("Wygra?? komputer. :(")






#zad10


import random
print("Podaj liczb?? z zakresu od 0 do 100.")
podana=int(input())
kompp=random.randint(podana,100)
print("wylosowana liczba: ", kompp)



#zad11


print("Kamie??= wci??nij 1\npapier= wci??nij 2\nno??yce= wci??nij 3")
znak=int(input())
import random
komp=random.randint(1,3)
print(komp)
if znak==1 and komp==2:
    print("komputer wygra??")
elif znak==1 and komp==3:
    print("Wygra??e??")
elif znak==2 and komp==1:
    print("Wygra??e??")
elif znak==2 and komp==3:
    print("komputer wygra??")
elif znak==3 and komp==1:
    print("komputer wygra??")
elif znak==3 and komp==2:
    print("Wygra??e??")
else:
    print("remis")





#zad12



import time
print("Od ilu zacz???? odlicznie?")
poczatekodliczania=int(input())
while poczatekodliczania!=0:
    poczatekodliczania-=1
    print(poczatekodliczania)
    time.sleep(1)
else:
    print("koniec odliczania")





#zad13


import random
los=random.randint(1,5)
if los==1:
    print("Co ci?? nie zabije, to ci?? wzmocni.")
elif los==2:
    print("I idzie si?? dalej...")
elif los==3:
    print("Fortuna ko??em si?? toczy.")
elif los==4:
    print("??ycie jest pi??kne!")
else:
    print("Love yourself so noone has to.")





#zad14



import random
wartosc=random.random()
print(wartosc)
if wartosc==1:
    print("zdarzenie pewne")
elif wartosc>0.5:
    print("zdarzenie z wysokim prawdopodobie??stwem")
elif wartosc==0:
    print("zdarzenie niemo??liwe")
else:
    print("zdarzenie z niskim prawdopodobie??stwem")
