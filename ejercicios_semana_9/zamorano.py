#PARTE 1: Pedir datos
#Pregunta cuántas notas quiere introducir la usuaria
#Usa un bucle para pedir cada nota
#Guarda todas las notas en una lista
#PARTE 2: Validación (condicional)
#Si la usuaria introduce una nota menor que 0 o mayor que 10:
#NO la guardes
#Muestra: "Nota inválida"
#(aquí puedes usar continue si quieres)
#PARTE 3: Cálculos (operaciones)
#Con las notas válidas:
#Calcula la suma total
#Calcula la media
#PARTE 4: Resultado (condicional)
#Si la media ≥ 5 → mostrar "Aprobado"
#Si la media < 5 → mostrar "Suspendido"

cantidad = int(input("Cuántas notas quiere introducir?: "))

def sumar_notas(cantidad):
    notas = []
    total = 0
    
    for i in range(cantidad):
        nota = float(input("Cuál es la nota?: "))
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            total = total + nota
        else:
            print("Nota inválida")
    return notas, total

def calcular_media(notas, total):
    if len(notas) > 0:
        return total / len(notas)
    else:
        return 0

def resultado(notas, media):
    if len(notas) == 0:
        print("No hay notas válidas")
    else:
        if media >= 5.0:
            print("Aprobado")
        else:
            print("Suspendido")

notas, total = sumar_notas(cantidad)
media = calcular_media(notas, total)

print("Las notas introducidas son:", notas)
print("La suma total es: ", total)
print("La media de las notas válidas es:", media)


