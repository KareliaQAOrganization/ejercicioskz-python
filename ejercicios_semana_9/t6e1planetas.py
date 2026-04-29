#Planetas del sistema solar
#Crea una lista con los 8 planetas del sistema solar.
#Pide a la usuaria un número del 1 al 8.
#Muestra el planeta correspondiente.
#Si el número es inválido, muestra un mensaje de error.

#------------------ CORRECTO
#posicion = 0 ,          1,       2, ..... etc.
planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

numero = int(input("Escribe un numero entre 1 al 8: "))
posicion = numero - 1
planeta = 8

if numero <= planeta: 
    print("El planeta correspondiente es:", (planetas[posicion]))
else:
    print("Error: El número es inválido")




