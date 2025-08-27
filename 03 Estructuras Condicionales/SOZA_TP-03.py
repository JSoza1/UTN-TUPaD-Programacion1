# ====================================================
# Ejercicio (1)
print("-------------- Ejercicio 1-------------------")

edad = input("Ingrese su edad: ")
edad = int(edad)

if edad >= 18:
    print("Es mayor de edad")

# ====================================================
# Ejercicio (2) 
print("-------------- Ejercicio 2-------------------")

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else: 
    print("Desaprobaado")

# ====================================================
# Ejercicio (3)
print("-------------- Ejercicio 3-------------------")

numeroParImpar = int(input("Ingrese un numero par: "))

if numeroParImpar % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# ====================================================
# Ejercicio (4)
print("-------------- Ejercicio 4-------------------")

edad2 = input("Ingrese su edad: ")

if edad2.isdigit():
    edad2 = int(edad2)
    if edad2 < 12:
        print("Usted es niño/a")
    elif edad2 >= 12 and edad2 < 18:
        print("Usted es adolescente")
    elif edad2 >= 18 and edad2 < 30:
        print("Usted es adulto/a joven")
    else:
        print("Usted es adulto/a mayor")
else:
    print("Ingrese un numero valido, sin simbolos, puntos y/o letras combinadas con números")

# ====================================================
# Ejercicio (5)
print("-------------- Ejercicio 5-------------------")

password = input("Ingrese una contraseña entre 8 y 14 caracteres: ")

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# ====================================================
# Ejercicio (6)
print("-------------- Ejercicio 6-------------------")

from statistics import mode, median, mean
import random 

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Segun los numeros aleatorios: ")

if media > mediana and mediana > moda:
    print("Hay Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay Sesgo negativo")
elif moda == mediana == media:
    print("No hay Sesgo")
else:
    print("No se puede determinar el Sesgo con los datos aleatorios obtenidos")

# ====================================================
# Ejercicio (7)
print("-------------- Ejercicio 7-------------------")

palabra = input("Ingrese una frase o palabra: ")

if palabra[-1].lower() == "a" or palabra[-1].lower() == "e" or palabra[-1].lower() == "i" or palabra[-1].lower() == "o" or palabra[-1].lower() == "u":
    print(palabra + "!")
else:
    print(palabra)

# ====================================================
# Ejercicio (8)
print("-------------- Ejercicio 8-------------------")

nombre = input("Ingrese su nombre: ")

if nombre != "" and nombre.isalpha():
    print("Elija una opcion")
    print("(1) Si quiere su nombre en mayúsculas.")
    print("(2) Si quiere su nombre en minúsculas")
    print("(3) Si quiere su nombre con la primera letra mayúscula.")
    opcion = input("Ingrese opcion: ")
    if opcion == "1":
        print(nombre.upper())
    elif opcion == "2":
        print(nombre.lower())
    elif opcion == "3":
        print(nombre.title())
    else:
        print("Opción no valida, ingrese 1, 2 o 3")
else:
    print("No ingreso un nombre valido o simplemente no ingreso nada")

# ====================================================
# Ejercicio (9)
print("-------------- Ejercicio 9-------------------")

terremoto = input("Ingrese el número, correspondiente a la magnitud de un terremoto: ")

if terremoto != "" and terremoto.isdigit():
    terremoto = int(terremoto)
    if terremoto < 3:
        print('"Muy leve" (imperceptible)') 
    elif terremoto >= 3 and terremoto < 4:
        print('"Leve" (ligeramente perceptible)')
    elif terremoto >= 4 and terremoto < 5:
        print('"Moderado" (sentido por personas, pero generalmente no causa daños)')
    elif terremoto >= 5 and terremoto < 6:
        print('"Fuerte" (puede causar daños en estructuras débiles)')
    elif terremoto >= 6 and terremoto < 7:
        print('"Muy Fuerte" (puede causar daños significativos)')
    else:
        print('"Extremo" (puede causar graves daños a gran escala)')
else:
    print("No ingreso un número o simplemente no ingreso nada")

# ====================================================
# Ejercicio 10
print("-------------- Ejercicio 10-------------------")

print("En cual hemisferio se encuenta?")
hemisferio = input("N = Norte / S = Sur: ").lower()
mes = input("En que mes se encuentra?: ").lower()
dia = input("Ingrese en que día se encuentra (número entre 1 y 31): ")

# Manejo de errores en el dia
if dia.isdigit():
    dia = int(dia)
    if dia == 0:
        print("El día 0 es incorrecto")
    elif dia > 31:
        print("Día fuera del rango de 1 a 31")
else:
    print("Ingrese un número en el día")
    exit()

# Periodo: 21 diciembre – 20 marzo
if (mes == "diciembre" and dia >= 21 and dia <= 31) or (mes == "marzo" and dia >= 1 and dia <= 20) or (mes == "enero" and dia >= 1 and dia <= 31) or (mes == "febrero" and dia >=1 and dia <= 29):
    if hemisferio == "n":
        print("Se encuentra en Invierno")
    elif hemisferio == "s":
        print("Se encuentra en Verano")
    else:
        print('Ingrese "S" o "N" para el hemisferio')

# Periodo: 21 marzo – 20 junio
elif (mes == "marzo" and dia >= 21 and dia <= 31) or (mes == "junio" and dia <= 20) or (mes == "abril" and dia >= 1 and dia <= 30) or (mes == "mayo" and dia >=1 and dia <= 31):
    if hemisferio == "n":
        print("Se encuentra en Primavera")
    elif hemisferio == "s":
        print("Se encuentra en Otoño")
    else:
        print('Ingrese "S" o "N" para el hemisferio')

# Periodo: 21 junio – 20 septiembre
elif (mes == "junio" and dia >= 21 and dia <= 30) or (mes == "septiembre" and dia <= 20) or (mes == "julio" and dia >= 1 and dia <= 31) or (mes == "agosto" and dia >= 1 and dia <= 31):
    if hemisferio == "n":
        print("Se encuentra en Verano")
    elif hemisferio == "s":
        print("Se encuentra en Invierno")
    else:
        print('Ingrese "S" o "N" para el hemisferio')

# Periodo: 21 septiembre – 20 diciembre
elif (mes == "septiembre" and dia >= 21 and dia <= 30) or (mes == "diciembre" and dia <= 20) or (mes == "octubre" and dia >= 1 and dia <= 31) or (mes == "noviembre" and dia >= 1 and dia <= 30):
    if hemisferio == "n":
        print("Se encuentra en Otoño")
    elif hemisferio == "s":
        print("Se encuentra en Primavera")
    else:
        print('Ingrese "S" o "N" para el hemisferio')

# Manejo de errores en la fecha
else:
    print("La fecha es incorrecta")