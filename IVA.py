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

# Comprobar si se ingresó un porcentaje de IVA

if porcentaje_iva_input:
    
    porcentaje_iva = float(porcentaje_iva_input)
    
else:
    
    porcentaje_iva = 21  # Valor por defecto


#Calcular el total de la factura

total_factura = calcular_total_factura(cantidad_sin_iva, porcentaje_iva)

#Mostrar el resultado

print(f"El total de la factura después del IVA es: {total_factura:.2f}")
