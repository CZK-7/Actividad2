#Una Empresa dedicada a la distribución de mercancía requiere el desarrollo de un aplicativo que permita registrar los pedidos solicitados por los diferentes clientes dentro de los cuales se tiene la siguiente información: 
# Nombre del cliente, dirección, contacto, sexo, descripción de la casa o lugar para guiar al personal de entrega. Adicional a ello se debe colocar el nombre del producto, referencia y cantidades a solicitar. Todo esto debe quedar registrado en un diccionario y debe tener la posibilidad de ver todos los pedidos realizados
def registrar_pedido(pedidos):
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    contacto = input("Ingrese el contacto del cliente: ")
    sexo = input("Ingrese el sexo del cliente (M/F): ")
    descripcion_lugar = input("Ingrese la descripción de la casa o lugar: ")
    
    nombre_producto = input("Ingrese el nombre del producto: ")
    referencia = input("Ingrese la referencia del producto: ")
    cantidad = int(input("Ingrese la cantidad a solicitar: "))
    
    pedido = {
        "Nombre del cliente": nombre_cliente,
        "Dirección": direccion,
        "Contacto": contacto,
        "Sexo": sexo,
        "Descripción del lugar": descripcion_lugar,
        "Producto": {
            "Nombre": nombre_producto,
            "Referencia": referencia,
            "Cantidad": cantidad
        }
    }
    
    pedidos.append(pedido)
    print("Pedido registrado con éxito!\n")

# Función para mostrar todos los pedidos
def mostrar_pedidos(pedidos):
    print("Lista de pedidos:")
    for i, pedido in enumerate(pedidos, 1):
        print(f"Pedido {i}:")
        for clave, valor in pedido.items():
            if clave == "Producto":
                for k, v in valor.items():
                    print(f"\t{k}: {v}")
            else:
                print(f"\t{clave}: {valor}")
        print("-" * 50)

# Lista para almacenar los pedidos
pedidos = []

# Menú principal
while True:
    print("Menú Principal")
    print("1. Registrar pedido")
    print("2. Ver todos los pedidos")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_pedido(pedidos)
    elif opcion == "2":
        mostrar_pedidos(pedidos)
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.\n")
