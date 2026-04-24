#Definimos una funcion SIN PARAMETROS
def saludar():
    print("Hola que tal ")

#1. Llamamos a la funcion
saludar()
saludar()

#----------------------------------------------------------
#Definir funciones que RECIBENy DEVUELVEN PARAMETROS
def saludarConNombre(nombre):
    saludo = "Hola que tal " + nombre
    return saludo

#1. guardamos el nombre
nombre = input("Introduce tu nombre: ")
saludo = saludarConNombre(nombre)
print(saludo)

nombre2 = input("Introduce tu nombre 2: ")
saludo2 = saludarConNombre(nombre2)
print(saludo2)

#----------------------------------------------------------
#Funciones con múltiples parámetros
def calcular_area(base, altura):
    area = base * altura / 2
    return area

#1. Llamar a la función con dos argumentos
area_triangulo = calcular_area(10, 5)

#2. Mostrar el área calculada
print(area_triangulo)

#Funciones que devuelven valores
def sumar(a, b):
    resultado = a + b
    return resultado

#1. Guardar el resultado en una variable
total = sumar(5, 3)
print("El total es:", total)

#Devolver múltiples valores
def calcular_operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

#1. Recibir múltiples valores
resultado_suma, resultado_resta = calcular_operaciones(10, 3)
print("Suma:", resultado_suma)
print("Resta:", resultado_resta)

#Funciones sin return
def mostrar_mensaje():
    print("Este mensaje se muestra pero no devuelve nada")

resultado = mostrar_mensaje()
print(resultado)