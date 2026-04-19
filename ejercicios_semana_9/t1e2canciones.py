#1. Pide a la usuaria que introduzca la siguiente información sobre su canción favorita
cancion = input("Cuál es tu canción favorita? ")
artista = input("Quién canta la canción? ")
album = input("Cuál es el nombre del Álbum? ")
lanzamiento = input("Cuál es el año de lanzamiento? ")
duracion = input("Cuál es el duración en segundos? ")
videoclip = input("¿Tiene videoclip (verdadero o falso)? ")

#2. Muestra la información introducida
print("Tu canción favorita es: ", cancion)
print("Es interpretada por: ", artista)
print("Forma parte del álbum: ", album)
print("Su lanzamiento fue en el año: ", lanzamiento)
print("Tiene una duración de: ", duracion, "segundos")
print("Tiene videoclip?: ", videoclip)


#3. Solicita los mismos datos de la canción que menos le guste
cancion2 = input("Cuál es tu canción menos favorita? ")
artista2 = input("Quién canta la canción? ")
album2 = input("Cuál es el nombre del Álbum? ")
lanzamiento2 = input("Cuál es el año de lanzamiento? ")
duracion2 = input("Cuál es el duración en segundos? ")
videoclip2 = input("¿Tiene videoclip (verdadero o falso)? ")

#4. Muestra la información introducida
print("Tu canción menos favorita es: ", cancion2)
print("Es interpretada por: ", artista2)
print("Es parte del álbum: ", album2)
print("Se lanzó en el año: ", lanzamiento2)
print("La duración es de: ", duracion2, "segundos")
print("Tiene videoclip?: ", videoclip2)