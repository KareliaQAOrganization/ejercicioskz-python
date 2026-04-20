#Pide a la usuaria una cantidad en euros
cantidad_euros = float(input("Por favor escribe una cantidad en euros: "))

#Convierte la cantidad a
dolar = cantidad_euros * 1.1
libra = cantidad_euros * 0.87

#Muestra los resultados
print(cantidad_euros, "euros, es igual a", dolar, "dólares.")
print(cantidad_euros, "euros, es igual a", libra, "libras.")