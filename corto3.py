productos  = []

for i in range(3): 
    print( f"\n Producto {i+1}: " )
    nombre = input("Nombre del producto: ")
    precio = int(input("Precio del producto en Q: "))
    stock = int(input("Cantidad en stock: "))

    producto = {
        "nombre" : nombre,
        "precio" : precio,
        "stock": stock
    }
    productos.append(producto)

    print("\n Productos")
    for j in productos:
        print( f"El producto {j['nombre']} cuesta {j['precio']} y quedan {j['stock']} unidades disponibles" )