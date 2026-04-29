#Pide a la usuaria 5 veces que introduzca un color.
#Si la usuaria introduce el color azul, muestra que el premio ha sido conseguido. 
#Si introduce otro color, dile que pruebe otro color.

cantidad = 5

def color():
    
    for i in range(cantidad):
        color = input("Escribe un color: ")
        if color == 'azul':
            print("PREMIO CONSEGUIDO")
            break:
            
        else:
            print("Prueba con otro color")



















