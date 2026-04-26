#Pide a la usuaria un número entre 1 y 10.
#El número ganador es el 4.
#Muestra:
#Mensaje de victoria si acierta.
#Mensaje de derrota si falla.


def ganador(numero):
    if numero == 4:
        print("VICTORIA: el número 4 es el ganador")
    elif numero <= 10 and numero != 4:
        print("DERROTA: otro es el número ganador")
    else:
        print("Escribiste un número fuera de rango")
    return()

numero = int(input("Escribe un número entre 1 y 10: "))
resultado = ganador(numero)