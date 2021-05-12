import os

'''class telewizor:
    kanaly=["tvp1","tvp2","polsat","tv4","tvn"]
    def listakanalow(self):
        for i in self.kanaly:
            print(i)

mojtv=telewizor()
mojtv.listakanalow() #wyswietlanie


class telewizor:
    kanaly=["tvp1","tvp2","polsat","tv4","tvn"]
    nrkanal=0

    def __init__(self):
        print("tv wlaczony")
        print("ustawiony kanal: ", self.kanaly[self.nrkanal])

    def listakanalow(self):
        for i in self.kanaly:
            print(i)

mojtv=telewizor()
mojtv.listakanalow()



class telewizor:
    kanaly=["tvp1","tvp2","polsat","tv4","tvn"]
    nrkanal=0

    def __init__(self):
        print("ustawiony kanal: ", self.kanaly[self.nrkanal])

    def ustawkanal(self,wpisanykanal):
        self.nrkanal=wpisanykanal

    def wyswietlkanal(self):
        print("ustawiony kanal: ", self.kanaly[self.nrkanal])

mojtv=telewizor()
nowykanal=int(input("Jaki kanał włączyć? "))
mojtv.ustawkanal(nowykanal)
mojtv.wyswietlkanal()




#zad 1
class telewizor:
    kanaly=["tvp1","tvp2","polsat","tv4","tvn"]
    nrkanal=0
    glos=0

    def __init__(self):
        print("ustawiony kanal: ", self.kanaly[self.nrkanal])

    def ustawkanal(self,wpisanykanal):
        self.nrkanal=wpisanykanal

    def wyswietlkanal(self):
        print("ustawiony kanal: ", self.kanaly[self.nrkanal])

    def ustawglos(self,wpisanaglosnosc):
        self.glos=wpisanaglosnosc

    def wyswietlkanaly(self):
        for i in self.kanaly:
            print(i)



mojtv=telewizor()
mojtv.wyswietlkanaly()
nowykanal=int(input("Jaki kanał włączyć? "))
mojtv.ustawkanal(nowykanal)
mojtv.wyswietlkanal()
nowaglosnosc=int(input("Ustaw głos: "))

for i in range(100):
    if nowaglosnosc>=0 and nowaglosnosc<=20:
        mojtv.ustawglos(nowaglosnosc)
    else:
        print("glosnosc wykracza poza mozliwosci twojego tv, wpisz liczbe od 0 do 20")
        nowaglosnosc=int(input("Ustaw glos: "))


print("aby przeskoczyc w gore wcisnij '1', aby przeskoczyc w dol wcisnij '0'")
odp=int(input())
if odp==1:
    if nowykanal==4:
        nowykanal=0
        mojtv.ustawkanal(nowykanal)
        mojtv.wyswietlkanal()
    else:
        nowykanal+=1
        mojtv.ustawkanal(nowykanal)
        mojtv.wyswietlkanal()

elif odp==0:
    nowykanal-=1
    mojtv.ustawkanal(nowykanal)
    mojtv.wyswietlkanal()
else:
    print("człeku co ty wciskasz?!?!?!?!")


#zad3
while True:
    os.system('cls')
    class telewizor:
        kanaly=["tvp1","tvp2","polsat","tv4","tvn"]
        nrkanal=0
        glos=0

        #def __init__(self):
        #    print("ustawiony kanal: ", self.kanaly[self.nrkanal])

        def ustawkanal(self,wpisanykanal):
            self.nrkanal=wpisanykanal

        def wyswietlkanal(self):
            print("ustawiony kanal: ", self.kanaly[self.nrkanal])

        def ustawglos(self,wpisanaglosnosc):
            self.glos=wpisanaglosnosc

        def wyswietlkanaly(self):
            for i in self.kanaly:
                print(i)

    print("aby wyświetlić kanaly wcisnij 'w'")
    print("aby zmienic kanal wcisnij 'z'")
    print("aby przeskoczyc wcisnij 'p'")
    print("aby ustawic glosnosc wcisnij 'g'")
    print("aby wyjsc wcisnij 'q'")
    literka=input()
    if literka=='w':
        mojtv=telewizor()
        mojtv.wyswietlkanaly()
    elif literka=='z':
        nowykanal=int(input("Jaki kanał włączyć? "))
        mojtv.ustawkanal(nowykanal)
        mojtv.wyswietlkanal()
    elif literka=='p':
        print("aby przeskoczyc w gore wcisnij '1', aby przeskoczyc w dol wcisnij '0'")
        odp=int(input())
        if odp==1:
            if nowykanal==4:
                nowykanal=0
                mojtv.ustawkanal(nowykanal)
                mojtv.wyswietlkanal()
            else:
                nowykanal+=1
                mojtv.ustawkanal(nowykanal)
                mojtv.wyswietlkanal()

        elif odp==0:
            nowykanal-=1
            mojtv.ustawkanal(nowykanal)
            mojtv.wyswietlkanal()
        else:
            print("człeku co ty wciskasz?!?!?!?!")
    elif literka=='g':
        nowaglosnosc=int(input("Ustaw głos: "))

        for i in range(100):
            if nowaglosnosc>=0 and nowaglosnosc<=20:
                mojtv.ustawglos(nowaglosnosc)
            else:
                print("glosnosc wykracza poza mozliwosci twojego tv, wpisz liczbe od 0 do 20")
                nowaglosnosc=int(input("Ustaw glos: "))
    elif literka=='q':
        break
    else:
        print("błędny znak")
    input()




#zad7
class prostokat:

    def poleprostokata(self,podanybok1,podanybok2):
        print("pole prostokata wynosi: ",podanybok1*podanybok2)

mojprostokat=prostokat()
bok1=int(input("ile ma bok a? "))
bok2=int(input("ile ma bok b? "))
mojprostokat.poleprostokata(bok1,bok2)
'''
