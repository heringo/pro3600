import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
import yfinance as yf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from fpdf import FPDF
import os
import datetime


fichier = open("historique.txt", "r")
nouv = fichier.read()
fichier.close()
historique = nouv.split()
auj=datetime.date.today()
Mem=[]

def update() :                               #mise à jour du fichier historique à chaque menu déroulant
    fichier = open("historique.txt", "r")
    nouv = fichier.read()
    fichier.close()
    text["values"] = nouv.split()

root = tk.Tk()              #mise en place de l'interface
root.geometry("1920x1080")
root.configure(bg='grey')


var1 = tk.BooleanVar()
check1 = tk.Checkbutton(root, text = "chandelier", height = 2, width = 10, variable=var1)
check1.place(x=200,y=700)

debut=tk.Label(text="DEBUT :", fg="blue", height=1, width=4, padx=5, bg='grey')
fin=tk.Label(text="FIN :", fg="red", height=1, width=4, padx=5, bg='grey')

text=tk.ttk.Combobox(root, values=historique, width=120, postcommand=update)
text.place(x=135, y=24)

ca1=tk.Text(root, height=1, width=4, padx=5)        #mise en place des boutons de choix des dates
ca1.place(x=1400, y=35)

ca2=tk.Text(root, height=1, width=4, padx=5)
ca2.place(x=1400, y=65)
ca2.insert('1.0', str(auj.year))

tj1=tk.Label(text="jour :", fg="blue", bg='grey')   
tm1=tk.Label(text="mois :", fg="blue", bg='grey')
ta1=tk.Label(text="année :", fg="blue", bg='grey')
tj1.place(x=1110, y=35)
tm1.place(x=1200, y=35)
ta1.place(x=1350, y=35)

tj2=tk.Label(text="jour :", fg="red", bg='grey')
tm2=tk.Label(text="mois :", fg="red", bg='grey')
ta2=tk.Label(text="année :", fg="red", bg='grey')
tj2.place(x=1110, y=65)
tm2.place(x=1200, y=65)
ta2.place(x=1350, y=65)

debut.place(x=1060,y=35)
fin.place(x=1070,y=65)

jours=[i for i in range(1,32)]
mois=["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]

cj1 = ttk.Combobox(root, values=jours, width=2)
cj1.place(x=1150,y=35)
cm1 = ttk.Combobox(root, values=mois, width=10)
cm1.place(x=1250,y=35)

cj2 = ttk.Combobox(root, values=jours, width=2)
cj2.place(x=1150,y=65)
cm2 = ttk.Combobox(root, values=mois, width=10)
cm2.place(x=1250,y=65)
cj2.current(auj.day-1)
cm2.current(auj.month-1)                #fin de mise en place des boutons de choix des dates

zooms=tk.Text(root, height=1, width=2, padx=5)      #bouton de zoom
zooms.place(x=500, y=700)

def getEntry():                         #lancement de la création de la figure après avoir entré les paramètres
    global ticker, dj, dm, da, fj, fm, fa
    ticker = text.get()
    dj = str(cj1.get())
    dm = str(mois.index(cm1.get())+1)
    da = str(ca1.get("1.0",'end-1c'))
    fj = str(cj2.get())
    fm = str(mois.index(cm2.get())+1)
    fa = str(ca2.get("1.0",'end-1c'))
    triger(ticker, dj, dm, da, fj, fm, fa)

def triger(ticker, dj, dm, da, fj, fm, fa):     #séléction de la date de début et de fin
    global start, end
    start = da+'-'+dm+'-'+dj
    end = fa+'-'+fm+'-'+fj
    dessin()
  
def dessin() :                                  #création du graph dans matplotlib
    global absi, start, end, ticker, plot1
    stock = yf.download(ticker, start, end)
    if not stock.empty :
        fig = Figure(figsize = (30, 20), dpi = 30, facecolor=('grey'))
        plot1 = fig.add_subplot(111)
        y = stock.iloc[:,4]
        absi = stock.index[0:len(y)]
        if not var1.get():                      #graph classique

            plot1.plot(absi,y)
            
        else:                                   #graph en chandelier
            up = stock[stock.Close >= stock.Open]
            down = stock[stock.Close < stock.Open]
            
            col1 = 'red'
            col2 = 'green'
            width = 1
            width2 = .3
              
            plot1.bar(up.index, up.Close-up.Open, width, bottom=up.Open, color=col1)
            plot1.bar(up.index, up.High-up.Close, width2, bottom=up.Close, color=col1)
            plot1.bar(up.index, up.Low-up.Open, width2, bottom=up.Open, color=col1)
              
            plot1.bar(down.index, down.Close-down.Open, width, bottom=down.Open, color=col2)
            plot1.bar(down.index, down.High-down.Open, width2, bottom=down.Open, color=col2)
            plot1.bar(down.index, down.Low-down.Close, width2, bottom=down.Close, color=col2)
            
        canvas = FigureCanvasTkAgg(fig, master = root)  
        canvas.draw()
        
        canvas.get_tk_widget().place(x=50,y=50)
        
    if ticker not in historique :                   #enegistrement dans l'historique de la dernière entrée
        fichier = open("historique.txt", "a")
        fichier.write(ticker+' ')
        fichier.close()
        
def export() :                      #exporter une image en pdf (à coriger)
    plot1.savefig("figure.jpeg", format="jpeg")
    pdf = FPDF()
    pdf.add_page()
    pdf.image("figure.jpeg")
    pdf.output("doc-with-figure.pdf")
    os.remove("figure.jpeg")
    
def browseFiles():                  #ouvrir un fichier de sauvegarde
    global ticker
    filename = tk.filedialog.askopenfilename(filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    fichier = open(filename, "r")
    nouv = fichier.read()
    fichier.close()
    sauvegarde = nouv.split()
    if len(sauvegarde)==7 :
        [ticker, dj, dm, da, fj, fm, fa] = sauvegarde
        triger(ticker, dj, dm, da, fj, fm, fa)
        cj1.current(int(dj)-1)
        cm1.current(int(dm)-1)
        cj2.current(int(fj)-1)
        cm2.current(int(fm)-1)
        update()
        text.current(text["values"].index(ticker))
        ca1.delete('1.0',"end")
        ca2.delete('1.0',"end")
        ca1.insert('1.0', da)
        ca2.insert('1.0', fa)

def save() :                        #sauvegarde des dates entrée et de l'entreprise choisi
    fichier = tk.filedialog.asksaveasfile(mode='w', filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    ticker = text.get()
    fichier.write(ticker+' '+dj+' '+dm+' '+da+' '+fj+' '+fm+' '+fa)
    fichier.close()

def clic(event):                    #zoom dans l'image à l'aide de la valeur entrée dans la case
    global Mem, absi, start, end
    zoom=int(zooms.get("1.0",'end-1c'))
    tx=len(absi)
    x=event.x
    h=event.y
    inter=int(697/tx)
    i=0
    if x<=810 and x>=113 and h<=524 and h>=72 :
        Mem.append([start,end])
        while x-113<=i*inter:
            i=i+1
        if i-tx//zoom<0:
            start=absi[0]
            end=absi[tx//zoom]
        elif i+tx//zoom>tx:
            start=absi[tx-tx//zoom]
            end=absi[tx]
        else:
            start=absi[i-tx//zoom]
            end=absi[i+tx//zoom]
        if len(absi)<=0:
            retour()
        else:
            dessin()
        
def retour():                       #retour arrière du zoom
    global Mem,start,end 
    ret=Mem.pop()               
    start=ret[0]
    end=ret[1]
    dessin()
 
menubar = tk.Menu(root)                     #création de la barre d'outil
menu1 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=menu1)
menu1.add_command(label="Ouvrir", command=browseFiles)
menu1.add_command(label="Sauvegarder", command=save)
menu1.add_separator()
menu1.add_command(label="Exporter en PDF", command=export)  #fin de création de la barre d'outil
root.config(menu=menubar)

root.bind("<Button-1>",clic)

btn = tk.Button(root, height=1, width=10, text="Lire", command=getEntry)  #création des boutons de lecture et de retour
btn.place(x=50, y=20)
rtn = tk.Button(root, height=1, width=10, text="Retour", command=retour)
rtn.place(x=700,y=700)

root.mainloop()

