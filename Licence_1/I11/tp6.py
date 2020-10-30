from pocketgl import *
from random import *

i=0
l=[0,0,0,0,0,0]
while i<10000:
    if randrange(1,7)==1:
        l[0]+=1
    elif randrange(1,7)==2:
        l[1]+=1
    elif randrange(1,7)==3:
        l[2]+=1
    elif randrange(1,7)==4:
        l[3]+=1
    elif randrange(1,7)==5:
        l[4]+=1
    elif randrange(1,7)==6:
        l[5]+=1
    i+=1
print(l)




init_window("premiers pas", 500,500)
i,j,k,l=0,0,500,0
r,g,b=35,35,35

current_color(r,g,b)
while l<500:
    line(i,j,k,l,10)
    r+=5
    g+=5
    b+=5
    current_color(r,g,b)
    j+=10
    l+=10
