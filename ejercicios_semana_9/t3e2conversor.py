#Pide a la usuaria una cantidad en euros
#1. Convierte la cantidad a
#2. Muestra los resultados
def euro_dolar(cantidad_euros):
    convertir_dolar = float(cantidad_euros * 1.1)
    return convertir_dolar

def euro_libra(cantidad_euros):
    convertir_libra = float(cantidad_euros * 0.87)
    return convertir_libra

cantidad_euros = float(input("Escribe un valor en euros: "))
convertir_dolar = euro_dolar(cantidad_euros)
print(convertir_dolar)

convertir_libra = euro_libra(cantidad_euros)
print(convertir_libra)