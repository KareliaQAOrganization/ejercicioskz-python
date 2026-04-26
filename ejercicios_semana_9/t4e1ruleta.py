#Ruleta de la fortuna de los colores
def ruleta(color):
    if color == 'rojo':
        print("Su fortuna elegida es: pasión y energía")
    elif color == 'verde':
        print("Su fortuna elegida es: esperanza y crecimiento")
    elif color == 'azul':
        print("Su fortuna elegida es: calma y serenidad")
    elif color == 'amarillo': 
        print("Su fortuna elegida es: felicidad y optimismo")
    elif color == 'morado':
        print("Su fortuna elegida es: sabiduría y creatividad")
    elif color != 'rojo' or 'verde' or 'azul' or 'amarillo' or 'morado':
        print("No es un color válido")
    return()

#Pide a la usuaria que elija un color
#Muestra un mensaje según el color elegido
color = input("Escribe en minúsculas cuál color prefieres: rojo, verde, azul, amarillo o morado: ")
resultado = ruleta(color)


