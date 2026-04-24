#Precio total de un producto
def subtotal_compra(precio_u,cantidad_u):
    subtotal = precio_u * cantidad_u
    return subtotal

def total_descuento(descuento_porcentaje):
    descuento = subtotal_compra(precio_u,cantidad_u) - ((subtotal_compra(precio_u,cantidad_u)) * (descuento_porcentaje / 100))
    return descuento

def total_iva(iva_porcentaje):
    total = (total_descuento(descuento_porcentaje) + ((total_descuento(descuento_porcentaje) * iva_porcentaje)) / 100)
    return total

#Solicita a la usuaria:
nombre_producto = input("Escribe el nombre del producto: ")
precio_u = float(input("Escribe el precio por unidad en euros: "))
cantidad_u = int(input("Escribe la cantidad de unidades a comprar: "))
descuento_porcentaje = float(input("Escribe el porcentaje de descuento: "))
iva_porcentaje = float(input("Escribe el IVA en porcentaje: "))

#Muestra el resultado final
subtotal = subtotal_compra(precio_u,cantidad_u)
descuento = total_descuento(descuento_porcentaje)
total = total_iva(iva_porcentaje)
print("Si compra", cantidad_u, nombre_producto, "el total a pagar será:", total, "euros.")

