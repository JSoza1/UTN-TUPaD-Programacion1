# Consigna 1: Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad 

# Mensaje inicial
print("============== Manejo de archivos ==============")

# Manejo seguro de archivo usando with (cierre automatico)
with open("productos.txt", "w") as archivo:
    archivo.write("Mouse,$500,15\n")
    archivo.write("Teclado,$5000,10\n")
    archivo.write("Monitor,$50000,5")

# Consigna 2: Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:

# Producto: Lapicera | Precio: $120.5 | Cantidad: 30 

# Manejo seguro de archivo usando with (cierre automático)
with open("productos.txt", "r") as archivo:
    # Se leen todas las líneas del archivo y las guarda como lista en "lineas"
    lineas = archivo.readlines()             

    # Inicio bucle 
    for linea in lineas:             
        # Se eliminan saltos de línea y se separan los elementos por coma           
        partes = linea.strip().split(",")        
        # Asignacion de valores a variables segun su indice y significado
        nombre = partes[0]                      
        precio = partes[1]                       
        cantidad = partes[2]                     

        # Mensaje mostrando cada elemento
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

# Mensaje final
print("================================================")

# Consigna 3: Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente. 

# Manejo seguro de archivo usando with (cierre automatico)
with open("productos.txt", "a") as archivo:
    nombre = input("Ingreese el nombre de un nuevo producto: ")
    # inicio condicional
    if nombre == "":
        print("Debe ingresar el nombre del producto")
    else:
        precio = input("Ingrese el precio del producto: ")
        if precio == "":
            print("Debe ingresar el precio del producto")
        else:
            cantidad = input("Ingrese la cantidad del producto: ")
            if cantidad == "":
                print("Debe ingresar la cantidad del producto")
            else:
                archivo.write(f"\n{nombre},${precio},{cantidad}")
                print(f"{nombre}, fue agregado con el precio de ${precio} y cantidad {cantidad} al archivo productos.txt")

# Consigna 4: Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.

# Inicializo variables
productos = []

# Manejo seguro de archivo usando with (cierre automatico)
with open("productos.txt", "r") as archivo:
    # Se leen todas las líneas del archivo y las guarda como lista en "lineas"
    lineas = archivo.readlines()

    # Inicio bucle 
    for linea in lineas:
        # Se eliminan saltos de línea y se separan los elementos por coma           
        partes = linea.strip().split(",")  
        # Asignacion de valores a variables segun su indice y significado
        nombre = partes[0]
        precio = partes[1]
        cantidad = partes[2]
        # Carga de diccionario a array "productos" 
        productos.append({
            "Nombre": nombre,
            "Precio": precio,
            "Cantidad": cantidad
        })

# Mensaje final
print("========= Lista de diccionario completa ==========")
print(productos)
print("==================================================")

# Consigna 5: Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error. 

# Inicializo variables
encontrado = False

# Solicitud y asignacion de valor a variable
busqueda = input("Ingrese el nombre del producto que desea buscar: ").lower()

# Inicio condicional
if busqueda == "":
    print("Error, no ingreso nada")
else:
    for producto in productos:
        if producto["Nombre"].lower() == busqueda:
            print("Producto encontrado:")
            for clave in producto:
                print(f"{clave}: {producto[clave]}")
            encontrado = True

# Inicio condicional - Mensaje de error
if not encontrado:
    print("Producto no encontrado")

# Consigna 6: Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.

# Manejo seguro de archivo usando with (cierre automatico)
with open("productos.txt", "w") as archivo:
    # Inicio bucle - Se recorre la lista de diccionarios
    for producto in productos:
        # Asignación de valor a variables para cada iteración 
        nombre = producto["Nombre"]
        precio = producto["Precio"]
        cantidad = producto["Cantidad"]
        # Escritura en archivo
        archivo.write(f"{nombre},{precio},{cantidad}\n")

# Mensaje final
print("=================================================")
print("Productos actualizados guardados en productos.txt")
print("=================================================")