from tkinter import *
from string import ascii_lowercase
from random import randint
from txttaquin import Taquin

class VueTaquin:
    '''Gère la Vue du jeu du Taquin.
    '''

    def __init__(self, taq):
        '''VueTaquin, Taquin -> VueTaquin
        '''

        fen = Tk()
        fen.title("Taquin")
        self.__taq = taq

        self.__images = initialisation_images()

        self.__btns = []
        for l in range(taq.dim()):
            for c in range(taq.dim()):
                self.__btns.append(Button(fen))
                self.__btns[-1].grid(row=l, column=c)

        lig,col = taq.coords_vide()
        self.mettre_a_jour(lig, col)

        f = Frame(fen)
        btn_rec = Button(f, text='Recommencer', command=self.ctrl_reinit)
        btn_quit = Button(f, text='Quitter', command=fen.destroy)

        f.grid(row=taq.dim(), column=0, columnspan=taq.dim())
        btn_rec.grid(row=0,column=0)
        btn_quit.grid(row=0, column=1)

        fen.mainloop()

    def mettre_a_jour(self, lig, col):
        '''Met à jour la vue.
        Arguments :
            self : VueTaquin --
            lig : int -- coordonnée de ligne de la case vide.
            col : int -- coordonnée de colonne de la case vide.
        Retour : None
        '''

        for l in range(self.__taq.dim()):
            for c in range(self.__taq.dim()):
                self.__btns[l*self.__taq.dim() + c]['image'] = self.__images[self.__taq.get(l,c)]
                self.__btns[l*self.__taq.dim() + c]['command'] = self.creer_ctrl_choisit_case(l,c)
        self.__btns[lig*self.__taq.dim() + col]['image'] = self.__images[0]
        self.__btns[lig*self.__taq.dim() + col]['command'] = self.none

        for b in self.__btns:
            if self.__taq.partie_finie():
                b['state'] = 'disabled'
            else:
                b['state'] = 'active'

    #def ctrl_choisit_case(self):
    #    '''VueTaquin -> None
    #    '''

    #    l_vide,c_vide = self.__taq.coords_vide()
    #    coords_poss = []
    #    for i in range(self.__taq.dim()):
    #        for j in range(self.__taq.dim()):
    #            if (i,j) != (l_vide,c_vide):
    #                coords_poss.append((i,j))
        
    #    lig,col = coords_poss[randint(0, len(coords_poss) - 1)]
    #    self.__taq.permute_case_vide(lig, col)
        
    #    self.mettre_a_jour(lig,col)

    def ctrl_reinit(self):
        '''VueTaquin -> None
        '''

        self.__taq.reinit()
        lig,col = self.__taq.coords_vide()
        self.mettre_a_jour(lig,col)
        
    def creer_ctrl_choisit_case(self, lig, col):
        '''VueTaquin, int, int -> None
        '''

        def ctrl_choisit_case():
            '''None -> None
            '''
        
            if self.__taq.bouge_case(self.__taq.get(lig,col)):
                self.mettre_a_jour(lig,col)

        return ctrl_choisit_case

    def none(self):
        '''VueTaquin -> None'''
        pass

# Fin de la classe VueTaquin ---------------------------------------------------------------------

def initialisation_images():
    '''None -> list(PhotoImage)
    Initialise les images.
    '''

    images = []
    images.append(PhotoImage(file="./alphabet/rien.gif"))
    for let in ascii_lowercase:
        images.append(PhotoImage(file="./alphabet/"+let+".gif"))

    return images

if __name__ == "__main__":
    v = VueTaquin(Taquin())
