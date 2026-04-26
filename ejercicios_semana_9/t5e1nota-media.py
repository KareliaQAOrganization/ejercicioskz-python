#Ejercicio 1: Calculadora de nota media

#Pide a la usuaria cuántas notas desea introducir.
cantidad = int(input("Cuántas notas desea introducir? "))

#Solicita cada nota.
for i in range(cantidad):
    print(float(input("Escribe la nota: ")))
    print("Numero:", i)
    


#Suma todas las notas.
#print("Suma: ", suma)
def calcular_operaciones(a, b):
    suma = a + b
    return suma


#Calcula y muestra la media.
#nota_media = (nota1 + nota2 + nota3 +...) / cantidad_notas

#media = "La media de todas las notas es: ", nota_media

#print(media)
