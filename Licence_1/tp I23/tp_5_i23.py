def chiffrer(clair,clé):
    l=[]
    i=0
    while i<len(clair):
        r=0
        if ord(clair[i])+clé>90:
            r=(ord(clair[i])+clé)-90
            l+=[r+64]
        elif ord(clair[i])==32:
            l+=[ord(clair[i])]
        else:
            l+=[ord(clair[i])+clé]
        i+=1
    crypt=""
    for j in range(len(l)):
        crypt+=chr(l[j])
    return crypt

def cribblage(n):
    cribble=[]
    l=[]
    i=2
    while i<n:
        if i not in cribble:
            j=i
            while j<n:
                if j%i==0:
                    cribble+=[j]
                j+=1
            l+=[i]
        i+=1
    return tuple(l)
        
def Factoriser(N):
   p = 2
   facteurs = ()
   while (N % p == 0):
      facteurs = facteurs + (p,)
      N = N // p
   p = 3
   while (p*p <= N):
      while (N % p == 0):
         facteurs = facteurs + (p,)
         N = N // p
      p = p + 2
   if (N != 1):
      facteurs = facteurs + (N,)
   return facteurs