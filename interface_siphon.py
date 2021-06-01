from tkinter import Tk,simpledialog,filedialog,colorchooser,messagebox,Frame,Button
from tkinter import *
import tkinter as tk
from tkinter import ttk
from xtr_txt import *


def open_load():
    ret = filedialog.askopenfilename()
    return ret

def open_directory():
    ret = filedialog.askdirectory()
    return ret

def popup_NEW(fenetre,jeu):
    xtr = xtr_txt()


    def Parcourir(txt):

        if txt == 'root':
            var = open_directory()
            txt_file_root.set(var)
        if txt == 'driver':
            var = open_load()
            txt_file_driver.set(var)


    def Valider(fenetre,pop_up):

        print('mot de passe', txt_mdp.get()       )
        print('driver', txt_file_driver.get()     )

        xtr.run()
        
        pass

    ''' Génération de la pop_up'''
    NEW = Toplevel()		  # Popup -> Toplevel()
    NEW.title(' Recherche mot ')
    #NEW.geometry('300x500')
    NEW.transient(jeu)  # Réduction popup impossible


    ''' Contenue de la page '''
    POLICE_TEXTE = ('verdana', 10)
    POLICE_TITRE = ('verdana', 12)
    Espace = Label(NEW, text='  ').grid(row=0, column=0)
    label  = Label(NEW, text=' Recherche mot ', font=POLICE_TITRE).grid(row=0, column=2)
    label = Label(NEW, text=' ', font=POLICE_TEXTE).grid(row=1, column=1)

    label = Label(NEW, text='   ', font=POLICE_TEXTE).grid(row=2, column=1, sticky="nsw")
    label = Label(NEW, text=' Mot à rechercher ', font=POLICE_TEXTE).grid(row=4, column=1, sticky="nsw")

    txt_mdp = StringVar()
    case = Entry(NEW, width=10, textvariable=txt_mdp)
    case.config(font=('verdana', 10))
    case.grid(row=4, column=2, sticky="nsew", padx=1, pady=1)

    label_selection = Label(NEW, text=' ', font=POLICE_TEXTE)
    label_selection.grid(row=10, column=1, columnspan=2, sticky="nsw")
    label_selection._name = 'txt_root'


    label_selection = Label(NEW, text=' Selection du dossier driver :', font=POLICE_TEXTE)
    label_selection.grid(row=13, column=1, columnspan=2, sticky="nsw")
    label_selection._name = 'txt_driver'

    txt_file_driver = StringVar()
    case_file = Entry(NEW, width=10, textvariable=txt_file_driver)
    case_file.config(font=('verdana', 10))
    case_file.grid(row=15, column=1, columnspan=2, sticky="nsew", padx=1, pady=1)
    case_file._name = 'Entry_driver'

    bouton_parcourir =Button(NEW, text='Parcourir', command=lambda :Parcourir('driver'))
    bouton_parcourir.grid(row=15, column=3, sticky="nsew", padx=1, pady=1)
    bouton_parcourir._name = 'Parcourir_driver'

    label = Label(NEW, text=' ', font=POLICE_TEXTE).grid(row=16, column=1)
    Button(NEW, text='Quitter', command=NEW.destroy).grid(row=17, column=2, sticky="nse", padx=1, pady=1)
    Button(NEW, text='Valider', command=lambda :Valider(fenetre,NEW)    ).grid(row=17, column=2, sticky="nsw", padx=1, pady=1)

    label = Label(NEW, text=' ', font=POLICE_TEXTE).grid(row=16, column=4)
    ''' Vérouillage de la page en background et de la pop_up'''
    NEW.grab_set()  # Interaction avec fenetre jeu impossible
    jeu.wait_window(NEW)  # Arrêt script principal

if __name__ == '__main__':
    POLICE_TEXTE = ('verdana', 10)
    class fen():
        def __init__(self):
            self.titre = []

    fenetre = fen()

    jeu = Tk()					  # Fenêtre principale -> Tk()
    label = Label(jeu, text=' Logiciel développé avec amour par Copy4', font=POLICE_TEXTE).pack(padx=5, pady=5)
    jeu.title('Siphon savoir 0.1')
    jeu.geometry('300x100')
    Button(jeu, text='parametrage', command=lambda :popup_NEW(fen,jeu)).pack(padx=10, pady=10)

    jeu.mainloop()				  # Uniquement pour la fenêtre principale