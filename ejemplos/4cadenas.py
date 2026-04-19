#Guardamos la ciudad del usuario
ciudad = input("Introduce tu ciudad: ")
#unimos 2 cadenas
bienvenida = "Bienvenidos a " + ciudad
#obtenemos el numero de letras de la cadena
longitud = len(bienvenida)
#poner la cadena en mayusculas
bienvenidamayusculas = bienvenida.upper()
#poner la cadena en minusculas
bienvenidaminusculas = bienvenida.lower()
#reemplazar texto
texto = bienvenida
nuevo_texto = texto.replace("Bienvenidos a ", "Sean Bienvenidos a ")
#Eliminar espacios al inicio y final
texto = "    Buenos días     "
limpio = texto.strip()
#Dividir una cadena en una lista
texto = "Como estas?"
palabras = texto.split()
#Verificar si contiene un texto
texto = bienvenida
contiene = "Sean" in texto.lower()



#IMPRIMIR CADENAS
#imprimimos la palabra
print(bienvenida)
#imprimir la longitud (al ser un numero no puede ir solo)
print("Longitud ", longitud)
#imprimir cadena en mayusculas
print(bienvenidamayusculas)
#imprimir la cadena en minusculas
print(bienvenidaminusculas)
#imprimir reemplazo de texto
print(nuevo_texto)
#imprimir sin espacios al inicio y final
print(limpio)
#imprimir una cadena en una lista
print(palabras)
#imprimir si contine un texto
print(contiene)