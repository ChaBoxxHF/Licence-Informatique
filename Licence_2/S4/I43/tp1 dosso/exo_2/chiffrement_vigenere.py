def chiffrement(message, cle):
    code = ""
    for i, c in enumerate(message):
        d = cle[i % len(cle)]
        d = ord(d) - 97
        code += chr((ord(c)-97+d) % 26+97)
    return code

message= "messagertresmesquinmesopotamien"
key= "test"
print(chiffrement(message,key))