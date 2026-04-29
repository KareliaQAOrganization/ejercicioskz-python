#Ejercicio 1: Calculadora de nota media
#Pide a la usuaria cuántas notas desea introducir.
#Solicita cada nota:
#Calcula y muestra la media.





def calculadora(cantidad):

    total = 0

    for i in range(cantidad):
        nota = float(input("Escribe la nota: " ))
        total = total + nota

    nota_media = total / cantidad

    return nota_media

def calculadora ():

cantidad = int(input("Cuántas notas desea introducir? "))

nota_media = calculadora(cantidad)

print("La media es:", nota_media)

calculadora ()