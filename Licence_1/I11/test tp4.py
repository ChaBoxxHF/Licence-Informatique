ch = input()
car = input()
cp = ""
i=0
while i<len(ch):
    if ch[i]==car:
        cp=cp+ch[i]*2
    else:
        cp=cp+ch[i]
    i+=1
print(cp)
