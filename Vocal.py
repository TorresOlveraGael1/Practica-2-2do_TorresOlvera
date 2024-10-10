#Función para verificar si un carácter es una vocal

print (" ")
print ("Torres Olvera Gael")
print (" ")

def es_vocal(caracter):
    
    return caracter.lower() in 'aeiou'

#Ejemplo de uso

caracter = input("Introduce un carácter: ")

print(f"¿Es vocal? {es_vocal(caracter)}")
