# Importation du module Tkinter
from tkinter import *

#Création de la première fenêtre
window = Tk()

#Personalisation de la fenêtre
window.title ("Convertisseur Universel")
window.geometry("1080x720")
window.minsize(720, 480)
window.iconbitmap("Logo.ico")
window.config(background='#4065A4')

#Création de la boîte
frame = Frame(window, background='#4065A4')

#Création d'une image
width = 550
height = 550
image = PhotoImage(file="Logo.png").zoom(35).subsample(32)
canvas = Canvas(frame, width=width , height=height, background='#4065A4', border=0, highlightthicknes=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack()

#Création d'un titre
label_title = Label(frame, text="Convertisseur Universel", font=("Helvetica", 35), background='#4065A4', foreground='white')
label_title.pack()


def kilometre():
    a = float(entremi2.get())
    result = a*10**3
    print("{:.2e}m".format(result))
    entry.delete(0, END)
    entry.insert(0, "{:.2e}m".format(result))


def hectometre():
    a = float(entremi2.get())
    result = a*10**2
    print("{:.2e}m".format(result))
    entry.delete(0, END)
    entry.insert(0, "{:.2e}m".format(result))

def decametre():
    a = float(entremi2.get())
    result = a*10**1
    print("{:.2e}m".format(result))
    entry.delete(0, END)
    entry.insert(0, "{:.2e}m".format(result))

def metre():
    a = float(entremi2.get())
    result = a*10**0
    print("{:.2e}m".format(result))
    entry.delete(0, END)
    entry.insert(0, "{:.2e}m".format(result))

def decimetre():
    a = float(entremi2.get())
    result = a*10**-1
    print("{:.2e}m".format(result))
    entry.delete(0, END)
    entry.insert(0, "{:.2e}m".format(result))

def centimetre():
    a = float(entremi2.get())
    result = a*10**-2
    print("{:.2e}m".format(result))
    entry.delete(0, END)
    entry.insert(0, "{:.2e}m".format(result))

def millimetre():
    a = float(entremi2.get())
    result = a*10**-3
    print("{:.2e}m".format(result))
    entry.delete(0, END)
    entry.insert(0, "{:.2e}m".format(result))

def micrometre():
    a = float(entremi2.get())
    result = a*10**-6
    print("{:.2e}m".format(result))
    entry.delete(0, END)
    entry.insert(0, "{:.2e}m".format(result))

def nanometre():
    a = float(entremi2.get())
    result = a*10**-9
    print("{:.2e}m".format(result))
    entry.delete(0, END)
    entry.insert(0, "{:.2e}m".format(result))

#Distance
def distance():
    global entremi2
    global entry
    window3 = Tk()
    window3.title("Convertisseur Universel")
    window3.geometry("1080x720")
    window3.minsize(720, 480)
    window3.iconbitmap("Logo.ico")
    window3.config(background='#4065A4')
    frame3 = Frame(window3, background='#4065A4')
    frame3.pack(expand=YES)
    label_title = Label(frame3, text="Choissisez l'unité pour convertir en mètre", font=("Courrier"), background="#4065A4", foreground="white")
    label_title.pack()
    entremi2 = Entry(frame3, width=50)
    entremi2.pack(pady=20)
    menudistance = Menubutton(frame3, text='Distance', width='20', borderwidth=0, bg='white', relief=RAISED, activebackground='orange', foreground='#4065A4')
    menudistance.pack()
    entry = Entry(frame3, width=50)
    entry.pack(pady=20)

# Création d'un menu défilant

    menuDeroulant1 = Menu(menudistance, tearoff=0)
    menuDeroulant1.add_command(label='Kilomètre', command= kilometre)
    menuDeroulant1.add_command(label="Hectomètre", command= hectometre)
    menuDeroulant1.add_command(label="Décamètre", command= decametre)
    menuDeroulant1.add_command(label="Mètre", command= metre)
    menuDeroulant1.add_command(label="Décimètre", command= decimetre)
    menuDeroulant1.add_command(label="Centimètre", command= centimetre)
    menuDeroulant1.add_command(label="Décimètre", command= decimetre)
    menuDeroulant1.add_command(label="Millimètre", command= millimetre)
    menuDeroulant1.add_command(label="Micromètre", command= micrometre)
    menuDeroulant1.add_command(label="Nanomètre", command= nanometre)
# Attribution du menu déroulant au menu Affichage
    menudistance.configure(menu=menuDeroulant1)

#Durée
def heure():
    a = float(entremi.get())
    result = a*3600
    print("{:.2e}s".format(result))
    entry.delete(0, END)
    entry.insert(0, "{:.2e}s".format(result))

def minute():
    a = float(entremi.get())
    result = a*60
    print("{:.2e}s".format(result))
    entry.delete(0, END)
    entry.insert(0, "{:.2e}s".format(result))

def seconde():
    a = float(entremi.get())
    result = a*1
    print("{:.2e}s".format(result))
    entry.delete(0, END)
    entry.insert(0, "{:.2e}s".format(result))

def millisecondes():
    a = float(entremi.get())
    result = a*10**-3
    print("{:.2e}s".format(result))
    entry.delete(0, END)
    entry.insert(0, "{:.2e}s".format(result))


def duree():
    global entremi
    global entry
    window4 = Tk()
    window4.title("Convertisseur Universel")
    window4.geometry("1080x720")
    window4.minsize(720, 480)
    window4.iconbitmap("Logo.ico")
    window4.config(background='#4065A4')
    frame4 = Frame(window4, background='#4065A4')
    frame4.pack(expand=YES)
    label_title = Label(frame4, text="Choissisez l'unité pour convertir en seconde", font=("Courrier"), background="#4065A4", foreground="white")
    label_title.pack()
    entremi = Entry(frame4, width=50)
    entremi.pack(pady=20)
    menudistance = Menubutton(frame4, text='Durée', width='20', borderwidth=0, bg='white', relief=RAISED, activebackground='orange', foreground='#4065A4')
    menudistance.pack()
    entry = Entry(frame4, width=50)
    entry.pack(pady=20)

# Création d'un menu défilant

    menuDeroulant1 = Menu(menudistance, tearoff=0)
    menuDeroulant1.add_command(label='Heure', command= heure)
    menuDeroulant1.add_command(label="Minute", command= minute)
    menuDeroulant1.add_command(label="Seconde", command= seconde)
    menuDeroulant1.add_command(label="Millisecondes", command= millisecondes)
# Attribution du menu déroulant au menu Affichage
    menudistance.configure(menu=menuDeroulant1)


#Masse
def masse():
    global entremi3
    global entry
    window5 = Tk()
    window5.title("Convertisseur Universel")
    window5.geometry("1080x720")
    window5.minsize(720, 480)
    window5.iconbitmap("Logo.ico")
    window5.config(background='#4065A4')
    frame5 = Frame(window5, background='#4065A4')
    frame5.pack(expand=YES)
    label_title = Label(frame5, text="Choissisez l'unité pour convertir en mètre", font=("Courrier"), background="#4065A4", foreground="white")
    label_title.pack()
    entremi3 = Entry(frame5, width=50)
    entremi3.pack(pady=20)
    menudistance = Menubutton(frame5, text='Masse', width='20', borderwidth=0, bg='white', relief=RAISED, activebackground='orange', foreground='#4065A4')
    menudistance.pack()
    entry = Entry(frame5, width=50)
    entry.pack(pady=20)

# Création d'un menu défilant

    menuDeroulant1 = Menu(menudistance, tearoff=0)
    menuDeroulant1.add_command(label='Kilogramme', command= kilogramme)
    menuDeroulant1.add_command(label="Hectogramme", command= hectogramme)
    menuDeroulant1.add_command(label="Décagramme", command= decagramme)
    menuDeroulant1.add_command(label="Gramme", command= gramme)
    menuDeroulant1.add_command(label="Décigramme", command= decigramme)
    menuDeroulant1.add_command(label="Centigramme", command= centigramme)
    menuDeroulant1.add_command(label="Milligramme", command= millimetre)
# Attribution du menu déroulant au menu Affichage
    menudistance.configure(menu=menuDeroulant1)

#Puissance
def puissance():
    window6 = Tk()
    window6.title("Convertisseur Universel")
    window6.geometry("1080x720")
    window6.minsize(720, 480)
    window6.iconbitmap("Logo.ico")
    window6.config(background='#4065A4')

#Température
def temperature():
    window7 = Tk()
    window7.title("Convertisseur Universel")
    window7.geometry("1080x720")
    window7.minsize(720, 480)
    window7.iconbitmap("Logo.ico")
    window7.config(background='#4065A4')

#Volume
def volume():
    window8 = Tk()
    window8.title("Convertisseur Universel")
    window8.geometry("1080x720")
    window8.minsize(720, 480)
    window8.iconbitmap("Logo.ico")
    window8.config(background='#4065A4')

#Deuxième page / Menu déroulant Catégorie
def create():
    window.withdraw()
    window2 = Tk()
    window2.title("Convertisseur Universel")
    window2.geometry("1080x720")
    window2.minsize(720, 480)
    window2.iconbitmap("Logo.ico")
    window2.config(background='#4065A4')
    frame2 = Frame(window2, background='#4065A4')
    label_title = Label(frame2, text="Pour les nombres à virgule,\n il faut utiliser le '.'", font=("Helvetica", 15), background='#4065A4', foreground='white')
    label_title.pack()
    bouton1 = Button(frame2, text="Distance", font=("Courrier", 40), background='white', foreground='#4065A4', border=0, highlightthicknes=0, command=distance)
    bouton1.pack(pady=10)
    bouton2 = Button(frame2, text="Durée", font=("Courrier", 40), background='white', foreground='#4065A4', border=0, highlightthicknes=0, command =duree)
    bouton2.pack(pady=10)
    bouton3 = Button(frame2, text="Masse", font=("Cou   rrier", 40), background='white', foreground='#4065A4', border=0, highlightthicknes=0, command= masse)
    bouton3.pack(pady=10)
    bouton4 = Button(frame2, text="Puissance", font=("Courrier", 40), background='white', foreground='#4065A4', border=0, highlightthicknes=0, command= puissance)
    bouton4.pack(pady=10)
    bouton5 = Button(frame2, text="Température", font=("Courrier", 40), background='white', foreground='#4065A4', border=0, highlightthicknes=0, command= temperature)
    bouton5.pack(pady=10)
    bouton6 = Button(frame2, text="Volume", font=("Courrier", 40), background='white', foreground='#4065A4', border=0, highlightthicknes=0 ,command= volume)
    bouton6.pack(pady=10)
    frame2.pack(expand=YES)


#Ajout d'un bouton
bouton = Button(frame, text="Continuer",font=("Courrier", 40), background='white', foreground='#4065A4',border=0, highlightthicknes=0, command=create )
bouton.pack(pady=15)

#Affichage de la boîte
frame.pack(expand=YES)


#Affichage de la fenêtre
window.mainloop()


