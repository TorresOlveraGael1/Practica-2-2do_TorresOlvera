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