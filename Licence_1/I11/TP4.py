semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
i=0
j=1
m=1
while m<=31:
    print(semaine[i],m,"octobre")
    if i==6:
        i=0
    else:
        i=i+1
    j+=1
    m+=1
    
