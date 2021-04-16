def chiffrement(message,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABETM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i=0
    cypher=""
    while i<len(message):
        if message[i] in alphabet:
            if ord(message[i])+key>ord("z"):
                cypher+=chr((ord("a")-1)+ord(message[i])-ord("z"))
            else:
                cypher+=chr(ord(message[i])+key)
        elif message[i] in ALPHABETM:
            if ord(message[i])+key>ord("Z"):
                cypher+=chr((ord("A")-1)+ord(message[i])-ord("Z"))
            else:
                cypher+=chr(ord(message[i])+key)
        elif message[i]==" ":
            cypher+=message[i]
        i+=1
    return cypher

message="ceci a ete chiffre via cesar"
key=2
print("voici le message a chiffrer:",message,"\nvoici le message chiffré grace a la clé",key,":",chiffrement(message,key))