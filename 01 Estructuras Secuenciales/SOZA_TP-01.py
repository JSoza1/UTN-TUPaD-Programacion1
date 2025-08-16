# Ejercicio 1
print("-------------- Ejercicio 1-------------------")

print("Hola mundo")

# Ejercicio 2
print("-------------- Ejercicio 2-------------------")

# Inicializo variables
nombre = ""

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

# Ejercicio 3 
print("-------------- Ejercicio 3-------------------")

# Inicializo variables
nombre2 = ""
apellido = ""
edad = 0
residencia = ""

nombre2 = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

print(f"Hola soy {nombre2} {apellido} tengo {edad} años y vivo en {residencia}")

# Ejercicio 4
print("-------------- Ejercicio 4-------------------")

# Inicializo variables
PI = 3.14
radio = 0
area = 0
perimetro = 0

radio = float(input("Ingrese el radio de un circulo: "))

area = PI * (radio ** 2)
perimetro = 2 * PI * radio

print(f"El area del circulo es {area} y su perimetro es {perimetro}")

# Ejercicio 5
print("-------------- Ejercicio 5-------------------")

# Inicializo variables
segundos = 0
horas = 0

segundos = float(input ("Ingrese los segundos que desea convertir a horas: "))

horas = segundos / 3600

print(f"los segundos ingresados son equivalente a {horas} horas")

# Ejercicio 6
print("-------------- Ejercicio 6-------------------")
  
# Inicializo variables
numero = 0

numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# Ejercicio 7
print("-------------- Ejercicio 7-------------------")

# Inicializo variables
numero2 = 0
numero3 = 0

numero2 = int(input("Ingrese un primer numero distinto del 0: "))
numero3 = int(input("Ingrese un segundo numero distinto del 0: "))

print(f"{numero2} + {numero3} = {numero2 + numero3}")
print(f"{numero2} / {numero3} = {numero2 / numero3}")
print(f"{numero2} x {numero3} = {numero2 * numero3}")
print(f"{numero2} - {numero3} = {numero2 - numero3}")

# Ejercicio 8
print("-------------- Ejercicio 8-------------------")

# Inicializo variables
imc = 0
peso = 0
altura = 0

print("Calculadora de IMC")
peso = float(input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print(f"Su IMC es {imc}")

# Ejercicio 9
print("-------------- Ejercicio 9-------------------")

# Inicializo variables
celcius = 0
fahrenheit = 0

print("Convertidor de Celcius a Fahrenheit")
celcius = float(input("Ingrese los grados Celcius: "))

fahrenheit = (9/5) * celcius + 32

print(f"El equivalente en grados Fahrenheit es {fahrenheit}")

# Ejercicio 10
print("-------------- Ejercicio 10-------------------")

# Inicializo variables
num1 = 0
num2 = 0
num3 = 0
promedio = 0

print("Promedio de 3 numeros")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los 3 numeros ingresados es {promedio}")