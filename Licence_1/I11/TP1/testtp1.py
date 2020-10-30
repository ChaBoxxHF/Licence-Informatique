deniers = int(input("Nombre de deniers : "))
livre= deniers//240
sous= (deniers%240)//12
denier= (deniers%240)%12
print("Valeur correspondante :",livre,"livre(s)",sous,"sou(s)",denier,"denier(s)")
