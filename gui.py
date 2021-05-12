from tkinter import *
from tkinter import messagebox

#przycisk i wyswietlanie w cmd
'''
def akcjaprzycisk():
    print("czesc")

glowneokno=Tk()
glowneokno.title("moje okno")
glowneokno.geometry("300x250")
przycisk1=Button(glowneokno, text="powitanie", command=akcjaprzycisk)
przycisk1.grid()
glowneokno.mainloop()


#przycisk i nowe okno
def akcjaprzycisk():
    messagebox.showinfo("okno zagrozenie", "zagrozenie pozarowe")

glowneokno=Tk()
glowneokno.title("moje okno")
glowneokno.geometry("300x250")
przycisk1=Button(glowneokno, text="nie wciskaj", command=akcjaprzycisk)
przycisk1.grid()
glowneokno.mainloop()



#pole tekstowe
def akcjaprzycisk():
    messagebox.showinfo("okno zagrozenie", poletekstowe.get())

glowneokno=Tk()
glowneokno.title("moje okno")
glowneokno.geometry("300x250")
opispolatekstowego=Label(glowneokno, text="wpisz cos")
opispolatekstowego.pack(side=LEFT)
poletekstowe=Entry(glowneokno)
poletekstowe.pack(side=RIGHT)
przycisk1=Button(glowneokno, text="nie wciskaj", command=akcjaprzycisk)
przycisk1.pack(side=BOTTOM)
glowneokno.mainloop()



#radiobutton 1 przycisk
glowneokno=Tk()
wartosc=IntVar()

def akcjaprzycisk():
    if wartosc.get()==1:
        messagebox.showinfo("magiczne okno", "uwaga")
    if wartosc.get()==2:
        messagebox.showinfo("magiczne okno", "zagrozenie pozarowe")

rprzycisk1=Radiobutton(glowneokno, text="nie klikaj", variable=wartosc, value=1)
rprzycisk1.pack()
rprzycisk2=Radiobutton(glowneokno, text="tutaj tez nie klikaj", variable=wartosc, value=2)
rprzycisk2.pack()
przycisk=Button(glowneokno, text="AAAAAAA!!!", command=akcjaprzycisk)
przycisk.pack()
glowneokno.mainloop()




#radiobutton niezalezne przyciski
glowneokno=Tk()
zad1=IntVar()
zad2=IntVar()

def akcjaprzycisk():
    if zad1.get()==1:
        messagebox.showinfo("magiczne okno", "uwaga")
    if zad2.get()==2:
        messagebox.showinfo("magiczne okno", "zagrozenie pozarowe")

rprzycisk1=Radiobutton(glowneokno, text="nie klikaj", variable=zad1, value=1)
rprzycisk1.pack()
rprzycisk2=Radiobutton(glowneokno, text="tutaj tez nie klikaj", variable=zad1, value=2)
rprzycisk2.pack()
rprzycisk1=Radiobutton(glowneokno, text="nie klikaj tu znowu", variable=zad2, value=1)
rprzycisk1.pack()
rprzycisk2=Radiobutton(glowneokno, text="uwazaj bo wybuchnie", variable=zad2, value=2)
rprzycisk2.pack()
przycisk=Button(glowneokno, text="AAAAAAA!!!", command=akcjaprzycisk)
przycisk.pack()
glowneokno.mainloop()








#zad1
def akcjaprzycisk1():
    messagebox.showinfo("okno zagrozenie", "zagrozenie pozarowe")
def akcjaprzycisk2():
    messagebox.showinfo("okno loser", "jesteś loserem")
def akcjaprzycisk3():
    messagebox.showinfo("okno nicość", "nicość")

glowneokno=Tk()
glowneokno.title("moje okno")
glowneokno.geometry("300x250")

przycisk1=Button(glowneokno, text="nie wciskaj", command=akcjaprzycisk1)
przycisk1.grid()
przycisk2=Button(glowneokno, text="wcisnij", command=akcjaprzycisk2)
przycisk2.grid()
przycisk3=Button(glowneokno, text="chcesz wcisnąć?", command=akcjaprzycisk3)
przycisk3.grid()
glowneokno.mainloop()






#zad2

glowneokno=Tk()
wartosc=IntVar()

def akcjaprzycisk():
    if wartosc.get()==1:

    if wartosc.get()==2:

    if wartosc.get()==3:


przycisk=Button(glowneokno, text="przycisk", command=akcjaprzycisk)
przycisk.pack()

rprzycisk1=Radiobutton(glowneokno, text="wybor 1", variable=wartosc, value=1)
rprzycisk1.pack()
rprzycisk2=Radiobutton(glowneokno, text="wybor 2", variable=wartosc, value=2)
rprzycisk2.pack()
rprzycisk3=Radiobutton(glowneokno, text="wybor 3", variable=wartosc, value=3)
rprzycisk3.pack()

glowneokno.mainloop()




#zad3
def akcjaprzycisk1():
    messagebox.showinfo("okno", "zagrozenie pozarowe")
def akcjaprzycisk2():
    messagebox.showinfo("okno", "zagrozenie")
def akcjaprzycisk3():
    messagebox.showinfo("okno", "pozarowe")

glowneokno=Tk()
glowneokno.title("moje okno")
glowneokno.geometry("300x250")

przycisk1=Button(glowneokno, text="wcisnij aby zmienic1", command=akcjaprzycisk1)
przycisk1.grid()
przycisk2=Button(glowneokno, text="wcisnij aby zmienic2", command=akcjaprzycisk2)
przycisk2.grid()
przycisk3=Button(glowneokno, text="wcisnij aby zmienic3", command=akcjaprzycisk3)
przycisk3.grid()
glowneokno.mainloop()




#zad4


def akcjaprzycisk():
    pierwszazmienna=float(poletekstowe1.get())**2
    drugazmienna=float(poletekstowe2.get())**2
    wynik=(pierwszazmienna+drugazmienna)**(1/2)
    wynik=Label(glowneokno,text=wynik)
    wynik.grid(row=1,column=4)


glowneokno=Tk()
glowneokno.title("moje okno")
glowneokno.geometry("400x200")

opispolatekstowego1=Label(glowneokno, text="a^2")
opispolatekstowego1.grid(row=0, column=0)
poletekstowe1=Entry(glowneokno)
poletekstowe1.grid(row=1, column=0)
opispolatekstowego2=Label(glowneokno, text="b^2")
opispolatekstowego2.grid(row=0, column=2)
poletekstowe2=Entry(glowneokno)
poletekstowe2.grid(row=1, column=2)
opispolawynik=Label(glowneokno, text="c^2")
opispolawynik.grid(row=0, column=4)

przycisk=Button(glowneokno, text="oblicz", command=akcjaprzycisk)
przycisk.grid(row=2, column=2)


glowneokno.mainloop()





#zad7

def akcjaprzycisk():
    wynik1=float(poletekstowe1.get())
    wynik2=float(poletekstowe2.get())
    wynikcaly=wynik1*wynik2
    messagebox.showinfo("wynik", wynikcaly)


glowneokno=Tk()
glowneokno.title("moje okno")
glowneokno.geometry("400x400")

opispolatekstowego1=Label(glowneokno, text="wprowadz a")
opispolatekstowego1.grid(row=0, column=0)
poletekstowe1=Entry(glowneokno)
poletekstowe1.grid(row=1, column=0)
opispolatekstowego2=Label(glowneokno, text="wprowadz b")
opispolatekstowego2.grid(row=0, column=2)
poletekstowe2=Entry(glowneokno)
poletekstowe2.grid(row=1, column=2)

przycisk=Button(glowneokno, text="wynik", command=akcjaprzycisk)
przycisk.grid(row=2, column=1)
glowneokno.mainloop()





#pomoc
def do_sqrt():
    root = float(number_input.get())**0.5
    MessageBox.showinfo("Square Root = ", root)


def do_square():
    square = float(number_input.get())**2
    MessageBox.showinfo("Square = ", square)

main_window = Tk()
main_window.title("Simple Calc")
number_input = Entry(main_window)
button_sqrt = Button(main_window, text="Square Root", command=do_sqrt)
button_sqrt.pack()
button_square = Button(main_window, text="Square", command=do_square)
button_square.pack()
number_input.pack()


main_window.mainloop()
'''




'''
#zad6

def akcjaprzycisk():
    zlicz=0
    while True:

            zlicz+=1
            zliczanie=zlicz
            zliczanie=Label(glowneokno,text=zliczanie)
            zliczanie.grid(row=2,column=2)
        else:
            break

glowneokno=Tk()
glowneokno.title("moje okno")
glowneokno.geometry("400x200")

przycisk=Button(glowneokno, text="klik", command=akcjaprzycisk)
przycisk.grid(row=1, column=2)


glowneokno.mainloop()
'''
