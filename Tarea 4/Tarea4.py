#Si no es la 4 renombrala 
#Escribe un programa que recorra una matriz de números enteros 𝑀 × 𝑁
# M×N (por ejemplo, 5 filas y 5 columnas) y haga lo siguiente:

# Identifique si un número es primo.
# Si el número es primo, reemplázalo por el valor 1.
# Si no es primo, reemplázalo por el valor 0.

# Condiciones:
# Implementa la lógica para determinar si un número es primo usando un for y un if.
# Usa bucles anidados para recorrer la matriz.
# El programa debe imprimir tanto la matriz original como la matriz resultante.

# Ejemplo
# Si la matriz original es:
# [
#   [2, 4, 6],
#   [5, 9, 11],
#   [13, 15, 18]
# ]

# El resultado debería ser:
# [
#   [1, 0, 0],
#   [1, 0, 1],
#   [1, 0, 0]
# ]

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
def numero_primo(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True
def matriz_primos(matriz):
    matriz_final = []
    for fila in matriz:
        fila_final = []
    for numero in fila:
        if numero_primo(numero):
            fila_final.append(1)
        else:
            fila_final.append(0)
    matriz_final.append(fila_final)
    return matriz_final

print("Matriz original:")
for row in matriz:
    print(row)

matriz_final = matriz_primos(matriz)    
print("Matriz resultante:")
for row in matriz_final:
    print(row)