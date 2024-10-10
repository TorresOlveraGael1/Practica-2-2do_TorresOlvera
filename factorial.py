# Factoral

#Definimos la función para calcular el factorial

print(" ")

print("Torres Olvera Gael")

print(" ")

def factorial(n):
    
    if n == 0 or n == 1:
        
        return 1
        
    else:
        
        return n * factorial(n - 1)

#Solicitar un entero positivo al usuario

numero = int(input("Introduce un entero positivo: "))

#Validar que el número sea positivo

if numero < 0:
    
    print("Por favor, introduce un entero positivo.")
else:
    
    # Calcular y mostrar el factorial
    
    resultado = factorial(numero)
    
    print(f"El factorial de {numero} es {resultado}.")