# Escribe un programa que lea una lista de números enteros y realice las siguientes acciones:
# 
# 1. Si un número es positivo y par, divídelo entre 2.
# 2. Si un número es positivo y divisible entre 3 pero no entre 6, réstale 3.
# 3. Si un número es negativo, conviértelo en su valor absoluto.
# 4. Si un número es cero, cámbialo por el número mayor de la lista.
# 
# El programa debe cumplir las siguientes condiciones:
# - Utiliza únicamente condicionales (if, elif, else).
# - No uses bucles para realizar las transformaciones, pero la lista resultante debe imprimirse.
# 
# Ejemplo:
# Entrada:
# [12, -5, 9, 0, 15, -6, 3]
# 
# Salida:
# Lista transformada:
# [6, 5, 6, 12, 15, 6, 0]
# 
# Explicación:
# - 12 es positivo y par, así que se divide entre 2.
# - -5 es negativo, así que se convierte en 5.
# - 9 es positivo y divisible entre 3 pero no entre 6, así que se le resta 3.
# - 0 se reemplaza por el mayor número en la lista original (12).
# - 15 es positivo pero no cumple ninguna de las reglas anteriores, así que permanece igual.
# - -6 es negativo, así que se convierte en 6.
# - 3 es positivo pero no cumple ninguna de las reglas anteriores, así que permanece igual.

numeros = [-14, -8, -2, 0, 2, 6, 9, 12]
mayor = max(numeros)
lista = []
for num in numeros:
    if num > 0 and num % 2 == 0:
        lista.append(num // 2)
    elif num > 0 and num % 3 == 0 and num % 6 != 0:
        lista.append(num - 3)
    elif num < 0:
        lista.append(abs(num))
    elif num == 0:
        lista.append(mayor)
print("lista_transformada:")
print(lista)
