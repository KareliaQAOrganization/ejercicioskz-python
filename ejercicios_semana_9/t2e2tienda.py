#Define los siguientes precios
camiseta = 10
sudadera = 20.5
gorra = 5.5

#Pide a la usuaria la cantidad de cada artículo
cantidad_camiseta = int(input("Cuántas camisetas comprará? "))
cantidad_sudadera = int(input("Cuántas sudaderas comprará? "))
cantidad_gorra = int(input("Cuántas gorras comprará? "))

#Calcula el total de la compra
total_compra = (camiseta * cantidad_camiseta) + (sudadera * cantidad_sudadera) + (gorra * cantidad_gorra)

#Añade el 21% de IVA al total
IVA = (total_compra * 21) / 100
totalIVA = total_compra + IVA

#Muestra el precio final
print ("Total de su compra:", totalIVA, "euros")