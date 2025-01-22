# Escribe un programa que lea una lista de valores y procese cada uno según las siguientes reglas:
# 
# 1. Si el valor es un número entero:
#    - Si es positivo, añade "Positivo" a una nueva lista.
#    - Si es negativo, añade "Negativo" a la nueva lista.
# 2. Si el valor es un número flotante, añade "Decimal" a la nueva lista.
# 3. Si el valor no es un número, ignóralo utilizando `pass`.
# 4. Si ocurre cualquier otro tipo de error al procesar el valor (por ejemplo, una operación inválida), 
#    captura la excepción y añade "Error" a la nueva lista.
# 
# Al final, imprime la lista original y la nueva lista resultante.
# 
# Ejemplo:
# Entrada:
# [5, -3, 4.2, "texto", None, 0, -2.7]
# 
# Salida:
# Lista original:
# [5, -3, 4.2, 'texto', None, 0, -2.7]
# 
# Lista resultante:
# ['Positivo', 'Negativo', 'Decimal', 'Error', 'Error', 'Positivo', 'Decimal']

valores = [10, 8, 4.2, 0, -2, "-13.3"]
lista = []
for valor in valores:
    try:
        if type(valor) == int:
            if valor > 0:
                lista.append("Positivo")
            else:
                lista.append("Negativo")
        elif type(valor) == float:
            lista.append("Decimal")
    except:
        lista.append("Error")
print("Lista original:")
print(valores)

print("\nLista resultante:")
print(lista)
