#Ejercicio 1: Calculadora de nota media

#HASTA AHORA ESTO FUNCIONA:
#Pide a la usuaria cuántas notas desea introducir.
cantidad = int(input("Cuántas notas desea introducir? "))

#Solicita cada nota:

total = 0

for i in range(cantidad):
    nota = float(input("Escribe la nota: " ))
    total = total + nota
    print(total)

print(cantidad)



#Calcula y muestra la media.
nota_media = total / cantidad
print("La media es:", nota_media)

