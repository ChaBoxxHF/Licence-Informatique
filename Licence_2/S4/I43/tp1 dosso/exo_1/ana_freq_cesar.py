def occurrence_max (ch):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    occurrence=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range (len(alphabet)):
        for j in range (len(ch)):
            if alphabet[i]==ch[j]:
                occurrence[i]=occurrence[i]+1
    maxi= occurrence[0]
    i=0
    cpt=0
    while i<len(occurrence)-1:
        if occurrence[i] > maxi:
            maxi=occurrence[i]
            cpt=i
        i=i+1
    return alphabet[cpt]

