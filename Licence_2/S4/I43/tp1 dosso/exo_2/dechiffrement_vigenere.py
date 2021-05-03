def dechiffrement(message, cle):
    code = ""
    for i, c in enumerate(message):
        d = cle[i % len(cle)]
        d = ord(d) - 97
        d = 26 - d
        code += chr((ord(c)-97+d) % 26+97)
    return code

message = "fikltkwkmvwlfikjnmffxwgihxsfbif"
key = "test"
print(dechiffrement(message,key))