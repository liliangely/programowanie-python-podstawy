import random
import os
'''cyfratrzy=["III",3,"three","trzy","..."]
pustalista=[]
print(cyfratrzy[0])
print(cyfratrzy[4])


print("rozne oblicza cyfry trzy")
for i in range(5):
    print(cyfratrzy[i])


print(cyfratrzy[2:4])


print("liczba elementow:", len(cyfratrzy))



lista=[1,2,3]

print("Podaj nową zawartość 0 elementu")
lista[0]=int(input())
print("\nNowa lista:")
for i in range(len(lista)):
    print(lista[i])

for i in range(len(lista)):
    print("Podaj zawartość",i,"elementu")
    lista[i]=input()
print("\nNowa lista:")
for i in range(len(lista)):
    print(lista[i])


dodaj=input("Jaki element dodać?")
lista.append(dodaj)
for i in range(len(lista)):
    print(lista[i])

lista=[1,2,3]
usun=int(input("Jaki element usunąć?"))
lista.remove(usun)
for i in range(len(lista)):
    print(lista[i])


lista1=[1,2,3,2,3,4,2]
lista2=lista1[:]
lista1[0]=8
print(lista1)
print(lista2)



wyniki=[1000,3,2345,687]
for i in wyniki:
    print(i)
print("sortowanie pierwsze:")
wyniki.sort()
for i in wyniki:
    print(i)
print("sortowanie drugie:")
wyniki.sort(reverse=True)
for i in wyniki:
    print(i)











#zad1
przedmioty=("polski","matematyka","angielski")
oceny=[]
suma=0
for i in range(len(przedmioty)):
	print("Podaj ocenę z przedmiotu w kolejności: polski, matematyka, angielski")
	ocena=int(input())
	oceny.append(ocena)
	print("ocena z", przedmioty[i], "wynosi", ocena)
	suma+=oceny[i]
srednia=suma/3
print("Twoja srednia to:", srednia)



#zad2
lista=[]

for i in range(9,-1,-1):
	lista.append(i)
print(lista)


#zad3
lista=[]
suma=0
for i in range(0,101):
    losowa=random.randint(0,9)
    lista.append(losowa)
print(lista)
for j in lista:
    if j==7:
        suma+=1
print("cyfra 7 pojawiła się: ",suma, "razy")



#zad4
lista=[]
for i in range(0,101):
    losowa=random.randint(0,9)
    lista.append(losowa)
print(lista)

lista.reverse()
print("odwrócona lista: ",lista)


#zad5
print("Ile cyfr pobrać?")
ilosccyfr=int(input())
zliczanie=0
lista=[]
while zliczanie!=ilosccyfr:
    losowe=random.randint(0,9)
    lista.append(losowe)
    zliczanie+=1
print(lista)
for i in range(len(lista)):
    if lista[i]%2==0:
        print("parzysta:", lista[i])
    else:
        print("nieparzysta:", lista[i])


#zad6
lista=[]
for i in range(50):
    element=0
    lista.append(element)
for i in range(len(lista)):
    if i%2==0:
        lista[i]=2
    if i%3==0:
        lista[i]=3
    if i%5==0:
        lista[i]=5
for i in lista[:]:
    if i==0:
        lista.remove(i)
print(lista)
print("Posortowana lista: ")
lista.sort()
print(lista)
print("liczba elementów: ",len(lista))




#zad7

lista=[]
for i in range(20):
    wylos=random.randint(0,90)
    lista.append(wylos)
print(lista)
for i in lista[:]:
    if i>50:
        lista.remove(i)
print(lista)




#zad8
lista=[]
liczenie=0
for i in range(20):
    wylos=random.randint(0,99)
    liczenie+=wylos
    lista.append(wylos)
print(lista)
najw=0
najmn=99
for i in lista[:]:
    if i>najw:
        najw=i
    if i<najmn:
        najmn=i
srednia=liczenie/20
print("Największy: ",najw)
print("Najmniejszy: ", najmn)
print("Średnia elementów: ",srednia)




#zad9

listalos=[]
for i in range(0,7):
    print(i)
    wylosowana=random.random()
    zaokraglona=round(wylosowana,2)
    listalos.append(zaokraglona)

lista=[]
nr=[0,1,2,3,4,5,6]
print("+---+------+")
for i in range(len(lista)):
	los=random.random()
    zaokraglona=round(los,2)
    lista.append(zaokraglona)
	print("|",nr[i],"|",lista[i],"|")
print("+---+------+")




#zad10
imiona=["A","B","C","D","E","F","G","H"]
zawod=["wojak","policjant","rabus","tancerz"]
print(zawod[:])
print("Jaki zawód wyświetlić?")
wyswietl=input()
wojak=imiona[:1]
policjant=imiona[1:3]
rabus=imiona[3:6]
tancerz=imiona[6:]
if wyswietl=="wojak":
    print(wojak)
elif wyswietl=="policjant":
    print(policjant)
elif wyswietl=="rabus":
    print(rabus)
elif wyswietl=="tancerz":
    print(tancerz)
else:
    print("błędny znak")




#zad11
imiona=["Ania","Basia","Cezary","Danuta","Elka","Felix","Gienio","Heniek"]
zarobki=[600,800,1000,1200,1800,2000,3000,4000]
print("Lista: ")
while True:
    os.system('cls')
    print("Aby wyświetlić imiona i zarobki, wciśnij 'a'")
    print("Aby dodać do listy, wciśnij 'b'")
    print("Aby wyjść wciśnij, 'q'")
    odp=input()
    if odp=='a':
        for i in range(len(imiona)):
            print(imiona[i],"\t",zarobki[i])
    elif odp=='b':
        dodimie=input("Podaj imię: ")
        dodzarobki=int(input("Podaj zarobki: "))
        imiona.append(dodimie)
        zarobki.append(dodzarobki)
        for i in range(len(imiona)):
            print(imiona[i],"\t",zarobki[i])
    elif odp=='q':
        break
    else:
        print("błędny znak")
    input()




#zad12

imiona=["Ania","Basia","Cezary","Danuta","Elka","Felix","Gienio","Heniek"]
zarobki=[600,1000,800,3000,2000,1800,2600,4000]

for i in range(len(zarobki)):
    for j in range(len(zarobki)):
        if zarobki[i]<zarobki[j]:
           pola=zarobki[j]
           zarobki[j]=zarobki[i]
           zarobki[i]=pola
           pola2=imiona[j]
           imiona[j]=imiona[i]
           imiona[i]=pola2

for i in range(len(imiona)):
    print(imiona[i],"\t",zarobki[i])





#zad13
lista=[]
for i in range(30):
    losowa=random.random()+3
    zaokraglona=round(losowa,2)
    lista.append(zaokraglona)
for i in range(len(lista)):
    print(lista[i])
'''
#cyfry=[0,0,0,0]
#cyfry.insert(2,5)
#print(cyfry)


#zad14

'''
while True:
    print("Aby wyświetlić listę wciśnij 'a'")
    print("Aby dodać graczy wciśnij 'b'")
    print("Aby poprawić wciśnij 'c'")
    print("Aby wyjść wciśnij 'q'")
    listaimie=[]
    listawynik=[]
    wyboropcji=input()
    if wyboropcji=='b':
        print("Ilu graczy?")
        odpilegraczy=int(input())
        sumka=0
        while odpilegraczy!=sumka:
            imie=input("Podaj imię gracza: ")
            wynik=float(input("Podaj wynik gracza: "))
            listaimie.append(imie)
            listawynik.append(wynik)
            sumka+=1
        for i in range(len(listaimie)):
            print(listaimie[i],"\t",listawynik[i])
    elif wyboropcji=='a':
        for i in range(len(listaimie)):
            print(listaimie[i],"\t",listawynik[i])
    elif wyboropcji=='c':
        print("Jeśli chcesz poprawić imię wciśnij 'i', a jeśli chcesz poprawić wynik wciśnij 'w'")
        wyborpoprawa=input()
        if wyborpoprawa=='i':
            for i in listaimie:
                print(i)
            poprawaimiewybor=int(input("Który element (licząc od 0) chcesz poprawić?"))
            poprawaimiewybor2=str(input("Wpisz imię, które ma błąd: "))
            listaimie.remove(poprawaimiewybor2)
            print("Podaj nowe imię ")
            poprawaimie=str(input())
            listaimie.insert(poprawaimiewybor,poprawaimie)
            print(listaimie)
        elif wyborpoprawa=='w':
            for i in listawynik:
                print(i)
            poprawawynikwybor=int(input("Który element (licząc od 0) chcesz poprawić?"))
            poprawaimiewybor2=str(input("Wpisz wartość, która ma błąd: "))
            listawynik.remove(poprawawynikwybor2)
            print("Podaj nowy wynik ")
            poprawawynik=input()
            listawynik.insert(poprawawynikwybor,poprawawynik)
            print(listawynik)
        else:
            print("błędny znak")
    elif wyboropcji=='q':
        break
    else:
        print("błędny znak")
'''

import os
imie=[]
wynik=[]
while True:
    print("Aby dodać imie i wynik, wciśnij d")
    print("Jeśli chcesz wyświetlić wyniki z listy wciśnij w")
    print("Jeśli chcesz poprawić błąd w imieniu, wciśnij p")
    print("Jeśli chcesz poprawić bład w wyniku, wciśnij y")
    print("Aby zakończyć program, wciśnij z")
    decyzja=str(input())
    if decyzja=="d":
        os.system("cls")
        print("Wprowadz ilu graczy bedzie w liscie")
        ilosc=int(input())
        for i in range(0,ilosc):
            imieu=str(input())
            limie=[imieu]
            imie.extend(limie)
            wyniku=int(input())
            lwynik=[wyniku]
            wynik.extend(lwynik)
    elif decyzja == "w":
        os.system("cls")
        for i in range(len(imie)):
            print(imie[i],wynik[i])
    elif decyzja == "p":
         os.system("cls")
         for i in range(len(imie)):
            print(i,imie[i],wynik[i])
         print("Podaj w którym rzędzie jest błąd")
         blad2=int(input())
         print("Wpisz wartośc która ma błąd")
         blad=str(input())
         imie.remove(blad)
         print("Wpisz poprawną wartość, miejsce w którym znajduje się bład")
         poprawa=str(input())
         imie.insert(blad2,poprawa)
         print(imie[i],wynik[i])
    elif decyzja=="y":
         os.system("cls")
         for i in range(len(wynik)):
            print(i,imie[i],wynik[i])
         print("Podaj w którym rzędzie jest błąd")
         blad3=int(input())
         print("Wpisz wartośc która ma błąd")
         blad4=int(input())
         wynik.remove(blad4)
         print("Wpisz poprawną wartość, miejsce w którym znajduje się bład")
         poprawa1=int(input())
         wynik.insert(blad3,poprawa1)
         print(imie[i],wynik[i])

    elif decyzja=="z":
        break
