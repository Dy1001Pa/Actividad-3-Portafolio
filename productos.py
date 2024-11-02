productos = {}

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio unitario del producto: "))
    productos[nombre] = precio
    print(f"Producto '{nombre}' agregado con precio unitario de ${precio:.2f}")

def modificar_precio():
    nombre = input("Ingrese el nombre del producto a modificar: ")
    if nombre in productos:
        nuevo_precio = float(input(f"Ingrese el nuevo precio para '{nombre}': "))
        productos[nombre] = nuevo_precio
        print(f"Precio de '{nombre}' actualizado a ${nuevo_precio:.2f}")
    else:
        print("El producto no existe.")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if nombre in productos:
        del productos[nombre]
        print(f"Producto '{nombre}' eliminado.")
    else:
        print("El producto no existe.")

def mostrar_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        print("Productos registrados:")
        for nombre, precio in productos.items():
            print(f"{nombre}: ${precio:.2f}")
