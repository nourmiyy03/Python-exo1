try :
    age = int(input("Votre age : "))
    carte_membre = input("Carte membre (oui/non) : ")

    # Conversion en booléen
    a_carte = carte_membre.lower() == "oui"

    if carte_membre not in ['oui', 'non']:
        print("Reponse invalide. Veuillez repondre par 'oui' ou 'non'.")

    
    if age >= 21 and a_carte:
        print("Acces autorise !")
        print("Bienvenue dans l'espace premium.")
        print("Vous avez acces a tous les services.")

    else:
        
        print("Acces refuse.")
        print("Raisons :")

        if age < 21:
            print(" Age min requis : 21 ans")
            print(f"YOU are {age} years old !!")
        if not a_carte:
            print("Raison : Pas de carte membre.")
            
  
except ValueError:
    print("Erreur : Age Invalide ! ")
    