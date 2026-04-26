def notaFinal(nota):
    if (nota > 8):
        mensaje = "SOBRESALIENTE"
    elif (nota < 5):
        mensaje = "SUSPENSO"
    else:
        mensaje = "APROBADO"
    return mensaje

#Pedimos al usuario que introduzca su nota

nota = float(input("Introduce tu nota del examen: "))

#Llamamos a nota final para que nos diga el mensaje
mensaje = notaFinal(nota)
#imprimimos el mensaje con la nota final
print(mensaje)


#2Llamamos a nota final para que nos diga el mensaje
mensaje2 = "Su nota final es: ", notaFinal(nota)
#imprimimos el mensaje con la nota final
print(mensaje2)