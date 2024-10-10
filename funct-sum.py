#Función para sumar todos los números de una lista

print (" ")
print ("Torres Olvera Gael")
print (" ")

def suma(lista):
    
    return sum(lista)

#Función para multiplicar todos los números de una lista

def multip(lista):
    
    resultado = 1
    
    for numero in lista:
        
        resultado *= numero
        
    return resultado

#Ejemplo de uso

numeros = [1, 2, 3, 4]

print(f"La suma es: {suma(numeros)}")
