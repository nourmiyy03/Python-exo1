contacts = ["Bouchra", "Ahmed", "Sara"]

# Menu principal
choix = 0  

while choix != 3:
    
    print("\n Choisir une Action : ")

    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Quitter le programme")

    
    try:
        choix = int(input("Votre choix (1-3) : "))
        
        if choix == 1:
            nom = input("Ajouter qui ? : ")
            contacts.append(nom)
            print(f"'{nom}' ajouté avec succès !")
            
        elif choix == 2:
            print("\n--- LISTE DES CONTACTS ---")

            if len(contacts) == 0:
                print("Aucun contact")

            else:

                for i, contact in enumerate(contacts):
                    print(f"   {i+1}. {contact}")

            
            
        elif choix == 3:
            print("\n Bye YOU !")
            
        else:
            print("Choix invalide ! Veuillez saisir 1, 2 ou 3.")
            
    except ValueError:
        print("Erreur : Veuillez saisir un nombre (1, 2 ou 3).")

