# Datos de ventas por tienda y por mes
ventas = {
    "ABSA 1": [50000, 60000, 65000, 62000, 78000, 95000],
    "ABSA 2": [89000, 90000, 98000, 80000, 85000, 90000],
    "ABSA 3": [65000, 72000, 85000, 72000, 83000, 98000],
    "ABSA 4": [92000, 88000, 90000, 76000, 82000, 93000],
}

# Venta total por todas las tiendas
venta_total = sum(sum(meses) for meses in ventas.values())
print("-"*10)
print(f"Venta total por todas las tiendas: {venta_total}")
print("-"*10)

# Venta total por cada tienda
print("-"*10)
print("Venta total por tienda:")
print("-"*10)
ventas_por_tienda = {}
for tienda, mensual in ventas.items():
    total = sum(mensual)
    ventas_por_tienda[tienda] = total
    print(f"{tienda}: {total}")

# Tienda que mas vendio
mayor_venta = max(ventas_por_tienda, key=ventas_por_tienda.get)
print("-"*10)
print(f"Tienda que mas vendio: {mayor_venta} con {ventas_por_tienda[mayor_venta]}")
print("-"*10)

# Tienda que menos vendio
menor_venta = min(ventas_por_tienda, key=ventas_por_tienda.get)
print("-"*10)
print(f"Tienda que menos vendio: {menor_venta} con {ventas_por_tienda[menor_venta]}")
print("-"*10)