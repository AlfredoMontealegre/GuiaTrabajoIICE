# Arreglo de 3 vendedores x 4 zonas
ventas = []
for v in range(3):
    fila = []
    print(f"\nVendedor {v}:")
    for z in range(4):
        val = int(input(f"  Zona {z}: "))
        fila.append(val)
    ventas.append(fila)

# Calcular las ventas totales por zona
zonas = [0, 0, 0, 0]
for z in range(4):
    for v in range(3):
        zonas[z] += ventas[v][z]
zona_max = zonas.index(max(zonas))
print(f"\nZona con más ventas: {zona_max} ({zonas[zona_max]})")

# Buscar la zona con más ventas
suma_vend = [sum(ventas[v]) for v in range(3)]
v_min = suma_vend.index(min(suma_vend))
print(f"Vendedor con menos ventas: {v_min} ({suma_vend[v_min]})")

# Calcular el total de todas las ventas
total = sum(suma_vend)
print(f"Total vendido: {total}")
