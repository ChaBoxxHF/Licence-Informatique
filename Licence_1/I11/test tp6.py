def prod_scal(u,v):
    a=0
    T=0
    while a<len(u):
        T=T+(u[a]*v[a])
        a+=1
    return (T)
