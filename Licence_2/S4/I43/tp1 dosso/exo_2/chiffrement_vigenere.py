def chiffrement(message,key):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    ALPHABETM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#code permettant de répter la clé si nécessaire 
    k=0
    j=0
    ch=key
    while k<len(message):
        if j==len(key):
            ch+=key
            j=0
        k+=1
        j+=1


    cypher=""
    i=0
    while i<len(message):
        if message[i] in alphabet:
            if ord(message[i])+ord(ch[i])>ord("z"):
                cypher+=chr((ord("a")-1)+ord(message[i])-ord("z"))
            else:
                cypher+=chr(ord(message[i])+ord(ch[i]))
        elif message[i] in ALPHABETM:
            if ord(message[i])+ord(ch[i])>ord("Z"):
                cypher+=chr((ord("A")-1)+ord(message[i])-ord("Z"))
            else:
                cypher+=chr(ord(message[i])+ord(ch[i]))
        elif message[i]==" ":
            cypher+=message[i]
        i+=1
    return cypher

message= "hakuna matata"
key= "eh"
print(chiffrement(message,key))