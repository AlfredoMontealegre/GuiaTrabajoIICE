# Matriz bidimensional ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Lista para almacenar la linealización
linealizada = []

# Proceso de linealización por columnas
filas = len(matriz)
columnas = len(matriz[0])

for j in range(columnas):
    for i in range(filas):
        linealizada.append(matriz[i][j])

# Mostrar resultados
print("Matriz original:")
for fila in matriz:
    print(fila)

print("\nArreglo linealizado por columnas:")
print(linealizada)