"""
1. La Abarrotera ABSA tiene 4 sucursales en las cuales se realizaron diferentes ventas en los
meses de Julio a diciembre del año 2022, se le ha solicitado a usted realizar un programa en
donde pueda capturar la siguiente tabla de datos:

Estado de cuenta de las Sucursales ABSA en el segundo semestre 2022
Tienda/Mes Julio Agosto Septiembre Octubre Noviembre Diciembre
ABSA 1 50,000 60,000 65,000 62,000 78,000 95,000
ABSA 2 89,000 90,000 98,000 80,000 85,000 90,000
ABSA 3 65,000 72,000 85,000 72,000 83,000 98,000
ABSA 4 92,000 88,000 90,000 76,000 82,000 93,000

y nos presente los siguientes resultados:
a. Venta total por todas las tiendas
b. Venta total por tienda
c. Tienda que más vendió en los 6 meses
d. Tienda que menos vendió
"""

# Lista de nombres de las tiendas
tiendas = ["ABSA 1", "ABSA 2", "ABSA 3", "ABSA 4"]

# Arreglo bidimensional con las ventas de cada tienda por mes (Desde Julio a Diciembre)
ventas = [
    [50000, 60000, 65000, 62000, 78000, 95000],  # ABSA 1
    [89000, 90000, 98000, 80000, 85000, 90000],  # ABSA 2
    [65000, 72000, 85000, 72000, 83000, 98000],  # ABSA 3
    [92000, 88000, 90000, 76000, 82000, 93000]   # ABSA 4
]

# Venta total por todas las tiendas
total_general = 0
# Se recorderan todas las tiendas (fila) y sus valores al mes (venta)
for fila in ventas:
    for venta in fila:
        total_general += venta

# Venta total por cada tienda
# Cada que se agrega un "[]" se guardaran datos dentro de ese arreglo
totales_por_tienda = []
for fila in ventas:
    total_tienda = 0
    for venta in fila:
        # Se agrega una sumatoria cual se agregara a los datos "totales por tienda"
        total_tienda += venta
    totales_por_tienda.append(total_tienda)

# Tienda que mas vendio al final
mayor_venta = totales_por_tienda[0]
indice_mayor = 0
for i in range(1, len(totales_por_tienda)):
    # Se hace el if con mayor para convalidar el total (y saber cuando es mayor o menor)
    if totales_por_tienda[i] > mayor_venta:
        mayor_venta = totales_por_tienda[i]
        indice_mayor = i

# Tienda que menos termino vendiendo
menor_venta = totales_por_tienda[0]
indice_menor = 0
for i in range(1, len(totales_por_tienda)):
    if totales_por_tienda[i] < menor_venta:
        menor_venta = totales_por_tienda[i]
        indice_menor = i

# Impresion de los resultados finales
print("===== Resultados de Ventas ABSA =====")
print(f"Venta total por todas las tiendas: {total_general}")

# Se imprimen cada nombre y registro de los resultados ABSA (Cada uno)
print("Venta total por tienda:")
for i in range(len(tiendas)):
    print(f"{tiendas[i]}: {totales_por_tienda[i]}")

# Se imprimen los demas registros pedidos 
print(f"Tienda que mas vendio: {tiendas[indice_mayor]} con {mayor_venta}")
print(f"Tienda que menos vendio: {tiendas[indice_menor]} con {menor_venta}")