#Función para encontrar el mayor de tres números

print (" ")
print ("Torres Olvera Gael")
print (" ")

def mayor_de_tres(num1, num2, num3):
    
    return max(num1, num2, num3)

#Ejemplo de uso

n1 = float(input("Introduce el primer número: "))

n2 = float(input("Introduce el segundo número: "))

n3 = float(input("Introduce el tercer número: "))

print(f"El mayor de los tres números es: {mayor_de_tres(n1, n2, n3)}")