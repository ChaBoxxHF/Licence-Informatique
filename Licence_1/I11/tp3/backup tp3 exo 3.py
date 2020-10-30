ch = input('Entrez une chaine de caracteres : ')
a=0
b=len(ch)-1
i=0
while i<len(ch)/2:
    if len(ch)%2==1:
        if i==len(ch)/2-0.5:
            print(ch[a])
        else:
            print(ch[a]+ch[b])
    else:
        print(ch[a]+ch[b])
    a+=1
    b-=1
    i+=1
