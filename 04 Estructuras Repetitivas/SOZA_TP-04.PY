# Consigna 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

print("-------------- Ejercicio 1 ------------------")

for numeros in range(101):
    print(numeros)

# Consigna 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 

print("-------------- Ejercicio 2 ------------------")

# Inicializo variable
contador_1 = 0

# Solicitud y asignacion de valor a variable
numero1 = input("Ingrese un numero: ")

# Inicio de bucle (se recorre cada caracter de la variable numero)
for digitos in numero1:
    # Por cada iteracion se suma 1 al contador
    contador_1 += 1
# Mensaje final
print("La cantidad de digitos es: ",contador_1)

# Consigna 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

print("-------------- Ejercicio 3 ------------------")

# Inicializo variable
suma_1 = 0

# Solicitud y asignacion de valor a variable
num_a = int(input("Ingrese un numero: "))
# Solicitud y asignacion de valor a variable
num_b = int(input("Ingrese un numero: "))

# Inicio condicional
if num_a > num_b:
    # Inicio de bucle
    for numeros_entre_medio in range(num_b + 1,num_a):
        # Por cada iteracion se suma los numeros entre medio
        suma_1 += numeros_entre_medio
elif num_a < num_b:
    for numeros_entre_medio in range(num_a + 1,num_b):
        # Por cada iteracion se suma los numeros entre medio
        suma_1 += numeros_entre_medio
# Mensaje final
print("La suma de los numeros enteros entre medio es: ",suma_1)

# Consigna 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 

print("-------------- Ejercicio 4 ------------------")

# Inicializo variable
suma_2 = 0

# Solicitud y asignacion de valor a variable
numero_2 = int(input("Ingrese un numeros para sumar (0 para finalizar): "))

# Inicio de bucle
while numero_2 != 0:
    # Por cada iteracion se suman numeros
    suma_2 += numero_2
    numero_2 = int(input("Ingrese otro numero: "))

# Mensaje final
print("La suma de los numeros es: ",suma_2)

# Consigna 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

print("-------------- Ejercicio 5 ------------------")

# Importación de modulo
import random

# Inicializo variable
contador_2 = 1
numero_aleatorio = random.randint(0,9)

# Solicitud y asignacion de valor a variable
numero_3 = int(input("Ingrese un número entre 0 y 9, para intentar adivinar el número aleatorio: "))

# Inicio de bucle
while numero_3 != numero_aleatorio:
    numero_3 = int(input("Ingrese un otro número: "))
    # Por cada iteracion se suman numeros
    contador_2 = contador_2 + 1

# Mensaje final
print(f"Adivino el número aleatorio ({numero_aleatorio}), en {contador_2} intentos")

# Consigna 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente. 

print("-------------- Ejercicio 6 ------------------")

# Inicio de bucle
for numeros_pares in range(100,-1,-2):
    print(numeros_pares)

# Consigna 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario. 

print("-------------- Ejercicio 7 ------------------")

# Inicializo variable
suma_3 = 0

# Solicitud y asignacion de valor a variable
numero_4 = int(input("Ingrese un número: "))

# Inicio de bucle
for suma_de_numeros in range(0, numero_4 +1):
    suma_3 += suma_de_numeros

# Mensaje final
print(f"La suma total de los números entre 0 y el número ingresado es: {suma_3}")

# Consigna 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

print("-------------- Ejercicio 8 ------------------")

# Inicializo variables
numeros_positivos = 0
numeros_negativos = 0
numeros_pares2 = 0
numeros_impares = 0

# Inicio de bucle (cambio en range para modificar números a ingresar)
for numeros_enteros in range(0,100):
    numeros_ingresados1 = int(input("Ingrese un número: "))
    if numeros_ingresados1 > 0:
        numeros_positivos += 1
        if numeros_ingresados1 % 2 == 0:
            numeros_pares2 += 1
        else:
            numeros_impares += 1
    elif numeros_ingresados1 < 0:
        numeros_negativos += 1
        if numeros_ingresados1 % 2 == 0:
            numeros_pares2 += 1
        else:
            numeros_impares += 1
    else:
        numeros_pares2 += 1

# Mensajes finales
print(f"Los cantidad de números pares ingresados es: {numeros_pares2}")
print(f"Los cantidad de números impares ingresados es: {numeros_impares}")
print(f"Los cantidad de números positivos ingresados es: {numeros_positivos}")
print(f"Los cantidad de números negativos ingresados es: {numeros_negativos}")
    
# Consigna 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor). 

print("-------------- Ejercicio 9 ------------------")

# Inicializo variable
suma_4 = 0

# Inicio de bucle (cambio en range para modificar números a ingresar)
for numeros_2 in range(0,100):
    numeros_ingresados2 = int(input("Ingrese un número: "))
    suma_4 += numeros_ingresados2

# Calculo de media
media = suma_4 / 5

# Mensaje final
print(f"La media de los números ingresados es: {media}")

# Consigna 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print("-------------- Ejercicio 10 ------------------")

# Inicializo variable
nuevo_numero = ""

# Solicitud y asignacion de valor a variable
numero_para_invertir = input("Ingrese un número para invertir el orden de los digitos: ")

# Inicio bucle
for digito in numero_para_invertir:
    nuevo_numero = digito + nuevo_numero

# Mensaje final
print(f"El numero invertido es: {nuevo_numero}")