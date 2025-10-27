# Consigna 1: Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario 

# Mensaje inicial
print("-------------- Ejercicio 1 --------------")
print ("======== Factorial de un número ========")

# Definición de función   
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# Solicitud, conversion y asignacion de valor a variable
n = int(input("Ingrese un numero para calcular el factorial: "))

# Inicio bucle - llamado a función y mensaje
for numero_actual in range(1, n + 1):
    print(f"El factorial de {numero_actual} es: {factorial(numero_actual)}")

# Consigna 2: Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# Mensaje inicial
print("-------------- Ejercicio 2 --------------")
print("========== Serie de Fibonacci ==========")

# Definición de función
def fibonacci(posicion):
    return posicion if posicion <= 1 else fibonacci(posicion - 1) + fibonacci(posicion - 2)

# Solicitud, conversion y asignacion de valor a variable
limite_superior = int(input("Ingrese una posición límite para mostrar la serie de Fibonacci: "))

# Inicio bucle - llamado a función y mensaje
for posicion_actual in range(limite_superior + 1):
    print(f"Fibonacci en posición {posicion_actual} es: {fibonacci(posicion_actual)}")

# Consigna 3: Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general. 

# Mensaje inicial
print("-------------- Ejercicio 3 --------------")
print ("== Potencia de un número base elevado a un exponente ==")

# Definición de función
def potencia(base, exponente):
    return 1 if exponente == 0 else base * potencia(base, exponente - 1)

# Solicitud, conversión y asignación de valor a variables
valor_base = int(input("Ingrese el número base: "))
valor_exponente = int(input("Ingrese el exponente: "))

# Llamado a función y mensaje
resultado = potencia(valor_base, valor_exponente)
print(f"{valor_base} elevado a la {valor_exponente} es: {resultado}")

# Consigna 4: Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto. Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. 

# Para convertir un número decimal a binario, se puede seguir este procedimiento: 
# 1. Dividir el número por 2. 
# 2. Guardar el resto (0 o 1). 
# 3. Repetir el proceso con el cociente hasta que llegue a 0. 
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

# Convertir el número 10 a binario: 
# 10 ÷ 2 = 5     resto: 0   
#  5 ÷ 2 = 2     resto: 1   
#  2 ÷ 2 = 1     resto: 0   
#  1 ÷ 2 = 0     resto: 1   

# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".

# Mensaje inicial
print("-------------- Ejercicio 4 --------------")
print("======== Base decimal a Binario ========")

# Definición de función
def conversion_binario(numero_decimal):
    # Paso 3: Repetir el proceso con el cociente hasta que llegue a 0
    if numero_decimal == 0:
        return ""
    else:
        # Paso 1: Dividir el número por 2
        cociente = numero_decimal // 2
        # Paso 2: Guardar el resto (0 o 1)
        resto = numero_decimal % 2
        # Paso 4: Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario
        binario_parcial = conversion_binario(cociente)
        return binario_parcial + str(resto)

# Solicitud, conversión y asignación de valor a variable
numero_decimal = int(input("Ingrese un número entero positivo: "))

# Inicio condicional
if numero_decimal == 0:
    print("El número binario es: 0")
else:
    # Llamado a función y mensaje
    resultado_binario = conversion_binario(numero_decimal)
    print(f"El número binario es: {resultado_binario}")

# Consigna 5: Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 

# Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed(). 

# Mensaje inicial
print("-------------- Ejercicio 5 --------------")
print ("============== Palíndromo ==============")

# Definición de función
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    # Si la primera y la última letra son distintas, no es palíndromo
    if palabra[0] != palabra[len(palabra) - 1]:
        return False

    # Llamado a la función sin la primera y última letra
    return es_palindromo(palabra[1:len(palabra) - 1])

# Solicitud y asignación de valor a variable
palabra = input("Ingresá una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo")
else:
    print(f"'{palabra}' no es un palíndromo")

# Consigna 6: Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos. 

# Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 

# Ejemplos: 
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
# suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5) 

# Mensaje inicial
print("-------------- Ejercicio 6 --------------")
print ("=========== Suma de digitos ===========")

# Definición de función
def suma_digitos(n):
    if n < 10:
        return n
    # Separación del último dígito y sumar el resto
    else:
        return (n % 10) + suma_digitos(n // 10)

# Solicitud, conversión y asignación de valor a variable
numero_ingresado = int(input("Ingresá un número entero positivo: "))

# Llamado a función y mensaje
print(f"La suma de los dígitos de {numero_ingresado} es {suma_digitos(numero_ingresado)}")

# Consigna 7: Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. 

# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide. 
 
# Ejemplos: 
# contar_bloques(1)   → 1         (1) 
# contar_bloques(2)   → 3         (2 + 1) 
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 

# Mensaje inicial
print("-------------- Ejercicio 7 --------------")
print ("========= Contador de bloques =========")

# Definición de función
def contar_bloques(n):
    if n == 1:
        return 1
    # Se retorna la suma de n (el nivel actual) más el resultado de contar_bloques(n - 1)
    else:
        return n + contar_bloques(n - 1)

# Solicitud, conversión y asignación de valor a variable
numero_bloques_nivel_bajo = int(input("Ingresá el número de bloques del nivel más bajo: "))

# Llamado a función y mensaje
print(f"Total de bloques necesarios: {contar_bloques(numero_bloques_nivel_bajo)}")

# Consigna 8: Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número. 

# Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4   
# contar_digito(123456, 7)     → 0

# Mensaje inicial
print("-------------- Ejercicio 8 --------------")
print ("== Veces que aparece un digito dentro de un número ==")

# Definición de función
def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        # Último dígito
        ultimo = numero % 10  
        # Resto del número
        resto = numero // 10  
        # Se compara el último dígito del número con el dígito buscado.
        # Si coincide el digito, suma 1 al contador y continúa con el resto del número.
        if ultimo == digito:  
            return 1 + contar_digito(resto, digito)
        # Si no coincide el digito, continúa con el resto sin sumar.
        else:
            return contar_digito(resto, digito)

# Solicitud, conversión y asignación de valor a variables
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese dígito a contar: "))

# Llamado a función y mensaje
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}.")