'''def wpisaniezawartosci(nazwapliku,tekst):
    pliktekstowy=open(nazwapliku, 'w')
    pliktekstowy.write(tekst)
    pliktekstowy.close()

nazwapliku="test.txt"
zawartosc='blah blah'
wpisaniezawartosci(nazwapliku,zawartosc)


def odczytzawartosci(nazwaplik):
    plik_tekstowy=open(nazwaplik,'r')
    print(plik_tekstowy.read(znaki))
    plik_tekstowy.close()

nazwaplik="test.txt"
znaki= int(input("Podaj ilość znaków: "))
odczytzawartosci(nazwaplik)



def odczytzawartosci(nazwapliku,znaki):
    pliktekstowy=open(nazwapliku,'r')
    ciagznakow=pliktekstowy.read(znaki)
    pliktekstowy.close()
    return ciagznakow

nazwapliku="test.txt"
odp=int(input("Ile znaków wczytać? "))
slowo=odczytzawartosci(nazwapliku,odp)
print("Odczytałam treść: ",slowo)



def odczytzawartosci(nazwapliku):
    pliktekstowy=open(nazwapliku, 'r')
    for linia in pliktekstowy:
        print(linia)


nazwapliku="test.txt"
odczytzawartosci(nazwapliku)




def dodaniedolisty():
    lista=[]
    for i in range(3):
        print("Podaj zawartość", i, "linii tekstu: ")
        linia=input()
        lista.append(linia + "\n" )
    return lista

def wpisaniezawartosci(nazwapliku):
    pliktekstowy=open(nazwapliku, 'w')
    tekst=dodaniedolisty()
    pliktekstowy.writelines(tekst)
    pliktekstowy.close()

nazwapliku="test.txt"
wpisaniezawartosci(nazwapliku)





def wpisaniezawartosci(nazwapliku):
    pliktekstowy=open(nazwapliku, 'w')
    pliktekstowy.writelines("EMO AT HEART")
    pliktekstowy.close()

print("Podaj nazwę pliku: ")
nazwa=input()
wpisaniezawartosci(nazwa)




def zamianatekstu(nazwapliku,tekstpierwotny, tekstkoncowy):
    zrodlo=open(nazwapliku).readlines()
    cel=open('test.txt', 'w')
    for s in zrodlo:
        cel.write(s.replace(tekstpierwotny, tekstkoncowy))
    cel.close()

nazwapliku="test.txt"
co=input("Co zamienić? ")
naco=input("Na co zamienić? ")
zamianatekstu(nazwapliku,co,naco)




import os

def tworzeniekatalogu(nazwakatalogu):
    if not os.path.exists(nazwakatalogu):
        os.makedirs(nazwakatalogu)

sciezka='C:\\Users\\dell\\Desktop\\PR\\'
nazwa=input("Podaj nazwe katalogu: ")
tworzeniekatalogu(sciezka + nazwa)





#zad 1 i 2

import os.path
import os
import random
def tworzeniepliku(folder):
    save_path = folder
    for i in range(50):
        alfabet = "abcdefghijklmnoprstuwyz"
        lista = [ ]
        los=random.randrange(20)
        for i in range(0,los):
            litera = random.choice(alfabet)
            lista.append(litera)
            ciag_znakow = "".join(lista)
        name_of_file = ciag_znakow
        completeName = os.path.join(save_path, name_of_file+".txt")
        file1 = open(completeName, "w")
        file1.close()

folder="C:\\Users\\dell\\Desktop\\PR\\"+input(("wpisz nazwe folderu"))
if not os.path.exists(folder):
    os.makedirs(folder)
tworzeniepliku(folder)




#zad3

import os
import random

def tworzeniekatalogu(nazwakatalogu):
    if not os.path.exists(nazwakatalogu):
        os.makedirs(nazwakatalogu)

    for i in range(50):
        def wpisaniezawartosci(nazwapliku):
            alfabet = "abcdefghijklmnoprstuwyz"
            losowa=random.choice(alfabet)
            pliktekstowy=open(nazwapliku, 'w')
            pliktekstowy.writelines(losowa)
            pliktekstowy.close()


sciezka='C:\\Users\\dell\\Desktop\\PR\\'
tworzeniekatalogu(sciezka)
'''


#zad4


def wpisaniezawartosci(nazwapliku,tekst):
    pliktekstowy=open(nazwapliku, 'w')
    pliktekstowy.write(tekst)
    pliktekstowy.close()

nazwapliku=input("Podaj nazwę pliku: ")
zawartosc=input("Podaj zawartość pliku: ")
wpisaniezawartosci(nazwapliku,zawartosc)


def odczytzawartosci(nazwaplik):
    plik_tekstowy=open(nazwaplik,'r')
    print(plik_tekstowy.read(znaki))
    plik_tekstowy.close()

nazwaplik=nazwapliku
znaki= int(input("Podaj ilość znaków: "))
odczytzawartosci(nazwaplik)



def nazwanienowego(nazwaplikuu):
    pliktekstowy=open(nazwapliku, 'w')
    pliktekstowy.close()

nazwaplikuu=input("Podaj nazwę nowego pliku: ")
nazwanienowego(nazwaplikuu)



def zamianatekstu(nazwaplika):
    zrodlo=open(nazwaplika).readlines()
    cel=open(nazwaplikuu, 'w')
    for s in zrodlo:
        zamiana1= s.replace("a","4")
        zamiana2=zamiana1.replace("b","8")
        cel.write(zamiana2)
    cel.close()


zamianatekstu(nazwapliku)
