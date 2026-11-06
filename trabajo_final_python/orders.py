ORDERS_ARCHIVE = "orders_archive.txt"

def take_order():
    print("Elige una comida que prefieras")
    print("1. Pizza")
    print("2. Hamburguesa")
    print("3. Ensalada")
    print("4. Sushi")
    print("5. Pasta")

    option = input("Seleccione una opción:")

    foods = {
        "1": "Pizza",
        "2": "Hamburguesa",
        "3": "Ensalada",    
        "4": "Sushi",
        "5": "Pasta"
    }

    if option in foods:
        food_order = foods[option]
        print(f"Tu pedido de {food_order} ha sido registrado.")

        with open(ORDERS_ARCHIVE, "a", encoding="utf-8") as file:
            file.write(f"{food_order}\n")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")




