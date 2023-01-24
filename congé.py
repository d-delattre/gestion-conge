import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import datetime
import time
import calendar
from io import BytesIO
from PIL import Image


class Conge:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.state = {
            "congé" : 1,
            "malade" : 2,
            "weekend" : 3,
            "récup" : 4,
            "récup de " + str(int(self.year)-1) : 5,
            "jour férié" : 6,
            "quatre cinquième" : 7,
            "convention" : 8,
            "accouchement" : 9,
            "quarantaine" : 10
        }
        self.saturdays = np.array(calendar.monthcalendar(year, month))[:,5]
        self.sundays = np.array(calendar.monthcalendar(year, month))[:,6]
        self.name_list = np.loadtxt('./.personel.txt', dtype="str")
        self.names = {}
        for i in range(len(self.name_list)):
            self.names[self.name_list[i]] = i
        self.colors = [
         'white',     #rien
         'green',     #congé
         'red',       #maladie
         'black',     #weekend
         'orange',    #récup
         'grey',      #récup_année_précédente
         'blue',      #6
         'yellow',    #7
         'darkgreen', #8
         'lightblue', #9
         'purple'     #10
         ]


    def display_mmatrix(self):
        self.ndays = int(calendar.month(self.year, self.month)[-3:-1])

        #Créer une matrice dont les valeurs correspondent à un certain affichage
        mmatrix = np.zeros((len(self.name_list), self.ndays))

        #Charge un fichier contenant les congés et modifie la matrice d'affichage.
        congés = np.loadtxt("./.congé.txt", dtype="U",delimiter=";")
        #print(np.shape(congés))
        #print(congés.shape)
        if len(congés) == 0:
            print("Pas de congés ou de maladie.")
        else:
            if congés.shape == (3,):
                congés = np.array([congés])
            #print(congés)
            for congé in congés:
                if int(congé[1].split('/')[1]) == self.month:
                    mmatrix[self.names[congé[0]], int(congé[1].split('/')[0])-1] = self.state[congé[2]]

        #Modifie la matrice d'affichage pour mettre les weekends en couleur.
        for i in np.arange(self.ndays):
            if i in self.saturdays and (i-1)>=0:
                mmatrix[:,i-1] = self.state['weekend']
            elif i in self.sundays and (i-1)>=0:
                mmatrix[:,i-1] = self.state['weekend']

        return mmatrix


    def fig_maker(self, mmatrix):
        #Initialise le mapping des couleurs
        cmap = mpl.colors.ListedColormap(self.colors)
        norm = mpl.colors.BoundaryNorm(np.arange(len(self.colors)), cmap.N)

        #Initialise l'affichage
        width, height = figsize = (12, 10)
        fig, ax = plt.subplots(figsize=figsize)
        dpi = fig.get_dpi()
        #print(dpi)
        self.size = (width*dpi, height*dpi)

        #Crée la figure à partir de la matrice
        im = ax.imshow(mmatrix, cmap=cmap, norm=norm)

        #Paramètres de l'affichage
        ax.set_xticks(np.arange(self.ndays))
        ax.set_yticks(np.arange(len(self.name_list)))
        ax.set_xticklabels(np.arange(self.ndays)+1)
        ax.set_yticklabels(self.name_list)
        #ax.grid()

        # Rotation et alignement des labels.
        plt.setp(ax.get_xticklabels(), rotation=0, ha="center",
                 rotation_mode="anchor")

        #écrire une veleur dans les cases
        #for i in range(len(vegetables)):
        #    for j in range(len(farmers)):
        #        text = ax.text(j, i, harvest[i, j],
        #                       ha="center", va="center", color="w")

        #titre et commandes d'affichage
        ax.set_title("Planning congés/maladies du mois de ")
        fig.tight_layout()
        #window.write_event_value('-THREAD-', 'done.')
        #time.sleep(1)
        #plt.show()

        with BytesIO() as b:
            plt.savefig(b, format='png')
            im = Image.open(b)
            del im
            return b.getvalue()

    


if __name__ == "__main__":
    c = Conge(2023, 1)
    mm = c.display_mmatrix()
    print(c.fig_maker(mm))
