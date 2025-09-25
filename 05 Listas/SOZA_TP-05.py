# Consigna General: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas. 

# Consigna 1: Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa. 
# • Calcular y mostrar el promedio. 
# • Indicar la nota más alta y la más baja.

print("-------------- Ejercicio 1 ------------------")

# Inicializo variables y asigno valores
notas = [1, 4, 5, 6, 6, 7, 7, 8, 9, 10]
nota_mas_alta = float("-inf") # Inicialmente el valor más bajo posible
nota_mas_baja = float("inf") # Inicialmente el valor más alto posible
suma = 0
cantidad_de_numeros = 0

# Mensaje inicial 
print ("============== Lista de notas ==============")

# Inicio bucle
for nota in notas:
    print(nota)
    suma += nota
    cantidad_de_numeros += 1
    # Condicional para determinar nota más alta o baja
    if nota > nota_mas_alta:
        nota_mas_alta = nota
    if nota < nota_mas_baja:
        nota_mas_baja = nota

# Mensaje final
print("============================================")
print(f"El promedio de las notas es {suma / cantidad_de_numeros}")
print(f"La nota más alta es: {nota_mas_alta}")
print(f"La nota más baja es: {nota_mas_baja}")

# Consigna 2: Pedir al usuario que cargue 5 productos en una lista. 
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

print("-------------- Ejercicio 2 ------------------")

# Inicializo variables 
productos = []
contador = 0

# Mensaje inicial
print("======= Lista de productos modificable =======")
print("Ingrese un maximo de 5 productos")

# Inicio bucles
for producto in range(5):
    contador += 1
    productos.append(input(f"Ingrese producto n° {contador}: "))

print("============ Productos ingresados ============")

for producto in sorted(productos):
    print(producto)

print("=============================================")

# Mensaje con solicitud de eliminación
productos.remove(input("Ingrese un producto a eliminar: "))

print("========== Productos actualizados ==========")
# Bucle final
for producto in sorted(productos):
    print(producto)

# Consigna 3: Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares. 
# • Mostrar cuántos números tiene cada lista. 

print("-------------- Ejercicio 3 ------------------")
# Importación de modulo
import random

# Inicializo variables
numeros = []
numeros_pares = []
numeros_impares = []

# Inicio bucles
for numero in range(15):
    numeros.append(random.randint(1, 100))

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

# Mensajes finales con resultados
print("===== Lista de numeros pares =====")
for numero in numeros_pares:
    print(numero)

print(f"Cantidad de números pares: {len(numeros_pares)}")

print("==== Lista de numeros impares ====")
for numero in numeros_impares:
    print(numero)

print(f"Cantidad de números impares: {len(numeros_impares)}")

# Consigna 4: Dada una lista con valores repetidos
# datos [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos. 
# • Mostrar el resultado. 

print("-------------- Ejercicio 4 ------------------")

# Inicializo variables y asigno valores
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
nuevos_datos = []

# Inicio bucle
for numero in datos:
    if numero not in nuevos_datos:
        nuevos_datos.append(numero)

# Mensaje final con resultados
print("====== Lista sin elementos repetidos ======")
for numero in nuevos_datos:
    print(numero)

# Consigna 5: Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# • Mostrar la lista final actualizada.

print("-------------- Ejercicio 5 ------------------")

# Inicializo variables y asigno valores
estudiantes = ["Juan","Carlos","Esteban","Pepe","Juana","Maria","Cristian","Ana"]
opcion = ""

# Mensaje inicial
print("========== Lista de estudiantes ==========")

# Inicio bucle
for estudiante in estudiantes:
    print(estudiante)

# Mensaje solicitando valor
print("=======================================")
opcion = input("Ingrese (a) para agregar un estudiante o (e) para eliminar un estudiante: ").lower()

# Inicio condicional
if opcion == "a":
    estudiantes.append(input("Ingrese estudiante a agregar: ").capitalize())
elif opcion == "e":
    estudiantes.remove(input("Ingrese estudiante a eliminar: ").capitalize())
else:
    print("Opcion invalida")

# Mensaje final con lista actualizada
print("====== Lista con estudiantes actualizada ======")
for estudiante in estudiantes:
    print(estudiante)

# Consigna 6: Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

print("-------------- Ejercicio 6 ------------------")

# Inicializo variables y asigno valores
lista_de_numeros = [1,2,3,4,5,6,7]

# Solucion con concatenacion y slicing
lista_de_numeros = [lista_de_numeros[-1]] + lista_de_numeros[:-1]

# Muestra de resultados
print("======= Nuevas posiciones en la lista =======")
print(lista_de_numeros)

# Consigna 7: Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana. 
# • Calcular el promedio de las mínimas y el de las máximas. 
# • Mostrar en qué día se registró la mayor amplitud térmica. 

print("-------------- Ejercicio 7 ------------------")

# Inicializo variables y asigno valores
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = [
    [8, 22],
    [12, 25],
    [9, 20],
    [7, 23],
    [13, 26],
    [8, 19],
    [10, 21]
]
mayor_amplitud = 0
dia_mayor_amplitud_termica = ""
suma_maximas = 0
suma_minimas = 0

# Mensaje
print("========= Temperaturas de la semana =========")

# Inicio bucles
for i in range(7):
    print(f"{dias[i]}: Mínima = {temperaturas[i][0]}° | Máxima = {temperaturas[i][1]}°")

# Calculos de promedios
for temperatura_minima in temperaturas:
    suma_minimas += temperatura_minima[0]

promedio_minimas = suma_minimas / len(temperaturas)

for temperatura_maxima in temperaturas:
    suma_maximas += temperatura_maxima[1]

promedio_maximas = suma_maximas / len(temperaturas)

# Calculos de amplitud termica
for i in range(7):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud_termica = dias[i]

# Mensaje final con resultados
print("========= Promedios de temperaturas =========")
print(f"Promedio de mínimas: {promedio_minimas:.0f}°")
print(f"Promedio de máximas: {promedio_maximas:.0f}°")
print("========== Mayor amplitud térmica ==========")
print(f"El {dia_mayor_amplitud_termica} fue el día con mayor amplitud termica con {mayor_amplitud}° de diferencia.")

# Consigna 8: Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# • Mostrar el promedio de cada estudiante. 
# • Mostrar el promedio de cada materia. 

print("-------------- Ejercicio 8 ------------------")

# Inicializo variables y asigno valores
matriz_de_notas = [
    [ "Informática" , "Matemática" , "Literatura" ],
    [       5       ,       7      ,      9       ],
    [       7       ,       1      ,      6       ],   
    [       5       ,       7      ,      5       ],
    [       10      ,       5      ,      9       ],
    [       9       ,       3      ,      3       ]
]
suma_notas = 0
promedio_estudiante = 0
suma_informatica = 0
suma_matematica = 0
suma_literatura = 0

# Mensaje
print("========== Promedio de estudiantes ==========")

# Inicio bucles
for i, estudiante in enumerate(matriz_de_notas[1:]):
    suma_notas = 0
    for estudiante_notas in estudiante:
        suma_notas += estudiante_notas
    promedio_estudiante = suma_notas / 3
    print(f"El promedio del estudiante N°{i + 1} es {promedio_estudiante:.0f}")

# Mensaje
print("=========== Promedio por materias ===========")

# Promedios por materia (informática)
for fila in matriz_de_notas[1:]:  # Salteamos el encabezado
    suma_informatica += fila[0]  # Posición 0 = Informática

promedio_informatica = suma_informatica / 5 

print(f"Promedio de Informática: {promedio_informatica:.0f}")

# Promedios por materia (matemática)
for fila in matriz_de_notas[1:]:  
    suma_matematica += fila[1]  

promedio_matematica = suma_matematica / 5 

print(f"Promedio de Matemática: {promedio_matematica:.0f}")

# Promedios por materia (Literatura)
for fila in matriz_de_notas[1:]:  
    suma_literatura += fila[2]  

promedio_literatura = suma_literatura / 5 

print(f"Promedio de Literatura: {promedio_literatura:.0f}")

# Consigna 9 Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
# • Inicializarlo con guiones "-" representando casillas vacías. 
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
# • Mostrar el tablero después de cada jugada. 

print("-------------- Ejercicio 9 ------------------")

# Inicializo variables y asigno valores
tateti = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
    ]
jugador = "X"
jugadas = 0

# Inicio bucle
while jugadas < 9:

    # Mensaje inicial
    print(f"Turno del jugador {jugador}")

    # Mensaje con solicitud de posicion
    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))

    # Inicio condicional
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Posición fuera de rango. Vuelva a intentarlo")
        continue
    if tateti[fila][columna] == "-":
        tateti[fila][columna] = jugador
        jugadas += 1
    else:
        print("Espacio ocupado. Vuelva a intentarlo")
        continue

    # Inicio Bucle
    for fila in tateti:
        for celda in fila:
            print(celda, end= " ")
        print()
    
    # Determinación de jugador
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

# Mensaje final
print("Fin del juego. Se completo el TaTeTi")

# Consigna 10: Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
# • Mostrar el total vendido por cada producto. 
# • Mostrar el día con mayores ventas totales. 
# • Indicar cuál fue el producto más vendido en la semana. 

print("-------------- Ejercicio 10 ------------------")

# Inicializo variables y asigno valores
productos2 = ["Tomate", "Fideos", "Cereales", "Azucar"]  
dias2 = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] 
ventas_productos = [
    [5, 3, 6, 2, 4, 7, 3],  # Ventas de Tomate 
    [2, 4, 1, 3, 5, 2, 6],  # Ventas de Fideos
    [3, 5, 2, 4, 6, 3, 1],  # Ventas de Cereales
    [4, 2, 5, 6, 3, 4, 2]   # Ventas de Azucar
]
mayor_venta_dia = 0            
ventas_mayor_dia = 0           
mayor_venta_producto = 0        
producto_mas_vendido = 0 

# Mensaje inicial
print("======= Total vendido por cada producto =======")
# Inicio bucle - Recorrido de cada producto 
for i, producto2 in enumerate(productos2):  
    # Reseteo de total de ventas
    total = 0   
    # Recorrido de cada venta (fila completa)
    for venta in ventas_productos[i]:   
        # Suma de ventas de cada fila 
        total += venta
    # Mensaje de resultado de ventas
    print(f"{producto2}: {total} unidades")

# Inicio bucle
for i, nombre_dia in enumerate(dias2): 
    total_dia = 0                     
    for producto in range(4):               
        # Se suman ventas de cada producto por dia
        total_dia += ventas_productos[producto][i]  
        # Si se encuentra nuevo maximo, se guarda el total y el indice del dia
    if total_dia > mayor_venta_dia:         
        mayor_venta_dia = total_dia         
        ventas_mayor_dia = i                

# Mensaje con resultados
print("========================================")
print(f"El día con mayores ventas fue {dias2[ventas_mayor_dia]} con {mayor_venta_dia} productos.")

# Inicio del bucle
for i, producto2 in enumerate(productos2):  
    total = 0                               
    for venta in ventas_productos[i]:      
        total += venta                     
    if total > mayor_venta_producto:       
        mayor_venta_producto = total      
        producto_mas_vendido = i         

# Mensaje final con resultados
print("========================================")
print(f"El producto más vendido en la semana fue el {productos2[producto_mas_vendido]} con {mayor_venta_producto} productos.")