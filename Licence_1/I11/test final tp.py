def jumeaux(p1,p2):
    if p2-p1==2:
        return(True)
    else:
        return(False)

def som_div_propre(n):
    som=0
    i=1
    while i<n:
        if n%i==0:
            som+=i
            i+=1
        else:
            i+=1

def affiche_jumeaux(k):
    i=1
    while i<2**k: 
        if som_div_propre(k)==1 and som_divpropre(k+2)==1:
            return(k,k+2)
            i+=1
        else:
            i+=1
