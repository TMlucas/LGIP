from tkinter import *
from random import randint
from math import *


#definition des fonctions
def clic(event):
    X=ceil(h*event.x/500)
    Y=ceil(w*event.y/500)

    print (X,Y)

    if X==lm and Y==cm:
        texte.set("C'est gagné")
        canvas.create_rectangle((500/h)*(X-1)+1,(500/w)*(Y-1)+1,(500/h)*X-1,(500/w)*Y-1,fill='red')
    else:
        cmp,lmp=False,False
        canvas.create_rectangle((500/h)*(X-1)+1,(500/w)*(Y-1)+1,(500/h)*X>
        if abs(X-lm)==1 or abs(X-lm)==0:
            lmp=True
        if abs(Y-cm)==1 or abs(Y-cm)==0:
            cmp=True
        if lmp ==True and cmp ==True:
            texte.set("C'est proche")
        else:
            texte.set("C'est loin")


#Taille du tableau
try:
    print ("Entrez la taille de l'océan\n(Maximum 10 par 10)\n")
    h=int(input("Entrer la largeur : "))
    w=int(input("Entrer la longueur : "))
    if h>10 or w>10:
        print("Les dimensions sont trop grandes\n")
    else :
        d=1
except:
    print ("Les donnees ne sont pas correctes\n")

#Case mystere
lm=randint(1,h)
cm=randint(1,w)

count=0

#Fenetre
main = Tk()
main.title ("Bataille navale")
main.geometry('800x800+25+25')
main.config(cursor='hand1')
font28="-size 28"
titre = Label (main, text="Bienvenue dans le jeu de la bataille navale")
titre.pack()
titre.configure(font=font28)

canvas = Canvas(main, width=500, height=500, background='blue', cursor="pirate")
canvas.pack(padx=10, pady=50)
for i in range (1, w):
    canvas.create_rectangle(i*500/(w),0,i*500/(w),500,fill='brown')
for i in range (1,h):
    canvas.create_rectangle(0,i*500/h,500,i*500/h,fill ='brown')


texte=StringVar()
texte.set('')
lose=Label(main,textvariable=texte)
lose.pack()
lose.configure(font=font28)

canvas.bind('<Button-1>', clic)

main.mainloop()
