# Définition des voyelles avec catégories
voyelles = "aeiouAEIOU"
    
    # Saisie utilisateur
phrase = input("Entrez une phrase à analyser : ")
    
if not phrase:
    print(" Phrase vide !")
else :
    print(f"ANALYSE DES VOYELLES")
       
    # Initialisation des compteurs
    cmp = 0   
    # Analyse caractère par caractère
  
    for caractere in phrase:
        if caractere in voyelles:
            cmp += 1

    print("\n RÉSULTATS :")
    print(f"  Total voyelles : {cmp}")

