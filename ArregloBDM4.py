#Ingresar tamaño de la matriz (n x m)

# Ingresar número de filas y columnas (máximo 9)
n = int(input("Filas (1-9): "))
m = int(input("Columnas (1-9): "))

# Crear la matriz y pedir al usuario que ingrese los valores
matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        val = int(input(f"Valor [{i}][{j}]: "))
        fila.append(val)
    matriz.append(fila)

# Mostrar la suma de cada fila
print("\nSuma por fila:")
for i in range(n):
    print(f"Fila {i}: {sum(matriz[i])}")

# Mostrar el promedio de cada columna
print("\nPromedio por columna:")
for j in range(m):
    suma = 0
    for i in range(n):
        suma += matriz[i][j]
    print(f"Columna {j}: {suma / n:.2f}")

# Buscar el mayor valor y su posición en la matriz
mayor = matriz[0][0]
f_max, c_max = 0, 0
for i in range(n):
    for j in range(m):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            f_max, c_max = i, j
            
# Mostrar el mayor valor encontrado
print(f"\nMayor valor: {mayor} en [{f_max}][{c_max}]")
