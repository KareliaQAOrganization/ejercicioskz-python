#Pide a la usuaria 5 veces que introduzca un color.
#Si la usuaria introduce el color azul, muestra que el premio ha sido conseguido. Si no, dile que pruebe otro color.


#color = print(input("Escribe un color: "))


for color in range(5):
    color = print(input("Escribe un color: "))
    if color == 'azul':
        print("El premio ha sido conseguido")
        break
    else:
        print(input("Intenta con otro color: "))
        continue
    print("Fin del juego")



resultado = ganador(premio)
