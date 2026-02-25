
MOT_DE_PASSE_CORRECT = "python123"

mot_de_passe = ""

print("\n Veuillez entrer votre mot de passe pour accéder au système.")

# Boucle while - tant que le mot de passe est incorrect
while mot_de_passe != MOT_DE_PASSE_CORRECT:
    mot_de_passe = input("Mot de passe : ")
    
    if mot_de_passe != MOT_DE_PASSE_CORRECT:
        print("Mot de passe incorrect. Réessayez.\n")

# Message de confirmation

print("CONNEXION RÉUSSIE !")

print("\n Hello YOU ! \n")

