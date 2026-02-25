temperature = 25

if temperature > 20:  
    print("Il fait chaud.")
    print("Pensez à boire de l'eau.")

elif temperature > 10:
    print("Température agréable. ")
    print("Une veste légère suffira.")

elif temperature > 0:
    print("Il fait froid. ")
    print("Manteau, écharpe et gants recommandés.")

elif temperature <0 :
    print("Température glaciale ! Restez au chaud si possible.")

else:
    print("Température Invalid.")
    print("Veuillez entrer un nombre valide !!")

print("Fin du programme.")