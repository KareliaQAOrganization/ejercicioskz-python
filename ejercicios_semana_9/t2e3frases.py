#Pide a la usuaria que introduzca una frase
frase = input("Escribe una frase porfavor: ")

#Muestra La longitud de la frase
#Muestra La frase en mayúsculas
#Muestra La frase en minúsculas

longitud = len(frase)
frase_mayusculas = frase.upper()
frase_minusculas = frase.lower()

print("La longitud de la frase es: ", longitud)
print("La frase en mayúsculas es así: ", frase_mayusculas)
print("La frase en minúsculas es así: ", frase_minusculas)