# Demander à l'utilisateur de saisir son âge
saisie_age = input("Veuillez saisir votre âge : ")

# Convertir 
try:
    age = int(saisie_age)
   
    if age < 0:
        print("Erreur : L'âge ne peut pas être négatif.")
    else:
        
        if age <= 12:
            categorie = "Enfant"
        elif age <= 17:
            categorie = "Adolescent"
        elif age <= 64:
            categorie = "Adulte"
        else:
            categorie = "Senior"
        
        # Afficher le message final
        print(f"Vous avez {age} ans, vous êtes dans la catégorie : {categorie}.")
        
except ValueError:
    print("Erreur : Veuillez saisir un nombre valide pour l'âge.")