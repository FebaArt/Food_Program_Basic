ORDERS_ARCHIVE = "orders_archive.txt"

def view_order_history():
    try:
        print("\nHistorial de pedidos:")
        with open(ORDERS_ARCHIVE, "r", encoding="utf-8") as file: #lee el archivo de historial de pedidos
            orders = file.readlines()
            if orders:
                for i, order in enumerate(orders, start=1):
                    print(str(i) + ", " + order.strip())
            else:
                print("No hay pedidos en el historial.")
    except FileNotFoundError:
        print("No se encontró el archivo de historial de pedidos.")