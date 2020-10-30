L=[-2]
i=0
maxi=-10**90
mini=10**90
while L!=[] and i<len(L):
    a=int(input())
    L=L+[a]
    if L[i]>maxi:
        maxi=L[i]
    if L[i]<mini:
        mini=L[i]
    i+=1
print("min =",mini)
print("max =",maxi)

