estudiantes = []  # Arreglo bidimensional para almacenar nombre y calificaciones

# Captura de datos
for i in range(5):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    calificaciones = []
    for j in range(3):
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación {j+1} de {nombre}: "))
                if 0 <= calificacion <= 100:
                    break
                else:
                    print("La calificación debe estar entre 0 y 100.")
            except ValueError:
                print("Error. Ingrese un número válido.")
        calificaciones.append(calificacion)
    estudiantes.append([nombre] + calificaciones)

# Cálculo y presentación de promedios
print("\nResultados:")
print("-" * 50)
print(f"{'Estudiante':<15}{'Calif 1':<10}{'Calif 2':<10}{'Calif 3':<10}{'Promedio':<10}")
print("-" * 50)

for estudiante in estudiantes:
    nombre = estudiante[0]
    promedio = sum(estudiante[1:]) / 3
    print(f"{nombre:<15}{estudiante[1]:<10}{estudiante[2]:<10}{estudiante[3]:<10}{promedio:<10.2f}")

print("-" * 50)