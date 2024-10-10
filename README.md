# Practica-2-2do_TorresOlvera

Torres Olvera Gael

En esta practica realizamos multiples codigos en python

# 1.Saludo

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Definimos la función

def saludar():

    print("Hey amigos!")

#Llamamos a la función

saludar()

![image](https://github.com/user-attachments/assets/1afe7433-2c29-4dfb-94be-6ac0f52ea773)
![image](https://github.com/user-attachments/assets/1adb578e-cdb7-46c4-b737-2072f2412958)


# 2.String

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Definimos la función

def saludar(nombre):

    print(f"¡Hola {nombre}!")

#Solicitar el nombre al usuario

nombre = input("Introduce tu nombre: ")

#Llamamos a la función con el nombre ingresado

saludar(nombre)

![image](https://github.com/user-attachments/assets/ab6cec66-ee02-4548-aaed-e4016a5d98c3)
![image](https://github.com/user-attachments/assets/8fc423e9-cf5a-41e8-ae9f-97d91fd06cbf)

# 3.Factorial

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


![image](https://github.com/user-attachments/assets/14a9e073-18f4-436d-a90a-eca65c777a22)
![image](https://github.com/user-attachments/assets/cb68703e-31d2-49aa-9b44-1f70706927ee)

# 4.IVA

#Función para calcular el total de la factura con IVA

print (" ")
print ("Torres Olvera Gael")
print (" ")

def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    
    iva = (porcentaje_iva / 100) * cantidad_sin_iva

    total = cantidad_sin_iva + iva
    
    return total


#Solicitar la cantidad sin IVA

cantidad_sin_iva = float(input("Introduce la cantidad sin IVA: "))

#Solicitar el porcentaje de IVA a aplicar

porcentaje_iva_input = input("Introduce el porcentaje de IVA a aplicar (presiona Enter para usar 21%): ")

#Comprobar si se ingresó un porcentaje de IVA

if porcentaje_iva_input:
    
    porcentaje_iva = float(porcentaje_iva_input)
    
else:
    
    porcentaje_iva = 21  # Valor por defecto


#Calcular el total de la factura

total_factura = calcular_total_factura(cantidad_sin_iva, porcentaje_iva)

#Mostrar el resultado

print(f"El total de la factura después del IVA es: {total_factura:.2f}")


![image](https://github.com/user-attachments/assets/d7856175-166a-4c8a-a06e-73d887ebf3d5)
![image](https://github.com/user-attachments/assets/9a9c06c4-4603-4bd7-91fa-f9d2c9b0b5b0)

# 5.calculo

print (" ")
print ("Torres Olvera Gael")
print (" ")

import math

#Función para calcular el área de un círculo

def area_circulo(radio):

    return math.pi * radio ** 2

#Función para calcular el volumen de una esfera

def volumen_esfera(radio):
    
    return (4/3) * math.pi * radio ** 3

#Función para calcular el volumen de un cilindro

def volumen_cilindro(radio, altura):
    
    return area_circulo(radio) * altura

#Ejemplo de uso

radio = float(input("Introduce el radio del círculo/esfera: "))

altura = float(input("Introduce la altura del cilindro: "))

print(f"Área del círculo: {area_circulo(radio):.2f}")

print(f"Volumen de la esfera: {volumen_esfera(radio):.2f}")

print(f"Volumen del cilindro: {volumen_cilindro(radio, altura):.2f}")

![image](https://github.com/user-attachments/assets/4090d186-812c-4dcc-a3a5-1cda582299f3)
![image](https://github.com/user-attachments/assets/92a90a21-4310-4b5e-9d0b-7e9c0d4586db)


# 6.Capturar

#Función para validar el email

print(" ")
print("Torres Olvera Gael")
print(" ")

def validar_email(email):
    
    return '@' in email

# Solicitar el email al usuario

email = input("Introduce tu dirección de email: ")

if validar_email(email):
    
    print("La dirección de email es válida.")
    
else:
    
    print("La dirección de email no es válida.")

![image](https://github.com/user-attachments/assets/de282f7c-3d03-4ea8-bd2b-60ad31ef70be)
![image](https://github.com/user-attachments/assets/7f90f2ed-357b-44d6-8186-05f24a5d70ee)

# 7.Longitud

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

![image](https://github.com/user-attachments/assets/54a9658f-e659-4075-878a-2c4c067a33c2)
![image](https://github.com/user-attachments/assets/a89c06d0-e301-4440-9a7d-df7f1b8839e9)

# 8.tresnumeros

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

![image](https://github.com/user-attachments/assets/62f79a83-f327-46fb-8663-dd88e5acc26a)
![image](https://github.com/user-attachments/assets/222cc4af-279f-478e-9118-ef159fdf69a1)

# 9.funct-sum


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

![image](https://github.com/user-attachments/assets/fd865b1d-380a-48fd-8b19-172905f73f5c)
![image](https://github.com/user-attachments/assets/de6be861-05d5-4e2b-83a6-c1be4373e6bc)

# 10.Vocal

#Función para verificar si un carácter es una vocal

print (" ")
print ("Torres Olvera Gael")
print (" ")

def es_vocal(caracter):
    
    return caracter.lower() in 'aeiou'

#Ejemplo de uso

caracter = input("Introduce un carácter: ")

print(f"¿Es vocal? {es_vocal(caracter)}")


![image](https://github.com/user-attachments/assets/ba880cf2-d1db-48a7-974f-6437d9c52e5d)
![image](https://github.com/user-attachments/assets/7cf44fda-935b-4c03-868f-668bd4508fcb)

# 11.Distancia

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

![image](https://github.com/user-attachments/assets/baa3427f-12b2-4b31-8014-d79cf1da2892)

