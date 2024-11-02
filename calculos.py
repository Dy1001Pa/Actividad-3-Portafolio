cantidades = {}

def pedir_cantidad(productos):
    if not productos:
        print("No hay productos registrados aún.")
        return
    for nombre in productos.keys():
        cantidad = int(input(f"Ingrese la cantidad de '{nombre}': "))
        cantidades[nombre] = cantidad

def calcular_total_por_producto(productos):
    if not productos or not cantidades:
        print("No hay productos ni cantidades para calcular.")
        return
    for nombre, precio in productos.items():
        cantidad = cantidades.get(nombre, 0)
        total_producto = precio * cantidad
        print(f"{nombre} - Cantidad: {cantidad}, Total: ${total_producto:.2f}")

def calcular_total_general(productos):
    if not productos or not cantidades:
        print("No hay productos ni cantidades para calcular.")
        return
    total_general = sum(precio * cantidades.get(nombre, 0) for nombre, precio in productos.items())
    print(f"Total general de la compra: ${total_general:.2f}")
