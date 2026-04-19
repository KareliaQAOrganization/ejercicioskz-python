#Pedir al usuario que introduzca 2 numeros
#Convertimos a numero. int (sin decimales), float(puede tener decimales)
numero1 = float(input("Introduzca un numero: "))
numero2 = float(input("Introduzca otro numero: "))

#Hacemos las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
media = (numero1 + numero2) / 2
# División entera (sin decimales)
division_entera = numero1 // numero2
# Módulo (resto de la división)
resto = numero1 % numero2
# Potencia
potencia = numero1 ** numero2

#Imprimimos los resultados
print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicacion: ", multiplicacion)
print("Division: ", division)
print("Media: ", media)
print("Division resultado entero: ", division_entera)
print("Resto de la division: ", resto)
print("Numero 1 elevado a la potencia del numero 2: ", potencia)