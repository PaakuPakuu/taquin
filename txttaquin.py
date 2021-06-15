from random import randint

class Taquin:
    '''Représente le jeu du Taquin.
    '''
    
    def __init__(self, dim=4):
        '''Taquin, int --> Taquin
        '''
        
        assert dim > 1
        
        self.__dim = dim
        self.__plateau = []
        
        for l in range(dim):
            ligne = []
            for c in range(dim):
                ligne.append(l * dim + c + 1)
                
            self.__plateau.append(ligne)
        
        self.__plateau[-1][-1] = -1
        self.__coords_vide = (self.__dim - 1, self.__dim - 1)
    
    def __str__(self):
        '''Taquin --> None
        '''
        
        plat = ''
        
        for l in self.__plateau:
            plat += ('+' + '-' * len(str(self.__dim**2 - 1)) ) * (self.__dim) + '+\n'
                
            for nb in l:
                if nb != -1:
                    plat += '|' + ' ' * (len(str(self.__dim**2 - 1)) - len(str(nb))) + str(nb)
                else:
                    plat += '|' + ' ' * len(str(self.__dim**2 - 1))
            plat += '|\n'

        plat += ('+' + '-' * len(str(self.__dim**2 - 1)) ) * (self.__dim) + '+'
        
        return plat

    def dim(self):
        '''Taquin -> int
        '''

        return self.__dim

    def get(self, lig, col):
        '''Taquin, int, int-> int
        '''

        return self.__plateau[lig][col]

    def coords_vide(self):
        '''Taquin -> (int,int)
        '''

        return self.__coords_vide

    def est_vide(self,lig,col):
        '''Taquin, int, int -> boolean
        '''

        return self.__coords_vide == (lig, col)

    def bouge_case(self, val):
        '''Taquin (modif), int --> bool
        '''
            
        lig ,col = self.coords(val)
        if (lig ,col) == (-1,-1):
            return False
        self.permute_case_vide(lig ,col)
        return True
    
    def voisins_du_vide(self):
        '''Taquin --> list(int,int)
        '''

        coords = []
        lig,col = self.__coords_vide
        
        if lig > 0:
            coords.append((lig - 1, col))
        if lig < self.__dim - 1:
            coords.append((lig + 1, col))
        if col > 0:
            coords.append((lig, col - 1))
        if col < self.__dim - 1:
            coords.append((lig, col + 1))
        
        return coords

    def coords(self, val):
        '''Taquin, int --> int,int
        '''
        
        for l,c in self.voisins_du_vide():
            if self.__plateau[l][c] == val:
                return l,c
        
        return -1,-1
    
    def permute_case_vide(self, lig, col):
        '''Taquin (modif), int, int --> None
        '''
        
        l_vide,c_vide = self.__coords_vide
        
        self.__plateau[l_vide][c_vide] = self.__plateau[lig][col]
        self.__plateau[lig][col] = -1

        self.__coords_vide = (lig,col)
    
    def reinit(self):
        '''Taquin (modif) --> None
        '''
        
        for k in range(self.__dim*1000):
            candidats = self.voisins_du_vide()
            ind = randint(0, len(candidats) - 1)
            self.permute_case_vide(candidats[ind][0], candidats[ind][1])

    def partie_finie(self):
        '''Taquin --> bool
        '''
        
        for i in range(self.__dim):
            for j in range(self.__dim):
                if self.__plateau [i][j] != (i*self.__dim )+j+1 and not self.est_vide(i,j):
                    return False
        return True

### fin de la classe Taquin

def main() :
    taq = Taquin()
    print(taq)
    taq.reinit()
    while not taq.partie_finie():
        print(taq)
        choix = int(input("Quelle valeur voulez-vous bouger ? "))
        res = taq.bouge_case(choix)
        if not res :
            print("Non, ce n'est pas possible avec cette valeur.")
    print(taq)
    print("Partie finie. Bravo")


### script principal
if __name__ == '__main__' :
    main()
