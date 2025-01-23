# Escribe un programa que lea una lista de valores y realice las siguientes acciones:
#
# 1. Intenta convertir cada valor de la lista a un número entero.
# 2. Si el valor es convertible, añádelo a una nueva lista.
# 3. Si no es convertible, captura la excepción y añade el mensaje "Valor inválido" a la nueva lista.
# 
# Al final, imprime la lista original y la lista resultante.
# 
# Reglas:
# - Usa exclusivamente manejo de excepciones (`try-except`) para controlar los errores.
# - No uses condicionales (`if-else`) en la lógica del programa.
#
# Ejemplo:
# Entrada:
# ["10", "veinte", 30, None, 15.5, "50"]
#
# Salida:
# Lista original:
# ["10", "veinte", 30, None, 15.5, "50"]
#
# Lista resultante:
# [10, "Valor inválido", 30, "Valor inválido", "Valor inválido", 50]

valores = ["10", "23", "veinte", "15.6", "30", "cien"]
lista = []
for valor in valores:
    try:
        lista.append(int(valor))
    except:
        lista.append("Valor inválido")

print("Lista original:")
print(valores)

print("\nLista resultante:")
print(lista)


#Agregar un try mas para los numeros decimales y cada que uno exista, poner un mensaje de "Numero decimal"