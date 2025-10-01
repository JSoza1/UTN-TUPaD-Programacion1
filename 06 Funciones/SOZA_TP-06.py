# Consigna 1: Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

# Mensaje inicial
print("-------------- Ejercicio 1 --------------")
print ("======= Hola mundo desde función =======")

# Definicion de función
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Llamado de función
imprimir_hola_mundo()

# Consigna 2: Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de volver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

# Mensaje inicial 
print("-------------- Ejercicio 2 --------------")
print ("=========== Saludar a usuario ===========")

# Definicion de función
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# Mensaje con solicitud y llamado de función
saludar_usuario(input("Ingrese su nombre: "))

# Consigna 3: Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Mensaje inicial 
print("-------------- Ejercicio 3 --------------")
print ("=== Oración con información personal ===")

# Inicialización de variables
nombre_3 = ""
apellido_3 = ""
edad_3 = 0
residencia_3 = ""

# Mensaje con solicitud y asignación de valor a varibles
nombre_3 = input("Ingrese su nombre: ")
apellido_3 = input("Ingrese su apellido: ")
edad_3 = input("Ingrese su edad: ")
residencia_3 = input("Ingrese su residencia: ")

# Definicion de función
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Llamado de función
informacion_personal(nombre_3, apellido_3, edad_3, residencia_3)

# Consigna 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# Mensaje inicial 
print("-------------- Ejercicio 4 --------------")
print ("=== Calculo de area y perimetro de un circulo ===")

# Inicialización de variables
PI = 3.14
radio = 0
area = 0
perimetro = 0

# Definicion de funciones
def calcular_area_circulo(radio):
    # Calculo para calcular el area de un circulo
    return PI * (radio ** 2)

def calcular_perimetro_circulo(radio):
    # Calculo para calcular el perimetro de un circulo
    return 2 * PI * radio

# Mensaje con solicitud y asignación de valor a varible
radio = float(input("Ingrese el radio de un circulo: "))

# Llamado de funciones y asignacion de valor a variables
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

# Mensaje final con resultados
print(f"El area del circulo es {area:.2f} y el perimetro es {perimetro:.2f}")

# Consigna 5: Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Mensaje inicial 
print("-------------- Ejercicio 5 --------------")
print ("=========== Segundos a horas ===========")

# Inicialización de variables
segundos = 0
horas = 0

# Definicion de función
def segundos_a_horas(segundos):
    return segundos / 3600

# Mensaje con solicitud y asignación de valor a varible
segundos = float(input ("Ingrese los segundos que desea convertir a horas: "))

# Llamado de función y asignacion de valor a variable
horas = segundos_a_horas(segundos)

# Mensaje final con resultados
print(f"Los segundos ingresados son equivalentes a {horas:.2f} horas.")

# Consigna 6: Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Mensaje inicial 
print("-------------- Ejercicio 6 --------------")
print ("========= Tabla de multiplicar =========")

# Inicialización de variable
numero6 = 0

# Definicion de función
def tabla_multiplicar(numero):
    for i in range(10):
        print(f"{numero} x {i+1} = {numero * (i+1)}")

# Mensaje con solicitud y asignación de valor a varible
numero6 = int(input("Ingrese un número para ver su tabla de multiplicar: "))

# Llamado de función
tabla_multiplicar(numero6)

# Consigna 7: Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# Mensaje inicial 
print("-------------- Ejercicio 7 --------------")
print ("========== Operaciones basicas ==========")

# Inicialización de variables
a = 0
b = 0

# Definicion de función
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # Validación de division por 0
    if b == 0:
        division = "No es posible dividir por 0"
    else:
        division = a / b
    # Tupla
    return (suma, resta, multiplicacion, division)

# Mensaje con solicitud y asignación de valor a varibles
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

# Llamado de función y muestra de resultados usando bucle
for operacion in operaciones_basicas(a,b):
    print(operacion)

# Consigna 8: Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# Mensaje inicial 
print("-------------- Ejercicio 8 --------------")
print ("============ Calculo de IMC ============")

# Inicialización de variables
peso = 0
altura = 0

# Definicion de función
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Mensaje con solicitud y asignación de valor a varibles
peso = float(input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura en metros: "))

# Llamado de función y asignacion de valor a variable
imc = calcular_imc(peso,altura)

# Mensaje final
print(f"Su IMC es {imc:.2f}")

# Consigna 9: Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# Mensaje inicial 
print("-------------- Ejercicio 9 --------------")
print ("========= Celsius a Fahrenheit =========")

# Inicialización de variables
celsius = 0
fahrenheit = 0

# Definicion de función
def celsius_a_fahrenheit(celsius):
    return (9/5) * celsius + 32

# Mensaje con solicitud y asignación de valor a varible
celsius = float(input("Ingrese los grados Celsius: "))

# Llamado de función y asignacion de valor a variable
fahrenheit = celsius_a_fahrenheit(celsius)

# Mensaje final
print(f"El equivalente en grados Fahrenheit es {fahrenheit:.2f}")

# Consigna 10: Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# Mensaje inicial 
print("-------------- Ejercicio 10 --------------")
print ("========== Calculo de promedio ==========")

# Inicialización de variables
num1 = 0
num2 = 0
num3 = 0
promedio = 0

# Definicion de función
def calcular_promedio(a, b, c):
    # Calculo de promedio
    return (a + b + c) / 3

# Mensajes con solicitud y asignación de valores a varibles
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Llamado de función y asignacion de valor a variable
promedio = calcular_promedio(num1,num2,num3)

# Mensaje final
print(f"El promedio de los 3 números ingresados es {promedio:.2f}")