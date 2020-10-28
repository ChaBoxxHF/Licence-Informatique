L1=[]
L2=[]
ch=["bon","soir","je m'appelle henry","je voudrais bien réussir ma vie"]
i=0
while i<len(ch):
    if len(ch[i])<5:
        L1+=[ch[i]]
    elif len(ch[i])>10:
        L2+=[ch[i]]
    i+=1
print(L1,L2)
