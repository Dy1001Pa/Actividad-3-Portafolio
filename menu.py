from productos import agregar_producto, modificar_precio, eliminar_producto, mostrar_productos, productos
from calculos import pedir_cantidad, calcular_total_por_producto, calcular_total_general, cantidades  # Importar cantidades

def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Gestionar Productos")
        print("2. Realizar Cálculos")
        print("3. Mostrar Resumen de Compra")
        print("4. Salir")

        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            menu_gestion_productos()
        elif opcion == 2:
            menu_calculos()
        elif opcion == 3:
            mostrar_resumen_compra()
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_gestion_productos():
    while True:
        print("\nGestión de Productos:")
        print("1. Agregar Producto")
        print("2. Modificar Precio")
        print("3. Eliminar Producto")
        print("4. Mostrar Productos")
        print("5. Volver al Menú Principal")

        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            modificar_precio()
        elif opcion == 3:
            eliminar_producto()
        elif opcion == 4:
            mostrar_productos()
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_calculos():
    while True:
        print("\nMenú de Cálculos:")
        print("1. Pedir Cantidad de Productos")
        print("2. Calcular Total por Producto")
        print("3. Calcular Total General")
        print("4. Volver al Menú Principal")

        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            pedir_cantidad(productos)
        elif opcion == 2:
            calcular_total_por_producto(productos)
        elif opcion == 3:
            calcular_total_general(productos)
        elif opcion == 4:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def mostrar_resumen_compra():
    if not productos or not cantidades:
        print("No hay productos ni cantidades para mostrar.")
        return
    print("\nResumen de la Compra:")
    for nombre, precio in productos.items():
        cantidad = cantidades.get(nombre, 0)
        total_producto = precio * cantidad
        print(f"{nombre} - Precio unitario: ${precio:.2f}, Cantidad: {cantidad}, Total: ${total_producto:.2f}")
    calcular_total_general(productos)

menu_principal()
