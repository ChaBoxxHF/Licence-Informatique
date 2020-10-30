def ListerVariables(exp):
    vrs=[]
    for ch in exp:
        if ord(ch)>=97 and ord(ch)<=122:
            if not(ch in vrs):
                vrs.append(ch)
    vrs=sorted(vrs)
    return (vrs)

def DicoVariables(L):
    i=0
    dcv={}
    while i<len(L):
        dcv[L[i]]=i
        i+=1
    return dcv

def Int2Bin(ent,n):
    bn=str(bin(ent)[2:])
    while len(bn)<n:
        bn="0"+bn
    return(bn)

def Bin2Bool(bits):
    tf=[]
    for bit in bits:
        tf.append(bool(int(bit)))
    tf=tuple(tf)

def Math2Python(exp,vecteur,DicoVariables):
    res=""
    for ch in DicoVariable.keys():
        if ch in DicoVariables.keys():
            res+=str(vecteur[DicoVariables[ch]])
        elif ch =="!":
            res+="not"
        elif ch =="+":
            res+="or"
        elif ch=="*":
            res+="and"

def TableVerite(exp,DicoVariables):
    nb=max(DicoVariables.values())+1
    i=0
    mtr=[]
    while i<= 2*nb-1:
        ln=[]
        vc=Bin2Bool(Int2Bin(i,nb))
        for el in vc:
            ln.append(int(el))
        ln.append(int(eval(Math2Python(exp,vecteur,Dicovariables))))
        mtr.append(ln)
        i+=1
    return(mtr)

def FNC(TDV, listevar):
    res=""
    for vecteur in TDV:
        if vecteur[-1]==0:
            res+="("
            for kek in listevar.items():
                oof=kek[0]
                if vecteur[kek[1]]==1:
                    oof+="\u0304"
                res+=oof
                if kek!= list(listevar.items())[-1]:
                    res+="+"
                res+=")"
        return (res)
    if __name__ =="__main__":
        kek= input("entrez une expression:")
        lst=listvar(kek)
        oof=DicoVariables(lst)
        uwu=TableVerite(kek,oof)
        fnd=FND(uwu,oof)
        fnc=FNC(uwu,oof)
        print("Matrice de vérité de l'expression:")
        print(lst)
        for vecteur in uwu:
            print(vecteur[:-1],"=",vecteur[-1])
        print("FND(f) = "+str(fnd))
        print("FNC(f) = "+str(fnc))
