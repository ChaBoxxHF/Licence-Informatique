def Gray(N):
    if N==0:
        return(0)
    if N==1:
        return(1)
    gray=""
    n2=N//2
    n=bin(N)
    n2=bin(n2)
    n=str(n[2:])
    n2=str("0"+n2[2:])
    i=0
    while i<len(n2):
        if n[i] =="1" and n2[i]=="1":
            gray+="0"
        elif n[i] == "1" or n2[i]=="1":
            gray+="1"
        else:
            gray+="0"
        i+=1
    a=int(gray,2)
    return a
          

def Inverse(n,x):
    for i in range(n):
        if x*i%n==1:
            return i
    return 0

#marche pas#
def Orbite(s,x):
    l=[]
    lord=[]
    i=0
    while i<len(s):
        lord+=[i+1]
        i+=1
    orb=[]
    i=0
    while i<len(s):
        ind=s.index(temp)
        temp=lord[ind]
        if temp not in l:
            l.append(temp)
        i+=1
    temp=min(l)
    i=0
    return tuple(l)

def EstTransitive(R):
    i=0
    l=[]
    while i<len(R):
        l+=R[i]
        i+=1
    j=1
    cpt=0
    while cpt<len(l):
        if l[i[1]]==l[j[0]] or l[j+1[0]]:
            return True
        else:
            return False

def EstSousSequence(u,v):
    if u=="":
        return True
    if len(u)>len(v):
        return False
    i=0
    j=0
    cpt=0
    while i<len(v) and j<len(u):
            if u[j]==v[i]:
                cpt+=1
                j+=1
            i+=1
    if cpt==len(u):
        return True
    else:
        return False
