#fichier vecteur de pascal crochard le 10/12/18
def somme_vect(u,v):
    som=()
    i=0
    while i<len(u):
        som+=(u[i]+v[i],)
        i+=1
    return(som)

def diff_vect(u,v):
    diff=()
    i=0
    while i<len(u):
        diff+=(u[i]-v[i],)
        i+=1
    return(diff)

def prod_scal(u,v):
    prod=0
    i=0
    while i<len(u):
        prod+=u[i]*v[i]
        i+=1
    return(prod)

def prod_mat_vec(u,m):
    i=0
    prod=[]
    i=0
    while i <len(m):
        prod+=[prod_scal(u,m[i])]
        i+=1
    return(prod)
