#Ejercicio 2: Meses del año
#Crea una lista con los 12 meses del año.
#Pide a la usuaria un número del 1 al 12.
#Muestra el mes correspondiente.
#Si el mes es junio, muestra además el mensaje: EL MEJOR MES.


meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

numero = int(input("Escribe un numero entre 1 al 12: "))
posicion = (numero - 1)
mes_letras = 12
mes_mejor = 6

if numero <= mes_letras:
    print("El mes correspondiente es:", (meses[posicion]))
    if numero == mes_mejor:
        print("EL MEJOR MES")
else:
    print("No es un número válido")





