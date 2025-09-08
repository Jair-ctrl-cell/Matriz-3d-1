# Definir dimensiones
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 2  # Ejemplo con 2 semanas

# Crear matriz 3D [ciudad][semana][día]
# Se simulan temperaturas con valores ficticios
import random

matriz_temperaturas = [
    [  # Para cada ciudad
        [random.randint(10, 30) for _ in dias_semana]  # Semana 1
        for _ in range(num_semanas)  # Varias semanas
    ]
    for _ in ciudades
]

# Calcular promedios de temperatura por ciudad y semana
for i, ciudad in enumerate(ciudades):  # Iterar por ciudad
    print(f"\nPromedios de temperaturas para {ciudad}:")
    for j in range(num_semanas):  # Iterar por semana
        suma = 0
        for k in range(len(dias_semana)):  # Iterar por días
            suma += matriz_temperaturas[i][j][k]

        promedio = suma / len(dias_semana)
        print(f"  Semana {j + 1}: {promedio:.2f} °C")

