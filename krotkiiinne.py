import random
import os

#zad3
'''krotka=(2,4,6,8)
print("Podaj cyfrę")
podana=int(input())
if podana in krotka:
    print("jest")
else:
    print("nie ma")


#zad4

tab=(1,2,3,4,8,7,6)
max=0
for i in range(len(tab)):
    if i>max:
        max=i
    else:
        print(max, "to jest max")



#zad5
krotka=(22,11,4,8,78,90,54,15,43,12)
print("Podaj liczbę")
podana=int(input())
print("Elementy:")
for i in range(len(krotka)):
    print(krotka[i],)
print(podana)




#zad6

krotka=(22,11,4,8,78,90,54,15,43,12)
suma=0
for i in range(len(krotka)):
    suma+=krotka[i]
print("Suma: ",suma)
'''





#zad13
ksiazkatel={"Kowal":1234,"X":3333,"Omom":2222,"Pimpek":8888}
while True:
    os.system('cls')
    print("aby wyświetlić książkę wciśnij 'a'")
    print("aby dodać numer wciśnij 'b'")
    print("aby usunąć numer wciśnij 'c'")
    print("aby zmodyfikować numer wciśnij 'd'")
    print("aby wyjść wciśnij 'q'")
    odp=input()
    if odp=='a':
        print(ksiazkatel)
    elif odp=='b':
        nazwisko=input("Podaj nowe nazwisko: ")
        nr=int(input("Podaj nowy numer: "))
        ksiazkatel[nazwisko]=nr
        print(ksiazkatel)
    elif odp=='c':
        print(ksiazkatel)
        print("Które numer usunąć (podaj nazwisko)?")
        usun=input()
        del(ksiazkatel[usun])
        print(ksiazkatel)
    elif odp=='d':
        print(ksiazkatel)
        print("Który numer zmodyfikować (podaj nazwisko)?")
        nazwiskoo=input()
        print("Podaj nowy numer")
        nowynr=int(input())
        ksiazkatel[nazwiskoo]=nowynr
        print(ksiazkatel)
    elif odp=='q':
        break
    else:
        print("błędny znak")
    input()
