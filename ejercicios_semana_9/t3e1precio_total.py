#Precio total de un producto
def compra(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal

def descuento(subtotal, descuento_porcentaje):
    subtotal_descuento = subtotal - (subtotal * descuento_porcentaje / 100)
    return subtotal_descuento

def iva(subtotal_descuento, iva_porcentaje):
    total = subtotal_descuento + (subtotal_descuento * iva_porcentaje / 100)
    return total

#Solicita a la usuaria
#Muestra el resultado final
def total_pagar():
    producto = input("Escribe el nombre del producto: ")
    precio = float(input("Escribe el precio por unidad en euros: "))
    cantidad = int(input("Escribe la cantidad de unidades a comprar: "))
    descuento_porcentaje = float(input("Escribe el porcentaje de descuento: "))
    iva_porcentaje = float(input("Escribe el IVA en porcentaje: "))
    subtotal = compra(precio, cantidad)
    subtotal_descuento = descuento(subtotal, descuento_porcentaje)
    total = iva(subtotal_descuento, iva_porcentaje)
    print("Si compra", cantidad, producto, "el total a pagar será:", total, "euros.")


total_pagar()