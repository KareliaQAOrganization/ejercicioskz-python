#Ejercicio 1: Calculadora de nota media

#HASTA AHORA ESTO FUNCIONA:
#Pide a la usuaria cuántas notas desea introducir.
cantidad = int(input("Cuántas notas desea introducir? "))
notas = []


#Solicita cada nota:
for i in range(cantidad):
    nota = float(input("Escribe la nota: " ))
    notas.append(nota)

notas_completas = notas.append(nota)

print(cantidad)


#Calcula y muestra la media.
nota_media = notas / cantidad
media = print("La media de todas las notas es: ", nota_media)
print(media)
