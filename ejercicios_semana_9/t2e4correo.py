#Pide a la usuaria que introduzca una dirección de correo electrónico
correo = input("Escribe una dirección de correo electrónico válido: ")

#Muestra La longitud del correo
#Muestra el correo en mayúsculas
#Muestra el correo en minúsculas

longitud = len(correo)
correo_mayusculas = correo.upper()
correo_minusculas = correo.lower()

print("La longitud del correo es: ", longitud)
print("El correo electrónico en mayúsculas es así: ", correo_mayusculas)
print("El correo electrónico en minúsculas es así: ", correo_minusculas)