############################
#
# Jeu du cavalier
# ---------------
#
# Auteur: Nicolas Méloni
# Mars 2018
# Université de Toulon
#
############################

import tkinter as tk
from PIL import Image, ImageTk  


EMPTY = 0
KNIGHT = 1
PAWN_W = 2
PAWN_B = 3

K_SQUARES = [(1,-2),(2,-1),(2,1),(1,2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

NBL,NBC=8,8
SIDE = 30
COLORS = ['Cornsilk','Sienna']

STATE_NONE = 0
STATE_SHOW_MOVES = 1
STATE_WON = 2

PUZZLES = [[(4, 4, 5), [(0, 2)], [(1, 0), (2, 3), (3, 2)], [(3, 0)]],
           [(5,5,4),[(0,0)],[(1,2)],[(2,4)]],
           [(6, 6, 6), [(0, 0)], [(0, 1), (1, 2), (3, 4)], [(5, 5)]],
           [(6, 6, 6), [(0, 1)], [(1, 4), (2, 1), (2, 3), (2, 5), (3, 0), (3, 3), (3, 4), (4, 3)], [(5, 4)]],
           [(5, 5, 9), [(0, 2)], [(2, 1), (2, 2), (2, 3)], [(4, 2)]],
           [(6, 6, 7), [(0, 5)], [(1, 4), (2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4), (4, 2), (4, 4), (5, 2)], [(5, 5)]],
           [(6, 6, 7), [(0, 0)], [(0, 1), (0, 2), (1, 2), (3, 3), (4, 2)], [(5, 4)]],           
           [(6, 6, 8), [(0, 0)], [(0, 4), (2, 1), (3, 1), (3, 2), (3, 3)], [(4, 0)]],
           [(4, 8, 9), [(0, 0)], [(0, 1), (1, 2), (1, 3), (2, 2), (2, 3)], [(3, 0)]],
           [(4, 8, 11), [(0, 1)], [(1, 2), (1, 3), (1, 4), (2, 2), (2, 3)], [(3, 1)]],
           [(9, 10, 8), [(0, 4)], [(0, 8), (2, 0), (2, 3), (2, 4), (2, 5), (2, 8), (3, 1), (3, 2), (3, 3), (3, 5), (3, 6), (3, 7), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (6, 1)], [(4, 4)]],
           [(21, 24, '?'), [(0, 10)], [(1, 7), (1, 16), (2, 6), (2, 10), (2, 14), (2, 19), (3, 7), (3, 9), (3, 11), (4, 4), (4, 6), (4, 8), (4, 10), (4, 19), (4, 21), (5, 2), (5, 4), (5, 8), (5, 12), (5, 18), (5, 19), (5, 20), (5, 21), (5, 22), (6, 9), (6, 11), (6, 15), (6, 17), (6, 18), (6, 19), (6, 21), (7, 5), (7, 6), (7, 8), (7, 10), (7, 12), (7, 14), (7, 16), (7, 17), (7, 18), (8, 4), (8, 6), (8, 7), (8, 9), (8, 11), (8, 13), (8, 15), (8, 17), (8, 19), (8, 20), (9, 2), (9, 8), (9, 10), (9, 12), (9, 14), (9, 16), (10, 4), (10, 6), (10, 9), (10, 11), (10, 13), (10, 15), (10, 18), (10, 19), (10, 21), (10, 23), (11, 7), (11, 8), (11, 9), (11, 10), (11, 14), (11, 15), (11, 18), (11, 19), (11, 20), (11, 22), (12, 3), (12, 6), (12, 7), (12, 8), (12, 9), (12, 19), (12, 21), (12, 23), (13, 2), (13, 3), (13, 5), (13, 6), (13, 7), (13, 8), (13, 15), (13, 17), (13, 18), (13, 20), (13, 22), (14, 2), (14, 6), (14, 7), (14, 8), (14, 9), (14, 14), (14, 15), (14, 17), (14, 18), (14, 19), (15, 5), (15, 8), (15, 10), (15, 18), (15, 20), (16, 3), (16, 8), (16, 9), (16, 15), (16, 17), (16, 19), (17, 7), (17, 8), (17, 9), (17, 18), (18, 6), (18, 16), (18, 19), (18, 21), (19, 9), (20, 8), (20, 16)], [(20, 20)]]]
           

class Engine():
    def __init__(self, parent, *args, **Kwargs):
        self.app = parent
        self.tries = 0
        self.max_tries = 0
        self.nb_goals = 0
        self.init_board(NBL,NBC)
        self.moves = []
        
    def init_board(self,nbl,nbc):
        self.nbl=nbl
        self.nbc=nbc
        self.board = [[0]*self.nbc for i in range( self.nbl )]

    def set_board(self, puzzle):
        """Initialize the chess board according to the parameters stored in
        <puzzle>: 

        [(nbc, nbl,max_tries), [knight sq], [white pawn sq], [black
        pawn sq] ]

        """
        self.tries = 0
        self.moves = []
        self.max_tries = puzzle[0][2]
        self.init_board(puzzle[0][0],puzzle[0][1])
        self.nb_goals = len(puzzle[PAWN_B])
        for piece in [KNIGHT,PAWN_W,PAWN_B]:
            for l,c in puzzle[piece]:
                self.board[l][c]=piece
        
    def move(self,start,end):
        ls,cs = start
        le,ce = end
        piece = self.board[ls][cs]
        goal = self.board[le][ce]
        if goal == PAWN_B:
            self.nb_goals -= 1
        self.board[ls][cs] = EMPTY
        self.board[le][ce] = piece
        self.inc_tries(1)
        self.moves.append((end))
        

    def move_list(self,start):
        lmove = []
        ls,cs = start
        piece = self.board[ls][cs]
        if piece == KNIGHT:
            for dx,dy in K_SQUARES:
                l,c = ls+dx,cs+dy
                if 0<=l<self.nbl and 0<=c<self.nbc and self.board[l][c] in [EMPTY,PAWN_B]:
                    lmove.append((l,c))
                    
        #elif piece == PAWN_W:
        #    if 0<=ls-1 and self.board[ls-1][cs]==EMPTY:
        #        lmove=[(ls-1,cs)]
        #elif piece == PAWN_B:
        #    if ls+1<self.nbl and self.board[ls+1][cs]==EMPTY:
        #        lmove=[(ls+1,cs)]
        return lmove

    def inc_tries(self, inc):
        self.tries += inc
        


class Board(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.app = parent
        self.side = SIDE
        self.engine = parent.engine
        self.state = STATE_NONE
        self.piece = EMPTY
        self.drawn_piece = []
        self.width = self.engine.nbc*SIDE
        self.height = self.engine.nbl*SIDE
        self.board = tk.Canvas(self,
                               width=self.width,
                               height=self.height,
                               bg='white')
        self.init_game()
        self.board.pack(fill="both",expand=True)
        self.board.bind("<Button-1>", self.click)


    def init_game(self):
        self.width = self.engine.nbc*SIDE
        self.height = self.engine.nbl*SIDE
        self.board.config(width=self.width,height=self.height)
        self.grid = [[] for i in range(self.engine.nbl)]
        for i in range(self.engine.nbl):
            for j in range(self.engine.nbc):
                self.grid[i].append(self.board.create_rectangle( j*self.side+1,i*self.side+1,
                                                                 (j+1)*self.side+1,(i+1)*self.side+1,
                                                                 fill=COLORS[(i+j)%2]))
        

    def delete_board(self):
        for line in self.grid:
            for square in line:
                self.board.delete(square)
        for p in self.drawn_piece:
            self.board.delete(p)

    def draw_piece(self,piece,l,c):
        self.drawn_piece.append(self.board.create_image((c+0.5)*SIDE,(l+0.5)*SIDE,image=self.app.images[piece]))

    def draw_game(self):
        self.delete_board()
        self.init_game()
        for i in range(self.engine.nbl):
            for j in range(self.engine.nbc):
                if self.engine.board[i][j]!=EMPTY:
                    self.draw_piece(self.engine.board[i][j],i,j)
        self.app.menu.var_tries.set(str(self.engine.tries))
        self.app.menu.var_max_tries.set(str(self.engine.max_tries))
        self.app.menu.var_moves.set(str(self.engine.moves))
        
    def click(self,event):
        l,c = self.square_num(event)
        board = self.engine.board
        piece = board[l][c]
        if self.state == STATE_NONE:
            if piece!= EMPTY:
                lmove = self.engine.move_list((l,c))
                self.change_color(lmove,'Lightgreen')
                self.state = STATE_SHOW_MOVES
                
        elif self.state == STATE_SHOW_MOVES:
            if self.piece in [KNIGHT,PAWN_W]:
                lmove = self.engine.move_list(self.prev_click)
                if (l,c) in lmove:
                    self.engine.move(self.prev_click,(l,c))
            self.draw_game()
            self.state = STATE_NONE
        if self.engine.nb_goals == 0:
            self.state = STATE_WON
        self.prev_click = (l,c)
        self.piece = piece


    def change_color(self, squares, color):
        self.draw_game()
        for l,c in squares:
            self.board.itemconfig(self.grid[l][c], fill=color)
     

    def square_num(self, event):
        return event.y // SIDE, event.x // SIDE

    def change_side(self, size):
        self.side = size
        

class Menu(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.app = parent
        self.level_nb = 0
        self.engine = parent.engine
        self.board = parent.board
        self.var_level = tk.StringVar()
        self.var_tries = tk.StringVar()
        self.var_max_tries = tk.StringVar()
        self.var_moves = tk.StringVar()
        
        self.info = tk.Frame(self)
        self.tries = tk.Label(self.info, textvariable=self.var_tries, font=("Helvetica", 16))
        self.bar = tk.Label(self.info,text=" / ", font=("Helvetica", 16))
        self.max_tries = tk.Label(self.info, textvariable=self.var_max_tries, font=("Helvetica", 16))

        self.moves = tk.Label(self.app, textvariable=self.var_moves, font=("Helvetica", 16))

        self.level = tk.Label(self, textvariable=self.var_level,font=("Helvetica", 16))
        self.level.pack(side='top')

        self.boutons = tk.Frame(self)
        self.bouton_next = tk.Button(self.boutons, image=self.app.images[4],command=self.prev_level)
        self.bouton_prev = tk.Button(self.boutons, image=self.app.images[5],command=self.next_level)
        self.boutons.pack(side='top')
        
        self.info.pack(side='top')
        self.max_tries.pack(side="right",expand=False)
        self.bar.pack(side="right", expand=False)
        self.tries.pack(side="right", expand=False)

        #self.moves.pack(side='bottom',expand=False)

        self.bouton_next.pack(side="left")
        self.bouton_prev.pack(side="right")
        


    def load_level(self):
        pzl = PUZZLES[self.level_nb]
        self.engine.set_board(pzl)
        self.board.state = STATE_NONE
        self.var_level.set("Niveau "+ str(self.level_nb+1))
        self.board.draw_game()        

    def next_level(self):
        if self.level_nb < len(PUZZLES)-1:
            self.level_nb += 1
        self.load_level()

    def prev_level(self):
        if self.level_nb > 0:
            self.level_nb -= 1
        self.load_level()

class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent

        self.root.title("Jeu du cavalier")

        self.engine = Engine(self)

        self.img_name = ["cavalier.png","pion.png","pion_noir.png","left.png","right.png"]
        self.init_images()
        
        self.board = Board(self)
        self.board.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        self.menu = Menu(self)
        self.menu.pack(side="left", padx=10, pady=10, fill="both", expand=True)
        self.menu.load_level()
        
        
    def init_images(self):
        self.images={}
        for i in range(len(self.img_name)):
            name = self.img_name[i]
            image = Image.open(name)
            image=image.resize((SIDE,SIDE),Image.ANTIALIAS)
            img = ImageTk.PhotoImage(image)            
            self.images[i+1]=img

    def mainloop(self):
        self.root.mainloop()

if __name__=='__main__':
    App = MainApp(tk.Tk())
    App.pack(side="top", fill="both", expand=True)
    App.mainloop()
