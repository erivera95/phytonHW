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
