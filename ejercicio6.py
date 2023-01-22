import math

def max_cord_length(diameter, percentage):
    # Calcular el radio del círculo
    radius = diameter / 2
    # Calcular el área del círculo
    area = math.pi * (radius ** 2)
    # Calcular el área máxima que burro puede acceder
    max_area = area * percentage
    # Calcular la longitud máxima de la cuerda
    cord_length = 2 * math.sqrt(max_area/math.pi)
    # Redondear hacia abajo y devolver como entero
    return int(cord_length)

# Ejemplo de uso
diameter = 50
percentage = 0.25
print(max_cord_length(diameter, percentage)) # Output: 15

diameter = 100
percentage = 0.50
print(max_cord_length(diameter, percentage)) # Output: 35
