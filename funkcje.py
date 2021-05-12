import random
import os
#zad 6
'''
lista=[1,2,3,4,5]
def nta(element):
    nty=random.randint(lista[0],lista[-1])
    return nty
wynik=nta(lista)
print(wynik)


#zad7
def alternatywa(pierwsza,druga):
    if pierwsza==0:
        if druga==0:
            alternatyw=0
        else:
            alternatyw=1
    else:
        alternatyw=1
    return alternatyw
pierw=int(input("Podaj pierwszą zmienną (0 lub 1): "))
drug=int(input("Podaj drugą zmienną (0 lub 1): "))
wynik=alternatywa(pierw,drug)
print("Alternatywa przyjmuje wartość: ", wynik)




#zad8

def koniunkcja(pierwsza,druga):
    if pierwsza==1:
        if druga==1:
            koniunk=1
        else:
            koniunk=0
    else:
        koniunk=0
    return koniunk
pierw=int(input("Podaj pierwszą zmienną (0 lub 1): "))
drug=int(input("Podaj drugą zmienną (0 lub 1): "))
wynik=koniunkcja(pierw,drug)
print("Koniunkcja przyjmuje wartość: ", wynik)


#zad9
def implikacja(pierwsza,druga):
    if pierwsza==1:
        if druga==0:
            impli=0
        else:
            impli=1
    else:
        impli=1
    return impli
pierw=int(input("Podaj pierwszą zmienną (0 lub 1): "))
drug=int(input("Podaj drugą zmienną (0 lub 1): "))
wynik=implikacja(pierw,drug)
print("Implikacja przyjmuje wartość: ", wynik)


#zad10
while True:
    os.system('cls')
    print("Jeśli chcesz obliczyć kwadrat wciśnij 'k'")
    print("Jeśli chcesz obliczyć sześcian wciśnij 's'")
    print("Jeśli chcesz wyjść wciśnij 'q'")
    odp=input()
    if odp=='k':
        def obliczaniekwadratu(liczba1):
            kwadrat=liczba1**2
            return kwadrat
        podanaliczba1=int(input("Podaj liczbę: "))
        wynik1=obliczaniekwadratu(podanaliczba1)
        print(wynik1)
    elif odp=='s':
        def obliczanieszescianu(liczba2):
            szescian=liczba2**3
            return szescian
        podanaliczba2=int(input("Podaj liczbę: "))
        wynik2=obliczanieszescianu(podanaliczba2)
        print(wynik2)
    elif odp=='q':
        break
    else:
        print("Błędny znak.")
    input()




#zad11
def dzientygodnia(liczba):
    if liczba==1:
        dzien="Poniedziałek"
    elif liczba==2:
        dzien="Wtorek"
    elif liczba==3:
        dzien="Środa"
    elif liczba==4:
        dzien="Czwartek"
    elif liczba==5:
        dzien="Piątek"
    elif liczba==6:
        dzien="Sobota"
    elif liczba==7:
        dzien="Niedziela"
    return dzien
podanynumerdnia=int(input("Podaj numer dnia tygodnia: "))
wynik=dzientygodnia(podanynumerdnia)
print(wynik)


#zad12
def gwiazdki(liczba):
    for i in range(liczba):
        print("*")
    return "Oto twoje gwiazdki"
podanaliczbagwiazdek=int(input("Podaj liczbę gwiazdek: "))
wynik=gwiazdki(podanaliczbagwiazdek)
print(wynik)


#zad13
def sprawdzenieparzystosci(liczba):
    if liczba%2==0:
        sprawdzenie="parzysta"
    else:
        sprawdzenie="nieparzysta"
    return sprawdzenie
podanaliczba=int(input("Podaj liczbę: "))
wynik=sprawdzenieparzystosci(podanaliczba)
print(wynik)


#zad14
def sumowanie(liczba):
    suma=0
    zliczanie=0
    while zliczanie!=liczba:
        zliczanie+=1
        suma+=zliczanie
    return suma
podanaliczba=int(input("Podaj liczbę: "))
wynik=sumowanie(podanaliczba)
print(wynik)


#zad15


while True:
    os.system('cls')
    print("Teraz nastąpi losowanie funkcji. \nJeśli się zgadzasz wciśnij 'z'. \nJeśli chcesz to przerwać wciśnij 'e'")
    odp=input()
    if odp=='z':
        wylosowana=random.randint(0,4)
        if wylosowana==0:
            print("Funkcja sumowania")
            def sumowanie(liczba):
                suma=0
                zliczanie=0
                while zliczanie!=liczba:
                    zliczanie+=1
                    suma+=zliczanie
                return suma
            podanaliczba=int(input("Podaj liczbę: "))
            wynik=sumowanie(podanaliczba)
            print(wynik)
        elif wylosowana==1:
            print("Funkcja sprawdzania parzystości")
            def sprawdzenieparzystosci(liczba):
                if liczba%2==0:
                    sprawdzenie="parzysta"
                else:
                    sprawdzenie="nieparzysta"
                return sprawdzenie
            podanaliczba=int(input("Podaj liczbę: "))
            wynik=sprawdzenieparzystosci(podanaliczba)
            print(wynik)
        elif wylosowana==2:
            print("Funkcja dni tygodnia")
            def dzientygodnia(liczba):
                if liczba==1:
                    dzien="Poniedziałek"
                elif liczba==2:
                    dzien="Wtorek"
                elif liczba==3:
                    dzien="Środa"
                elif liczba==4:
                    dzien="Czwartek"
                elif liczba==5:
                    dzien="Piątek"
                elif liczba==6:
                    dzien="Sobota"
                elif liczba==7:
                    dzien="Niedziela"
                return dzien
            podanynumerdnia=int(input("Podaj numer dnia tygodnia: "))
            wynik=dzientygodnia(podanynumerdnia)
            print(wynik)
        elif wylosowana==3:
            while True:
                os.system('cls')
                print("Jeśli chcesz obliczyć kwadrat wciśnij 'k'")
                print("Jeśli chcesz obliczyć sześcian wciśnij 's'")
                print("Jeśli chcesz wyjść wciśnij 'q'")
                odp=input()
                if odp=='k':
                    def obliczaniekwadratu(liczba1):
                        kwadrat=liczba1**2
                        return kwadrat
                    podanaliczba1=int(input("Podaj liczbę: "))
                    wynik1=obliczaniekwadratu(podanaliczba1)
                    print(wynik1)
                elif odp=='s':
                    def obliczanieszescianu(liczba2):
                        szescian=liczba2**3
                        return szescian
                    podanaliczba2=int(input("Podaj liczbę: "))
                    wynik2=obliczanieszescianu(podanaliczba2)
                    print(wynik2)
                elif odp=='q':
                    break
                else:
                    print("Błędny znak.")
                input()
        else:
            print("Funkcja losowanie elementu")
            lista=[1,2,3,4,5]
            def nta(element):
                nty=random.randint(lista[0],lista[-1])
                return nty
            wynik=nta(lista)
            print(wynik)
    elif odp=='e':
        break
    else:
        print("Błędny znak.")
    input()
'''




#zad16

pobranaliczba=int(input("Podaj liczbę: "))

def sprawdz_dol(liczba):
    if liczba>10:
        sprawdzenie="Twoja liczba jest większa od 10."
    else:
        sprawdzenie="Twoja liczba nie jest większa od 10."
    return sprawdzenie
wynik_sprawdz_dol=sprawdz_dol(pobranaliczba)
print(wynik_sprawdz_dol)

def sprawdz_gore(liczba):
    if liczba<100:
        sprawdzenie2="Twoja liczba jest mniejsza od 100."
    else:
        sprawdzenie2="Twoja liczba nie jest mniejsza od 100."
    return sprawdzenie2
wynik_sprawdz_gore=sprawdz_gore(pobranaliczba)
print(wynik_sprawdz_gore)

def pierwiastkuj(liczba):
    pierwiastek=liczba**(1/2)
    return pierwiastek
wynik_pierwiastkowanie=pierwiastkuj(pobranaliczba)
print("Pierwiastek z twojej liczby: ",wynik_pierwiastkowanie)

def dodaj_dwa(liczba4):
    dodawanie=liczba4+2
    return dodawanie
wynik_dodawanie=dodaj_dwa(wynik_pierwiastkowanie)
print("Twoja spierwiastkowana liczba plus dwa: ",wynik_dodawanie)

def do_potegi(liczba5):
    potega=liczba5**2
    return potega
wynik_potega=do_potegi(wynik_dodawanie)
print("Następnie potęguję i Twoja liczba wygląda teraz tak: ",wynik_potega)

def wyswietl(liczba6):
    wyswietlenie="Twoja liczba po wykonaniu działań: ",liczba6,"Twoja liczba przed wykonaniem działań: ",pobranaliczba
    return wyswietlenie
wynik_ostateczny=wyswietl(wynik_potega)
print(wynik_ostateczny)
