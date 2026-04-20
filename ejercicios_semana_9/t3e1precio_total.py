#Precio total de un producto
#Solicita a la usuaria:
nombre_producto = input("Escribe el nombre del producto: ")
precio_u = float(input("Escribe el precio por unidad en euros: "))
cantidad_u = int(input("Escribe la cantidad de unidades a comprar: "))
descuento_porcentaje = float(input("Escribe el porcentaje de descuento: "))
IVA_porcentaje = float(input("Escribe el IVA en porcentaje: "))

#Calcula el precio total aplicando descuento e IVA
subtotal = precio_u * cantidad_u
descuento = (subtotal * descuento_porcentaje) / 100
subtotal_descuento = subtotal - descuento
IVA = (subtotal_descuento * IVA_porcentaje) / 100
total = subtotal_descuento + IVA

#Muestra el resultado final
print("Si compra", cantidad_u, nombre_producto, "el total a pagar será:", total, "euros.")