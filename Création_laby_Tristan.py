########
class UneCellule:
    """
    définition d'une cellule
    """
    
    def __init__(self,x, y):
        """
        créer une cellule positionnée en (x=ligne, y=colonne)
        """
        
        self.x = x
        self.y = y
        #les murs sont dans l'ordre : N, S, E, O. 
        #la valeur est à True si un mur est présent, False sinon
        self.murs = {'N': True, 'S': True, 'E': True, 'O': True}

########       
class Grille :
    """
    construction d'une grille de cellules
    """
    
    def __init__(self, nl, nc):
        """
        construction d'une grille de dimension (nl, nc)
        """
        
        self.nl = nl
        self.nc = nc
        self.cadrillage = []
        for i in range(nl):
            GrilleLigne=[]
            for j in range(nc):
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
    
