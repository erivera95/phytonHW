matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matriz:
    print(row)

def suma_matriz(matriz):
    suma = 0
    for fila in matriz:
        for element in fila:
            suma += element
    return suma

def diagonal(matriz):
    diagonal = []
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])
    return diagonal

print("La suma de la matriz:", suma_matriz(matriz))
print("La diagonal de la matriz es:", diagonal(matriz))