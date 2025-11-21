
def add(inventario):
    check = True
    while check:
        nombre = input("Nombre del producto: ").strip()
        if not nombre : 
            print("el nombre no puede estar vacio")
            continue
        valor = input("Precio: ").strip()
        try:
            precio = float(valor)
            if precio > 0:
                break
            else:
                print("Digite un precio válido (mayor que 0).")
        except ValueError:
            print("Digite un valor válido para el precio (ejemplo: 4.99).")

    while check:
        numero = input("Cantidad: ").strip()
        if numero.isdigit():
            cantidad = int(numero)
            if cantidad > 0:
                break
            else:
                print("Digite una cantidad válida (mayor que 0).")
        else:
            print("Digite un número entero para la cantidad.")

    product = {"Nombre": nombre, "Precio": precio, "Cantidad": cantidad}
    inventario.append(product)
#Añadir algun producto 
def view(inventario) : 
    for product in inventario: 
        print(f"Producto: {product['Nombre']}| precio {product['Precio']} | cantidad {product['Cantidad']} ") 
#buscar algun producto       
def search (inventario) : 
    search = input("Nombre del producto: ") 
    locate = False
    for product in inventario: 
        if product['Nombre'] == search: 
            locate = True 
            print(f"Producto: {product['Nombre']}| precio {product['Precio']} | cantidad {product['Cantidad']} ") 
    if locate == False : 
        print("producto no encontrado ") 
#funcion para actualizar datos bajo algunos parametros
def update (inventario) : 
    search = input("Que producto vas a actualizar: ") 
    locate = False 
    check = True
    for product in inventario : 
         if product['Nombre'] == search : 
            locate = True 
            cambiar = input("1. cambiar nombre \n2. cambiar precio \n3. cambiar cantidad \n4. cambiar todo \n5. salir")
            if cambiar == "1" :
                new_name = input("nuevo nombre: ")  
                if not new_name: 
                    print("el nombre no puede estar vacio")
                    continue
                product['Nombre'] = new_name
            elif cambiar == "2" :
                while check:
                    new_price = input("nuevo precio: ")    
                    try:
                        precio = float(new_price)
                        if precio > 0:
                            product['Precio'] = precio
                            break
                        else:
                            print("Digite un precio válido (mayor que 0).")
                    except ValueError:
                        print("Digite un valor válido para el precio (ejemplo: 4.99).")
                    
            elif cambiar == "3" : 
                 while check:
                    numero = input("Cantidad: ").strip()
                    if numero.isdigit():
                        cantidad = int(numero)
                        if cantidad > 0:
                            product['Cantidad'] = cantidad
                            break
                        else:
                            print("Digite una cantidad válida (mayor que 0).")
                    else:
                        print("Digite un número entero para la cantidad.")
                    
            elif cambiar =="4" : 
                new_name = input("nuevo nombre: ")  
                product['Nombre'] = new_name
                while check:
                    new_price = input("nuevo precio: ")    
                    try:
                        precio = float(new_price)
                        if precio > 0:
                            product['Precio'] = precio
                            break
                        else:
                            print("Digite un precio válido (mayor que 0).")
                    except ValueError:
                        print("Digite un valor válido para el precio (ejemplo: 4.99).")
                while check:
                    numero = input("Cantidad: ").strip()
                    if numero.isdigit():
                        cantidad = int(numero)
                        if cantidad > 0:
                            product['Cantidad'] = cantidad
                            break
                        else:
                            print("Digite una cantidad válida (mayor que 0).")
                    else:
                        print("Digite un número entero para la cantidad.")
            else : 
                print("Opcion no valida")
    
    if locate == False: 
        print("Producto no encontrado")    
#eliminar objetos de la lista
def delete(inventario) : 
    search = input("Que producto vas a eliminar: ") 
    locate = False
    for product in inventario : 
        if product['Nombre'] == search : 
            inventario.remove(product) 
            locate = True
    if locate == False : 
        print("producto no encontrado")
#funcion para calcular los objetos de la lista             
def calcularEstadistica(inventario) : 
   
    if not inventario: 
        print("No hay productos en el inventario") 
        return
    unidadesTotales = sum(i['Cantidad'] for i in inventario)
    ValorProductos = sum(i['Precio'] * i['Cantidad'] for i in inventario)
    ProductoCaro = max(inventario, key=lambda p: p["Precio"])
    mayorCantidad = max(inventario, key=lambda p: p["Cantidad"])  
    print(f"Unidades : {unidadesTotales} | valor total de los productos: {ValorProductos} \nProducto mas caro:  {ProductoCaro["Nombre"]} precio {ProductoCaro["Precio"]} | mayor cantidad de productos: {mayorCantidad["Nombre"]} cantidad {mayorCantidad["Cantidad"]}")
     
    