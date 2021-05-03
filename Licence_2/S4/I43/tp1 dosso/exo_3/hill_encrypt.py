def test(message):
    l=[]
    for i in range(len(message)):
        l+=[ord(message[i])]
    i=0
    j=0
    print(l)
    l2=[]
    while i<len(l)//2:
        l2+=[[l[j],l[j+1]]]
        i+=1
        j+=2
    return l2

message= "hakuna matata"
print(test(message))