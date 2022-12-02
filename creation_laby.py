def creer_labyrinthe(self,x, y):
    """ 
    """
    self.x = x
    self.y = y
#les murs sont dans l'ordre : N, S, E, O. 
#la valeur est à True si un mur est présent, False sinon
    self.murs = {'N': True, 'S': True, 'E': True, 'O': True}

class Grille :
    """
    construction d'une grille de cellule
    """

    def __init__(self, nb_lig, nb_col):
        """
        construction d'une grille de dimension (nb_lig, nb_col)
        """

        self.nb_lig = nb_lig
        self.nb_colnb_colnc
        self.cadrillage = []
        for i in range(nb_lig):
            GrilleLigne=[]
            for j in range(nb_col):
                GrilleLigne.append(UneCellule(i,j))
            self.cadrillage.append(GrilleLigne)
    def cellule(self, x, y):
        """
        retourne la cellule de la grille de position (x=ligne, y=colonne)
        """

        return self.cadrillage[x][y]
    

    def __str__(self):
        """
        retourne une chaine de caractères représentant le labyrinthe
        pour les cellules touchant le bord gauche ou le bord du haut de la grille, les 4 murs sont représentés.
        pour les autres, seuls les murs Est et Sud sont représentés
        """

        laby_lignes = []
        laby_l = ['+']
        for y in range(self.nc):
            if self.cadrillage[0][y].murs['N']:
                laby_l.append('---+')
            else :
                laby_l.append('   +')
        laby_lignes.append(''.join(laby_l))
        
        for x in range(0,self.nl):
            if self.cadrillage[x][0].murs['O'] :
                laby_l = ['|']
            else :
                laby_l = [' ']
            for y in range(self.nc):
                if self.cadrillage[x][y].murs['E']:
                    laby_l.append('   |')
                else:
                    laby_l.append('    ')
            laby_lignes.append(''.join(laby_l))
            laby_l = ['+']
            for y in range(self.nc):
                if self.cadrillage[x][y].murs['S']:
                    laby_l.append('---+')
                else:
                    laby_l.append('   +')
            laby_lignes.append(''.join(laby_l))

        #laby_lignes.append('\n')
        return '\n'.join(laby_lignes)


if __name__ == "__main__":
    # Lance le test de la fonction creer_labyrinthe()
    Labyrinthe = creer_labyrinthe(4, 3, 30)
    m = nx.adjacency_matrix(Labyrinthe)
    print(m)

