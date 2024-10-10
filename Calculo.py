# Calculo

print (" ")
print ("Torres Olvera Gael")
print (" ")

import math

# Función para calcular el área de un círculo

def area_circulo(radio):

    return math.pi * radio ** 2

# Función para calcular el volumen de una esfera

def volumen_esfera(radio):
    
    return (4/3) * math.pi * radio ** 3

# Función para calcular el volumen de un cilindro

def volumen_cilindro(radio, altura):
    
    return area_circulo(radio) * altura

# Ejemplo de uso

radio = float(input("Introduce el radio del círculo/esfera: "))

altura = float(input("Introduce la altura del cilindro: "))

print(f"Área del círculo: {area_circulo(radio):.2f}")

print(f"Volumen de la esfera: {volumen_esfera(radio):.2f}")

print(f"Volumen del cilindro: {volumen_cilindro(radio, altura):.2f}")
