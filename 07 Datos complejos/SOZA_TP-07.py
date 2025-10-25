# Consigna 1: Dado el diccionario precios_frutas 

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 

# Añadir las siguientes frutas con sus respectivos precios: 
# Naranja = 1200 
# Manzana = 1500 
# Pera = 2300 

# Mensaje inicial
print("-------------- Ejercicio 1 --------------")
print ("======= Diccionario de Frutas 1 =======")

# Inicializo variables
precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

# Mensaje
print("Antes de agregar items al diccionario:")

# Inicio de bucle, usando items()
for clave, valor in precios_frutas.items():
    print(f"{clave}: {valor}")

# Agregado de nuevas clave-valor
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Mensaje
print("--------------------------------------------")
print("Despues de agregar items al diccionario:")

# Inicio de bucle, usando items()
for clave, valor in precios_frutas.items():
    print(f"{clave}: {valor}")

# Consigna 2: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 

# Banana = 1330 
# Manzana = 1700 
# Melón = 2800

# Mensaje inicial
print("-------------- Ejercicio 2 --------------")
print ("======= Diccionario de Frutas 2 =======")

# Modificacion de valores
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# Mensaje
print("Despues de modificar valores al diccionario:")

# Inicio de bucle, usando items()
for clave, valor in precios_frutas.items():
    print(f"{clave}: {valor}")

# Consigna 3: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios. 

# Mensaje inicial
print("-------------- Ejercicio 3 --------------")
print ("=========== Lista de Frutas ===========")

# Inicializo variables
lista_de_frutas = []

# Inicio de bucle, usando keys()
for clave in precios_frutas.keys():
    lista_de_frutas.append(clave)

# Mensaje final
print(lista_de_frutas)

# Consigna 4: Escribí un programa que permita almacenar y consultar números telefónicos. Permitir al usuario cargar 5 contactos con su nombre como clave y número como valor. Luego, pedí un nombre y mostrale el número asociado, si existe.

# Mensaje inicial
print("-------------- Ejercicio 4 --------------")
print ("==== Agenda de números telefónicos ====")

# Inicializo variables
contactos = {}

# Inicio bucle
while len(contactos) < 5:
    nuevo_contacto = input("Ingrese un nuevo contacto: ")
    if nuevo_contacto != "":
        nuevo_numero = input("Ingrese un número: ")
    
    # Asignacion clave-valor a diccionario
    contactos[nuevo_contacto] = nuevo_numero

# Mensaje - busqueda en diccionario - asignacion de valor a variable
numero_de_telefono = contactos.get(input("Ingrese un nombre de contacto para buscar su número: "))

# Inicio condicional 
if numero_de_telefono: # Variable con valor es considerada true
    print(f"Telefono: {numero_de_telefono}") 
else:
    print("Nombre de contacto no agendado")

# Consigna 5: Solicita al usuario una frase e imprime: 

# Las palabras únicas (usando un set). 
# Un diccionario con la cantidad de veces que aparece cada palabra.

# Mensaje inicial
print("-------------- Ejercicio 5 --------------")
print ("========= Contador de palabras =========")

# Inicializo variables
frase = ""
array_palabras = []
set_palabras_unicas = set()
dic_palabras_cantidad = {}

# Solicitud y asignación de valor a variable
frase = input("Escribe una frase: ")

# Conversion a minuscula (para no tener errores en conteo) y creacion de lista de strings
array_palabras = frase.lower().split()

# Conversion de array a set (eliminación de duplicados)
set_palabras_unicas = set(array_palabras)

# Inicio bucle
for palabra in array_palabras:
    dic_palabras_cantidad[palabra] = dic_palabras_cantidad.get(palabra, 0) + 1

# Mensajes finales
print("Palabras únicas:")
print(set_palabras_unicas)
print("Recuento de palabras:")
print(dic_palabras_cantidad)

# Consigna 6: Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno.

# Mensaje inicial
print("-------------- Ejercicio 6 --------------")
print ("========== Promedio de notas ==========")

# Inicializo variables
alumnos = {}

# Inicio bucle
for vuelta_nombres in range(3):
    alumno = ""
    while alumno == "":
        alumno = input(f"Ingrese el nombre del alumno {vuelta_nombres + 1}: ")
        
    notas = []
    for vuelta_notas in range(3):
        nota = input(f"Ingrese la nota n°{vuelta_notas + 1} de {alumno}: ")
        notas.append(nota)

    alumnos[alumno] = tuple(notas)

# Mensaje
print("Promedios por alumno:")

# Inicio bucle
for nombre, notas in alumnos.items():
    suma = 0
    for nota in notas:
        # Conversion de cada nota a float
        suma += float(nota)  
    promedio = suma / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")

# Consigna 7: Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2: 

# Mostrá los que aprobaron ambos parciales. 
# Mostrá los que aprobaron solo uno de los dos. 
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

# Mensaje inicial
print("-------------- Ejercicio 7 --------------")
print ("======= Aprobación de parciales =======")

# Inicializo variables
parcial_1 = {101, 102, 103, 104}
parcial_2 = {103, 104, 105, 106}

# Intersección y muestra de resultados
print("Los que aprobaron ambos parciales: ", parcial_1 & parcial_2)

# Diferencia y muestra de resultados
print("Los que aprobaron solo el parcial 1: ", parcial_1 - parcial_2)

# Unión y muestra de resultados
print("Los que aprobaron al menos un parcial: ", parcial_1 | parcial_2)

# Consigna 8: Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 

# Permitir al usuario: 
# Consultar el stock de un producto ingresado. 
# Agregar unidades al stock si el producto ya existe. 
# Agregar un nuevo producto si no existe. 

# Mensaje inicial
print("-------------- Ejercicio 8 --------------")
print ("========= Stocks de productos =========")

# Inicializo variables
menu_opciones = ["1. Consultar stock de producto",
                 "2. Agregar stock a producto existente",
                 "3. Agregar nuevo producto", 
                 "4. Salir"]
productos = {}

# Funciones globales
def existencia_productos():
# Validación de existencia de productos
    if not productos:
        print("No hay productos cargados, opción invalida")
        print("=================================")
        # Valor de retorno de función
        return False
    return True

# Inicio bucle principal
while True:
    # Inicio bucle - se recorre el array del menú y se muestra en consola su contenido
    for opcion in menu_opciones:
        print(opcion)

    print("====================================")
    # Solicitud y asignacion de valor a variable
    opcion_ingresada = input("Ingrese una opción: ")

    # Inicio condicional match case
    match opcion_ingresada:
        case "1": # Consultar stock de producto
            
            # Inicio condicional (vuelve al menú principal si no hay productos)
            if not existencia_productos():
                continue
                    
            # Inicio bucle
            while True:
                # Solicitud y asignacion de valor a variable
                producto_consultado = input("Ingrese un producto para ver su stock: ").lower()

                # Validación de string vacio
                if producto_consultado == "":
                    print("No ingresó nada. Vuelva a intentarlo.")
                    continue

                # Bandera
                encontrado = False

                # Inicio bucle - Se recorre el diccionario de productos buscando coincidencia con la busqueda
                for producto, stock in productos.items():
                    if producto_consultado == producto.lower():
                        print(f"El producto ({producto_consultado.capitalize()}) dispone de {stock} unidades")
                        encontrado = True
                        break

                if not encontrado:
                    print(f"El producto '{producto_consultado}' no fue encontrado.")
                
                # Solicitud y asignacion de valor a variable
                opcion4 = input("¿Desea consultar otro producto? S = Sí / N = No: ").lower()

                # Si el ingreso es distinto de "s" se vuelve al menú principal
                if opcion4 != "s":
                    print("Volviendo al menú principal")
                    break
        
        case "2": # Agregar stock a producto existente

            existencia_productos()

            # Inicio condicional (vuelve al menú principal si es true)
            if not existencia_productos():
                continue

            # Inicio bucle - Combinacion con enumerate para tener los indices y claves
            for i, producto in enumerate(productos.keys()):
                print(f"{i + 1} {producto}")

            # Solicitud y asignacion de valor a variable
            producto_seleccionado = input("Ingrese el número del producto para actualizar stock: ")

            # Inicio condicional si el valor es un numero
            if producto_seleccionado.isdigit():
                producto_seleccionado = int(producto_seleccionado) - 1

                # Inicio bucle - Agregado de stock
                for i, producto in enumerate(productos.keys()):
                    if i == producto_seleccionado:
                        actualizar_stock = input("Ingrese cantidad de stock a agregar: ")
                        if actualizar_stock.isdigit():
                            actualizar_stock = int(actualizar_stock)
                            productos[producto] += actualizar_stock
                        else:
                            print("============================================")
                            print("Ingreso invalido. Debe ingresar un número")
                            print("============================================")
            
            else:
                print("============================================")
                print("Ingreso invalido. Debe ingresar el número del producto para agregar stock")
                print("============================================")

        case "3": # Agregar nuevo producto

            # Solicitud y asignacion de valor a variable
            nuevo_producto = input("Ingrese un nuevo producto: ")

            # Inicio condicional
            if nuevo_producto in productos:
                print("============================================")
                print("El producto ya fue agregado")
                print("============================================")
            
            elif nuevo_producto != "":
                productos[nuevo_producto] = 0
                print("============================================")
                print(f"Producto {nuevo_producto} agregado")
                print("============================================")
            else:
                print("============================================")
                print("Debe ingresar un nombre de producto")
                print("============================================")
            
        case "4": # Salir
            # Salida del bucle y finalización del programa
            print("¡Programa finalizado!")
            break

# Consigna 9: Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

# Permitir consultar qué actividad hay en cierto día y hora. 

# Mensaje inicial
print("-------------- Ejercicio 9 --------------")
print ("=============== Agenda ===============")

# Inicializo variables
agenda = {("Lunes","10:00"): "Matematica",
          ("Martes","11:00"): "Programacion",
          ("Miercoles","12:00"): "AySO",
          ("Jueves","13:00"): "Organizacion Empresarial",
          ("Viernes","14:00"): "Base de datos",
          ("Sabado","15:00"): "Estadistica",
          ("Domingo","16:00"): "Natación"
          }

# Solicitud y asignación de valor a variable
consulta = input("Ingrese la actividad a consultar: ").lower()

# Inicio condicional
if consulta == "":
    print("No se ingresó ninguna actividad.")

else:
    existe = False
    for (dia, hora), actividad in agenda.items():
        if consulta == actividad.lower():
            print(f"{dia} a las {hora}: {actividad}")
            existe = True

    if not existe:
        print("La actividad no está programada en la agenda.")

# Consigna 10: Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:

# Las capitales sean las claves. 
# Los países sean los valores.

# Mensaje inicial
print("-------------- Ejercicio 10 --------------")
print ("===== Nombres de países y capitales =====")

# Inicializo variables - Diccionario inicial
diccionario_paises= {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

# Nuevo diccionario con inversión de clave-valor
diccionario_capitales = {}

# Inicio bucle
for pais, capital in diccionario_paises.items():
    diccionario_capitales[capital] = pais

# Mensaje final
print("Diccionario inicial:")
print(diccionario_paises)
print("Diccionario invertido:")
print(diccionario_capitales)