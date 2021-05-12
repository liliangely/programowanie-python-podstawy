'''print("Podaj pierwszą liczbę")
liczba1=int(input())
print("Podaj drugą liczbę")
liczba2=int(input())
if liczba1>liczba2:
    print("Pierwsza liczba jest większa.")
else:
    print("Druga liczba jest większa.")



print("Podaj liczbę")
liczba1=int(input())
print("Podaj następną liczbę")
liczba2=int(input())
print("Podaj następną liczbę")
liczba3=int(input())
print("Podaj następną liczbę")
liczba4=int(input())
print("Podaj następną liczbę")
liczba5=int(input())
if liczba1>liczba2:
    if liczba1>liczba3:
        if liczba1>liczba4:
            if liczba1>liczba5:
                print("Pierwsza liczba jest największa.")
elif liczba2>liczba3:
    if liczba2>liczba4:
        if liczba2>liczba5:
            print("Druga liczba jest największa.")
elif liczba3>liczba4:
    if liczba3>liczba5:
        print("Trzecia liczba jest największa.")
elif liczba4>liczba5:
    print("Czwarta liczba jest największa.")
else:
    print("Piąta liczba jest największa.")




print("Podaj liczbę punktów z testu")
liczpun=float(input())
if liczpun<=5:
    print("ndst")
elif liczpun<=7:
    print("dst")
elif liczpun<=7.5:
    print("dst+")
elif liczpun<=8:
    print("db")
elif liczpun<=9:
    print("db+")
else:
    print("bdb")





print("Podaj nazwę użytkownika")
uzytkownik=input()
print("Podaj dwukrotnie hasło")
haslo=input()
haslo2=input()
if haslo==haslo2:
    print("Czy masz 18 lat?")
    odpnapyt=input()
    if odpnapyt=="nie":
        print("Masz zgodę rodziców?")
        odpnapyt2=input()
        if odpnapyt2=="tak":
            print("Konto założone!")
            print("Czy chcesz konto superużytkownika?")
            kontosuper=input()
            if kontosuper=="tak":
                print("Superkonto założone!")
            else:
                print("Dlaczego?")
                odpwhy=input()
        else:
            print("Nie możesz założyć konta.")
    else:
        print("Możesz założyć konto!")
        print("Czy chcesz konto superużytkownika?")
        kontosuper=input()
        if kontosuper=="tak":
            print("Superkonto założone!")
        else:
            print("Dlaczego?")
            odpwhy=input()

else:
    print("Hasła niezgodne :(")
















print("Podaj liczbę")
liczba=float(input())
if liczba>=0:
    print("Wartość bezwzględna= ", liczba)
else:
    liczbamniejszaodzera=liczba*-1
    print("Wartość bezwzględna= ", liczbamniejszaodzera)
'''







print("Podaj liczbę")
liczbap=int(input())
if liczbap%2==0:
    print("liczba parzysta")
    print("wynik dzielenia przez 2= ", liczbap/2)
else:
    print("liczba nieparzysta")
    if liczbap>10:
        print("liczba jest duża")
    else:
        print("liczba jest mała")
