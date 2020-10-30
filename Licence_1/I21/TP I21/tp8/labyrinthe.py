import tkinter as tk
from pilefile import *
from chemin import chemin
from prim import *

PAUSE  = 200
COTE   = 20
HAUTEUR, LARGEUR = 13, 13
STATE_NONE = 0
STATE_PARCOURS = 1

        
class Canevas(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.state = STATE_NONE
        self.app = parent
        self.cote = COTE
        self.largeur = LARGEUR
        self.hauteur = HAUTEUR
        self.canevas = tk.Canvas(self,
                                 width =self.largeur*self.cote,
                                 height=self.hauteur*self.cote,
                                 bg='white')
        self.canevas.pack(fill="both",expand=True)
        self.labyrinthe = []
        
        

    def gen_grille(self):
        self.grille = prim_maze(self.hauteur,self.largeur)
        self.canevas.config(width=self.largeur*self.cote, height = self.hauteur*self.cote)

        
    def init_labyrinthe(self):
        self.effacer_labyrinthe()
        self.labyrinthe = [[] for i in range(self.largeur)]
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.labyrinthe[i].append(self.canevas.create_rectangle(i*self.cote, j*self.cote, (i+1)*self.cote, (j+1)*self.cote, outline='white', fill='white'))


    def colorer(self,i,j,coul):
        self.canevas.itemconfig(self.labyrinthe[i][j], fill=coul, outline=coul)

    def dessiner_labyrinthe(self):
        self.largeur = int(self.app.menu.scales[0].get())
        self.hauteur = int(self.app.menu.scales[0].get())
        self.gen_grille()
        self.init_labyrinthe()
        for lig in range(self.hauteur):
            for col in range(len(self.grille[lig])):
                if self.grille[lig][col] == 1:
                    self.colorer(col,lig,"black")
                elif self.grille[lig][col] == 2:
                    self.depart = (lig,col)
                    self.colorer(col,lig,"blue")
                elif self.grille[lig][col] == 3:
                    self.arrivee = (lig,col)
                    self.colorer(col,lig,"green")
        

    def effacer_labyrinthe(self):
        for ligne in self.labyrinthe:
            for case in ligne:
                self.canevas.delete(case)

    def afficher_chemin(self, algo_chemin):
        self.icase = 0
        self.lcase = algo_chemin(self.grille, self.depart,self.arrivee)
        self.lcase = self.lcase[::-1]
        if len(self.lcase) > 1:
            self.after(PAUSE, self.dessiner_parcours)
    
    def dessiner_parcours(self):
        if self.state == STATE_NONE:
            return
        self.colorer(self.lcase[self.icase][1],self.lcase[self.icase][0],"red")
        self.icase += 1
        self.colorer(self.lcase[self.icase][1],self.lcase[self.icase][0],"blue")
        if self.icase < len(self.lcase)-1:
            self.after(PAUSE, self.dessiner_parcours)

class Menu(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.canevas = self.root.canevas
        self.boutons = [tk.Button(self, text='Gen Labyrinthe',
                                  command=self.prim_maze,
                                  width=20, height=3),
                        tk.Button(self, text="Plus court chemin",  
                                  command=self.chemin_distance,
                                  width=20, height=3) ]
        self.scales = [tk.Scale(self,from_ = 7,to=51,orient=tk.HORIZONTAL,command=self.fix1)]

        self.pack_menu()
        self.pack_scale()

    def fix1(self,n):
        scale =  self.scales[0]
        n = int(n)
        if n%2 == 0:
            scale.set(n-1)
            
    
        
    def pack_menu(self):
        for button in self.boutons[::-1]:
            button.pack(side = "bottom", padx=5, pady=5)

    def pack_scale(self):
        for scale in self.scales[::-1]:
            scale.pack(side = "bottom", padx=5, pady=5)

    def chemin_distance(self):
        self.canevas.state = STATE_PARCOURS
        self.canevas.afficher_chemin(chemin)

    def prim_maze(self):
        self.canevas.state = STATE_NONE
        self.canevas.dessiner_labyrinthe()
                        
class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.title("Labyrinthe")
        self.canevas = Canevas(self)
        self.canevas.pack(side="right", padx=10, pady=10, fill="both", expand=True)
        self.menu = Menu(self)
        self.menu.pack(side="right", padx=10, pady=10, fill="both", expand=True)

    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
   App = MainApp(tk.Tk())
   App.pack(side="top", fill="both", expand=True)
   App.mainloop()

