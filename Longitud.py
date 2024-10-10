#Función para calcular la longitud de la última palabra

print (" ")
print ("Torres Olvera Gael")
print (" ")

def longitud_ultima_palabra(texto):
    
    palabras = texto.strip().split()
    
    return len(palabras[-1]) if palabras else 0

#Ejemplo de uso

frase = input("Introduce una frase: ")

print(f"La longitud de la última palabra es: {longitud_ultima_palabra(frase)}")
