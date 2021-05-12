from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter
from random import randint

'''
glowneokno=Tk()
glowneokno.geometry("400x400")

def usunprzycisk():
    przyciskpoprzednie.destroy()
    stworzprzycisk()

def stworzprzycisk():
    global przyciskpoprzednie
    przyciskpoprzednie=Button(glowneokno,text="wcisnij", command=usunprzycisk)
    przyciskpoprzednie.place(x=50,y=100)

stworzprzycisk()

glowneokno.mainloop()






glowneokno=Tk()
glowneokno.geometry("400x400")

def usunprzycisk():
    przyciskpoprzednie.destroy()

przyciskpoprzednie=Button(glowneokno, text="wcisnij", command=usunprzycisk)
przyciskpoprzednie.place(x=170,y=50)

glowneokno.mainloop()


glowneokno=Tk()
glowneokno.title("moje okno")
glowneokno.geometry("300x250")

przyciskred=Button(glowneokno, text="czerwony", fg="red")
przyciskred.place(x=70, y=50)
przyciskzielen=Button(glowneokno, text="zielony", fg="green")
przyciskzielen.place(x=170, y=50)
przyciskniebieski=Button(glowneokno, text="niebieski", fg="blue")
przyciskniebieski.place(x=70, y=150)
przyciskbiel=Button(glowneokno, text="biały", fg="white")
przyciskbiel.place(x=170, y=150)

glowneokno.mainloop()




glowneokno=Tk()
glowneokno.geometry("400x400")

def usunprzycisk():
    przyciskpoprzednie.destroy()

przyciskpoprzednie=Button(glowneokno, text="wciśnij", command=usunprzycisk)
przyciskpoprzednie.place(x=150, y=100)

glowneokno.mainloop()





def akcjazrob():
    messagebox.showinfo("coś", "wyświetlam okno")

def akcjaautor():
    messagebox.showinfo("autor","that's me")

glowneokno=Tk()
pasekmenu=Menu(glowneokno)
pierwszemenu=Menu(pasekmenu, tearoff=0)

pierwszemenu.add_command(label="zrob coś", command=akcjazrob)
pierwszemenu.add_command(label="wyjdz", command=glowneokno.quit)
pasekmenu.add_cascade(label="pierwsze", menu=pierwszemenu)

pomocmenu=Menu(pasekmenu, tearoff=0)
pomocmenu.add_command(label="o autorze", command=akcjaautor)
pasekmenu.add_cascade(label="autor", menu=pomocmenu)

glowneokno.config(menu=pasekmenu)
glowneokno.mainloop()





glowneokno=Tk()
plotno=Canvas(glowneokno, width=400, height=400)
plotno.pack()
obraz=Image.open("castiel.jpg")
obraz=obraz.filter(ImageFilter.CONTOUR)
obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(200,200,image=obrazTk)
glowneokno.mainloop()




#zad1


def kawalskiegoopcje():
    messagebox.showinfo("opcje", "tak jest szefie")

def kowalskiego():
    messagebox.showinfo("opcje2", "(*^*) naszą opcją jest manewr sowi foch")

glowneokno=Tk()
pasekmenu=Menu(glowneokno)
pierwszemenu=Menu(pasekmenu, tearoff=0)

pierwszemenu.add_command(label="zrob coś")
pierwszemenu.add_command(label="nutychinskie")
pierwszemenu.add_command(label="wyjdz", command=glowneokno.quit)
pasekmenu.add_cascade(label="pierwsze", menu=pierwszemenu)

pomocmenu=Menu(pasekmenu, tearoff=0)
pomocmenu.add_command(label="opcje", command=kawalskiegoopcje)
pomocmenu.add_command(label="nuty")
pomocmenu.add_command(label="opcja2", command=kowalskiego)
pasekmenu.add_cascade(label="kowalski", menu=pomocmenu)

pomocmenu2=Menu(pasekmenu, tearoff=0)
pomocmenu2.add_command(label="uuuuu")
pomocmenu2.add_command(label="whaaat")
pomocmenu2.add_command(label="option")
pasekmenu.add_cascade(label="pampam", menu=pomocmenu2)

glowneokno.config(menu=pasekmenu)
glowneokno.mainloop()




#zad3
glowneokno=Tk()
glowneokno.geometry("400x400")
pasekmenu=Menu(glowneokno)

def stworzprzycisk():
    global przycisk
    przycisk=Button(glowneokno, text="wciśnij")
    przycisk.place(x=50,y=100)

def usunprzycisk():
    przycisk.destroy()


pierwszemenu=Menu(pasekmenu, tearoff=0)
pierwszemenu.add_command(label="stworz", command=stworzprzycisk)
pasekmenu.add_cascade(label="stworz przycisk", menu=pierwszemenu)

pomocmenu=Menu(pasekmenu, tearoff=0)
pomocmenu.add_command(label="usuń", command=usunprzycisk)
pasekmenu.add_cascade(label="usuń przycisk", menu=pomocmenu)


glowneokno.config(menu=pasekmenu)
glowneokno.mainloop()






#zad4

glowneokno=Tk()
glowneokno.geometry("400x400")
pasekmenu=Menu(glowneokno)

def stworzelement1():
    global element1
    element1=Label(glowneokno, text="hi")
    element1.place(x=100,y=100)

def stworzelement2():
    global element2
    element2=Label(glowneokno, text="sowi foch (*^*)")
    element2.place(x=50,y=50)

def usunelement1():
    element1.destroy()

def usunelement2():
    element2.destroy()


pierwszemenu=Menu(pasekmenu, tearoff=0)
pierwszemenu.add_command(label="stwórz powitanie", command=stworzelement1)
pasekmenu.add_cascade(label="stwarzanie", menu=pierwszemenu)

pomocmenu1=Menu(pasekmenu, tearoff=0)
pomocmenu1.add_command(label="usuń powitanie", command=usunelement1)
pasekmenu.add_cascade(label="usuwanie", menu=pomocmenu1)

drugiemenu=Menu(pasekmenu, tearoff=0)
drugiemenu.add_command(label="aktywacja", command=stworzelement2)
pasekmenu.add_cascade(label="stwarzanie", menu=drugiemenu)

pomocmenu=Menu(pasekmenu, tearoff=0)
pomocmenu.add_command(label="usuń aktywacje", command=usunelement2)
pasekmenu.add_cascade(label="usuwanie", menu=pomocmenu)


glowneokno.config(menu=pasekmenu)
glowneokno.mainloop()


#zad5

glowneokno=Tk()
glowneokno.geometry("400x400")
pasekmenu=Menu(glowneokno)

def stworzprzycisk1():
    global przycisk1
    przycisk1=Button(glowneokno, text="wciśnij")
    przycisk1.place(x=50,y=100)

def stworzprzycisk2():
    global przycisk2
    przycisk2=Button(glowneokno, text="wciskaj")
    przycisk2.place(x=100,y=50)

def stworzprzycisk3():
    global przycisk3
    przycisk3=Button(glowneokno, text="hejo")
    przycisk3.place(x=40,y=20)

def stworzprzycisk4():
    global przycisk4
    przycisk4=Button(glowneokno, text="(*^*)")
    przycisk4.place(x=150,y=200)

def usunprzycisk():
    przycisk1.destroy()
    przycisk2.destroy()
    przycisk3.destroy()
    przycisk4.destroy()


pierwszemenu=Menu(pasekmenu, tearoff=0)
pierwszemenu.add_command(label="stwórz przycisk1", command=stworzprzycisk1)
pasekmenu.add_cascade(label="stwarzanie", menu=pierwszemenu)

pomocmenu1=Menu(pasekmenu, tearoff=0)
pomocmenu1.add_command(label="stwórz przycisk2", command=stworzprzycisk2)
pasekmenu.add_cascade(label="stwarzanie", menu=pomocmenu1)

drugiemenu=Menu(pasekmenu, tearoff=0)
drugiemenu.add_command(label="stwórz przycisk3", command=stworzprzycisk3)
pasekmenu.add_cascade(label="stwarzanie", menu=drugiemenu)

pomocmenu=Menu(pasekmenu, tearoff=0)
pomocmenu.add_command(label="stwórz przycisk4", command=stworzprzycisk4)
pasekmenu.add_cascade(label="stwarzanie", menu=pomocmenu)

pomocmenu3=Menu(pasekmenu, tearoff=0)
pomocmenu3.add_command(label="usuń przyciski", command=usunprzycisk)
pasekmenu.add_cascade(label="usuwanie", menu=pomocmenu3)

glowneokno.config(menu=pasekmenu)
glowneokno.mainloop()

'''

#zad6



def filtr1():
    global obraz
    global obrazTk
    obraz=Image.open("kitten.jpg")
    obraz=obraz.filter(ImageFilter.CONTOUR)
    obrazTk=ImageTk.PhotoImage(obraz)
    plotno.create_image(200,200,image=obrazTk)


def filtr2():
    global obraz
    global obrazTk
    obraz=Image.open("kitten.jpg")
    obraz=obraz.filter(ImageFilter.FIND_EDGES)
    obrazTk=ImageTk.PhotoImage(obraz)
    plotno.create_image(200,200,image=obrazTk)


def filtr3():
    global obraz
    global obrazTk
    obraz=Image.open("kitten.jpg")
    obraz=obraz.filter(ImageFilter.EMBOSS)
    obrazTk=ImageTk.PhotoImage(obraz)
    plotno.create_image(200,200,image=obrazTk)

def filtr4():
    global obraz
    global obrazTk
    obraz=Image.open("kitten.jpg")
    obraz=obraz.filter(ImageFilter.EDGE_ENHANCE_MORE)
    obrazTk=ImageTk.PhotoImage(obraz)
    plotno.create_image(200,200,image=obrazTk)

def original():
    global obraz
    global obrazTk
    obraz=Image.open("kitten.jpg")
    obrazTk=ImageTk.PhotoImage(obraz)
    plotno.create_image(200,200,image=obrazTk)


glowneokno=Tk()
plotno=Canvas(glowneokno, width=600, height=600)
plotno.pack()
obraz=Image.open("kitten.jpg")
obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(200,200,image=obrazTk)


przycisk1=Button(glowneokno, text="zmiana1", command=filtr1)
przycisk1.place(x=100,y=500)

przycisk2=Button(glowneokno, text="zmiana2", command=filtr2)
przycisk2.place(x=200,y=500)

przycisk3=Button(glowneokno, text="zmiana3", command=filtr3)
przycisk3.place(x=300,y=500)

przycisk4=Button(glowneokno, text="zmiana4", command=filtr4)
przycisk4.place(x=400,y=500)

pasekmenu=Menu(glowneokno)
pierwszemenu=Menu(pasekmenu, tearoff=0)
pierwszemenu.add_command(label="oryginał", command=original)
pierwszemenu.add_command(label="wyjdz", command=glowneokno.quit)
pasekmenu.add_cascade(label="opcje", menu=pierwszemenu)

glowneokno.config(menu=pasekmenu)
glowneokno.mainloop()

'''

#zad7

def test1():
    zad1=IntVar()
    zad2=IntVar()

    def akcjaprzycisk():
        wynik=0
        if zad1.get()==1:
            wynik+=1
        if zad2.get()==2:
            wynik+=1
        messagebox.showinfo("okno wynik", "twój wynik:"+ str(wynik))

    pyt1=Label(glowneokno, text="Imiona głównych bohaterów 'supernatural': ")
    pyt1.pack()
    rprzycisk1=Radiobutton(glowneokno, text="Sam i Dean", variable=zad1, value=1)
    rprzycisk1.pack()
    rprzycisk2=Radiobutton(glowneokno, text="Cassandra i Samantha", variable=zad1, value=2)
    rprzycisk2.pack()
    pyt2=Label(glowneokno, text="Ile sezonów ma 'supernatural': ")
    pyt2.pack()
    rprzycisk1=Radiobutton(glowneokno, text="14", variable=zad2, value=1)
    rprzycisk1.pack()
    rprzycisk2=Radiobutton(glowneokno, text="13", variable=zad2, value=2)
    rprzycisk2.pack()
    przycisk=Button(glowneokno, text="wynik", command=akcjaprzycisk)
    przycisk.pack()


def test2():
    zad1=IntVar()
    zad2=IntVar()

    def akcjaprzycisk():
        wynik=0
        if zad1.get()==1:
            wynik+=1
        if zad2.get()==2:
            wynik+=1
        messagebox.showinfo("okno wynik","twój wynik:"+ str (wynik))


    pyt1=Label(glowneokno, text="pierwszy dzień tygodnia to: ")
    pyt1.pack()
    rprzycisk1=Radiobutton(glowneokno, text="poniedziałek", variable=zad1, value=1)
    rprzycisk1.pack()
    rprzycisk2=Radiobutton(glowneokno, text="wtorek", variable=zad1, value=2)
    rprzycisk2.pack()
    pyt2=Label(glowneokno, text="drugi dzień tygodnia to: ")
    pyt2.pack()
    rprzycisk1=Radiobutton(glowneokno, text="poniedziałek", variable=zad2, value=1)
    rprzycisk1.pack()
    rprzycisk2=Radiobutton(glowneokno, text="wtorek", variable=zad2, value=2)
    rprzycisk2.pack()
    przycisk=Button(glowneokno, text="wynik", command=akcjaprzycisk)
    przycisk.pack()



glowneokno=Tk()
glowneokno.geometry("400x400")
pasekmenu=Menu(glowneokno)


pierwszemenu=Menu(pasekmenu, tearoff=0)
pierwszemenu.add_command(label="test1", command=test1)
pierwszemenu.add_command(label="test2", command=test2)
pierwszemenu.add_command(label="wyjdź", command=glowneokno.quit)
pasekmenu.add_cascade(label="menu", menu=pierwszemenu)


glowneokno.config(menu=pasekmenu)
glowneokno.mainloop()



#zad8

def filtr1():
    global obraz
    global obrazTk
    obraz=Image.open("kitten.jpg")
    obrazTk=ImageTk.PhotoImage(obraz)
    plotno.create_image(200,200,image=obrazTk)


def filtr2():
    global obraz
    global obrazTk
    obraz=Image.open("castiel.jpg")
    obrazTk=ImageTk.PhotoImage(obraz)
    plotno.create_image(200,200,image=obrazTk)


def filtr3():
    global obraz
    global obrazTk
    obraz=Image.open("dean.jpg")
    obrazTk=ImageTk.PhotoImage(obraz)
    plotno.create_image(200,200,image=obrazTk)

def filtr4():
    global obraz
    global obrazTk
    obraz=Image.open("sam.jpg")
    obrazTk=ImageTk.PhotoImage(obraz)
    plotno.create_image(200,200,image=obrazTk)


glowneokno=Tk()
plotno=Canvas(glowneokno, width=600, height=600)
plotno.pack()
pasekmenu=Menu(glowneokno)

pierwszemenu=Menu(pasekmenu, tearoff=0)
pierwszemenu.add_command(label="kotek", command=filtr1)
pierwszemenu.add_command(label="cass", command=filtr2)
pierwszemenu.add_command(label="dean", command=filtr3)
pierwszemenu.add_command(label="sammy", command=filtr4)
pierwszemenu.add_command(label="wyjdz", command=glowneokno.quit)
pasekmenu.add_cascade(label="menu", menu=pierwszemenu)

glowneokno.config(menu=pasekmenu)
glowneokno.mainloop()
'''
