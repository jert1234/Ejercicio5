def calculadora():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operador = input("Seleccione la operación (+, -, *, /): ")

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 == 0:
            resultado = "Error: División por cero"
        else:
            resultado = num1 / num2
    else:
        resultado = "Operador no válido"

    print(f"Resultado: {num1} {operador} {num2} = {resultado}")

calculadora()

def contar_vocales(cadena):
    cadena = cadena.lower()
    contador = 0
    for letra in cadena:
        if letra in "aeiou":
            contador += 1
    return contador

cadena = input("Ingrese una cadena de texto: ")
num_vocales = contar_vocales(cadena)
print(f"Número de vocales: {num_vocales}")

def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

numero = int(input("Ingrese un número: "))
resultado = es_primo(numero)
print(f"Es primo: {resultado}")

def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

cadena = input("Ingrese una cadena de texto: ")
num_palabras = contar_palabras(cadena)
print(f"Número de palabras: {num_palabras}")

def potencia(base, exponente):
    resultado = base ** exponente
    print(f"{base}^{exponente} = {resultado}")

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
potencia(base, exponente)