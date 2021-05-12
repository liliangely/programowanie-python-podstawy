lista=[2,3,4,1]

'''
def sumowanie(listaliczb):
    if len(listaliczb)>0:
        return listaliczb[0] + sumowanie(listaliczb[1:])
    else:
        return 0

wynik=sumowanie(lista)
print(wynik)




def gwiazdki(liczbagwiazdek):
    if liczbagwiazdek>0:
        print("*")
        gwiazdki(liczbagwiazdek-1)

gwiazdki(5)




def ostatni(listaliczb):
    if len(listaliczb)>0:
        return listaliczb[-1]

wynik=ostatni(lista)
print(wynik)




def ogon(listaliczb):
    if len(listaliczb)>0:
        return listaliczb[1:]

wynik=ogon(lista)
print(wynik)



lista.sort()
def max(listaliczb):
    if len(listaliczb)>0:
        return listaliczb[-1]

wynik=max(lista)
print(wynik)

def min(listaliczb):
    if len(listaliczb)>0:
        return listaliczb[0]

wynik=min(lista)
print(wynik)



podany=int(input("Podaj element do sprawdzenia: "))
def sprawdzenie(listaliczb):
    if podany in listaliczb:
        return "tak"
    else:
        return "nie"

wynik=sprawdzenie(lista)
print(wynik)




def sumowanie(liczba1,liczba2):
    suma=liczba1+liczba2
    return suma
podana1=int(input("Podaj liczbę: "))
podana2=int(input("Podaj liczbę: "))
wynik=sumowanie(podana1,podana2)
print(wynik)




def porownywanie(liczba1,liczba2):
    if liczba1==liczba2:
        return "są równe"
    else:
        if liczba1>liczba2:
            return 'nie są równe, różnica: ' , liczba1-liczba2
        else:
            return 'nie są równe, różnica: ' , liczba2-liczba1

podana1=int(input("Podaj liczbę: "))
podana2=int(input("Podaj liczbę: "))
wynik=porownywanie(podana1,podana2)
print(wynik)



def pierwiastkowanie(liczba):
    if liczba%2==0:
        return liczba**(1/2), 'parzysta'
    else:
        return liczba**(1/2), 'nieparzysta'

podana=int(input("Podaj liczbę: "))
wynik=pierwiastkowanie(podana)
print(wynik)
'''
