print("Choisir 2 nombres :")

a= int(input(" a = "))
b= int(input(" b = "))

op = input("Choisire une opereation d'apres chiffre: (1. Addition/ 2. Soustraction/ 3. Multiplication/ 4.Division) :  ")

resultat = 0

match op :
    case "1" :
        # better than adding another var
        print(f"{a} + {b} = {a + b}")

    case "2" :
        print(f"{a} - {b} = {a - b}")

    case "3" :
        print(f"{a} * {b} = {a * b}")

    case "4" :
        if b == 0 :
            print("ERROR : on ne peus pas diviser sur 0")
             
        else: 
            print(f"{a} / {b} = {a / b}")

