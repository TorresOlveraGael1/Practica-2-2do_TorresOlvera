import math

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Función para calcular la distancia entre dos puntos

def distancia(punto1, punto2):
    
    return math.sqrt((punto2[0] - punto1[0]) ** 2 + (punto2[1] - punto1[1]) ** 2)

#Ejemplo de uso

x1 = map(float, input("Introduce las coordenadas del primer punto (x1): ").split())

y1 = map(float, input("Introduce las coordenadas del primer punto (y1): ").split())

x2 = map(float, input("Introduce las coordenadas del segundo punto (x2): ").split())

y2 = map(float, input("Introduce las coordenadas del segundo punto (x2): ").split())

punto1 = (x1, y1)

punto2 = (x2, y2)

print(f"La distancia entre los dos puntos es: {distancia(punto1, punto2):.2f}")
