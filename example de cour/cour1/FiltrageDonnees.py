prix_articles = [12.99, 45.50, 8.75, 67.20, 23.40, 89.99, 34.50, 51.30]

# Seuil de prix premium
seuil_premium = 50.0

# Compteurs
articles_premium = 0
total_premium = 0.0

print("Liste complete des prix :")
for prix in prix_articles:
    print("  ", prix, "€")


print("ARTICLES PREMIUM (plus de", seuil_premium, "€) :")


for prix in prix_articles:
    if prix > seuil_premium:
        print("Article premium a ", prix, "€")
        articles_premium += 1
        total_premium += prix

print("Nombre d'articles premium :", articles_premium)
print(f"Valeur totale des articles premium : €{total_premium:.2f}")
print("Moyenne des prix premium :", total_premium / articles_premium, "€")
