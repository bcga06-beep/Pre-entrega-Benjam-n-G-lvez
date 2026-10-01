#Pre-entrega.

stock = [["Chile", "Verdulería", "101"],["Rúcula","Verdulería","98"],["Ramen","Almacén","67"],["Huevo","Almacén","76"]]

print("-------------------------------------------------------------------------")
print("Usted está en el sistema de gestión del mejor local de ramen del internet")
print("-------------------------------------------------------------------------")

opciónElegida = ""

while opciónElegida != "6":
    print("--------Menú--------")
    print("1. Añadir un producto")
    print("2. Visualizar un producto")
    print("3. Buscar un producto")
    print("4. Eliminar un producto")
    print("5. Calcular ramen especial de la casa")
    print("6. Salir")
    print("--------------------")
    opciónElegida = input("Elija una opción para continuar la gestión\n1/2/3/4/5/6: ").strip()
    
    match opciónElegida:
        case "1":
            print("")
            print("###################################")
            print("Usted está agregando un producto...")
            print("")
            print("Para volver escriba: 0")
            print("###################################")
            print("")

            nombreProducto = input("Nombre del producto: ")
            if nombreProducto != "0":
                categoriaProducto = input("Categoria del producto: ")
                precioProducto = input("Precio del producto: $")
            else:
                continue
            stock.append([nombreProducto, categoriaProducto, precioProducto])
            
            print("Producto agregado al sistema")
            
        case "2":
            print("")
            print("Usted está visualizando los productos: ")
            print("")
            contador = 1

            
            for producto in stock:
                print(f"Numero: {contador}")
                print("Producto:", producto[0])
                print("Categoria:", producto[1])
                print(f"${producto[2]}")
                print("---------")
                print("")
                contador = contador + 1
            
        case "3":
            print("")
            print("##################################")
            print("Usted está buscando un producto...")
            print("")
            print("Para volver escriba: 0\n")
            print("###################################")
            print("")
            busqueda = input("Que producto buscas?: ").strip().title()
            encontrado = False
            
            for producto in stock:
                if busqueda == producto[0]:
                    encontrado = True
                    print("---------")
                    print("Producto encontrado!")
                    print("Producto:", producto[0])
                    print("Categoria:", producto[1])
                    print("Precio: $", producto[2])
                    print("---------")
                    print("")

            if busqueda == "0":
                continue
            
            if encontrado == False:
                print("Producto no encontrado")
            
            
        case "4":
            print("")
            print("####################################")
            print("Usted está eliminando un producto...")
            print("")
            print("Para volver escriba: 0")
            print("####################################")
            print("")

            #Pedir que quiere Eliminar
            productoAEliminar= input("Que producto quiere eliminar?: ")
            encontrado = False
            
            for producto in stock:
                if productoAEliminar == producto[0]:
                    encontrado = True
                    print("---------")
                    print("Producto encontrado!")
                    print("Producto:", producto[0])
                    print("Categoria:", producto[1])
                    print("Precio: $", producto[2])
                    print("---------")
                    print("")
                    
                    decision = input(f"Estás seguro de querer eliminar {producto[0]} Si/No: ")
                    if decision == "Si":
                        stock.remove(producto)
                        print("Producto eliminado")

            if productoAEliminar == "0":
                continue
            
            if encontrado == False:
                print("El producto que buscas eliminar, ya no existe")  

        case "5":
            ingredientes = ["Chile", "Ramen", "Huevo"]
            total = 0
            for nombre in ingredientes:
                for producto in stock:
                    if producto[0] == nombre:
                        total += int(producto[2])
                        break
            print("")
            print("#########################################")
            print(f"El precio del Ramen Picante es: ${total}")
            print("#########################################")
            print("")
        
        case "6":
            print("")
            print("##################################")
            print("Gestión finalizada, hasta la próxima")
            print("##################################")
            print("")
        case _:
            print("")
            print("##################################")
            print("Opcion no valida...")
            print("##################################")
            print("")