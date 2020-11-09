def pgcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def euclide_e(a,n):
    u=1
    v=0
    u1=0
    v1=1
    q=0
    while n!=0:
        q=a//n
        tmpa=a
        tmpn=n
        a=n
        n=tmpa%n
        tmpu=u
        tmpv=v
        u=u1
        v=v1
        u1=tmpu-u1*q
        v1=tmpv-v1*q
    return [u,v,a]

def inverse(a,p):
    u, v, u1, v1 , p1 = 1, 0, 0, 1, p
    while a != 0:
        u2 = u - (p1 // a) * u1
        v2 = v - (p1 // a) * v1
        u, v = u1, v1
        u1, v1 = u2, v2
        p1, a = a, p1 % a
    return v%p

def euler_phi(n):
    Zn=0
    i=0
    while i<n:
        a=i
        b=n
        while b>0:
            tmp=a
            a=b
            b=tmp%b
        if a==1:
            Zn+=1
        i+=1
    return Zn

def decompose(n):
    l=[]
    while n!=0:
        l+=[n%b]
        n//=b
    return l[::-1]

def valeur(L,b):
    p=1
    s=0
    i=0
    while i<len(L):
        s+=L[::-1][i]*p
        p*=b
        i+=1
    return s

def decompose(n):
    D,i=set(),2
    while n>1:
        if n%i==0:
            n//=i
            D.add(i)
        else:
            i+=1
    return list(sorted(D))

def ord(a,n):
    pass


def generateurs(n):
    return [i for i in range(n) if pgcd(i, n) == 1]

#print(euclide_e(54,39))
#print(inverse(,))
#print(euler_phi(57))
#print(decompose(30, 5))
#print(valeur([3,2,1],5))
#print(decompose(99999876400))
print(generateurs(6))