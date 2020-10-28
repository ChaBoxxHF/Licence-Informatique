#fichier geometrie 2d de Crochard pascal 10/12/18
from math import *
from pocketgl import *
from vecteur import *

def mat_rotation_2d(theta):
    m=([(cos(theta),-sin(theta)),(sin(theta),cos(theta))])
    return(m)
def rotation_point_2d(p,c,theta):
    d=diff_vect(p,c)
    point=prod_mat_vec(d,mat_rotation_2d(theta))
    x=somme_vect(point,c)
    return(x)
def dessine_polygone_2d(pol):
    init_window("geometrie",1920,1080)
    i=0
    while i<len(poly)-1:
        line(poly[i][0],poly[i][1],poly[i+1][0],poly[i+1][1],1)
        i+=1
    main_loop()
def rotation_polygone_2d(p,c,theta):
    
