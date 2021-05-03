from ana_freq_cesar import *

def dechiffrement(message):
    key=ord(occurrence_max(message))-ord("e")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABETM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i=0
    uncypher=""
    while i<len(message):
        if message[i] in alphabet:
            if ord(message[i])+key<ord("a"):
                uncypher+=chr((ord("z")+1)-ord(message[i])+ord("a"))
            else:
                uncypher+=chr(ord(message[i])-key)
        elif message[i] in ALPHABETM:
            if ord(message[i])+key>ord("Z"):
                uncypher+=chr((ord("Z")+1)-ord(message[i])+ord("A"))
            else:
                uncypher+=chr(ord(message[i])-key)
        else:
            uncypher+=message[i]
        i+=1
    return uncypher

message = "egek c gvg ejkhhtg xkc eguct"
print("voici le message a déchiffrer:",message,"\nvoici le message déchiffré:",dechiffrement(message))