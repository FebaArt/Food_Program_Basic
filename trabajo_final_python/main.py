from history import view_order_history
from menu import mostrar_menu
from orders import take_order


def main():
    while True:
        #mostrar el menú de opciones
        mostrar_menu()
        option = input("Seleccione una opción:")

        if option == "1":
            #pedir una comida al usuario
            take_order() 
        elif option == "2":
            #ver el historial de pedidos
            view_order_history()
        elif option == "3":
            print("Muchas gracias por usar nuestro sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()