#Nombre: Doram Basdemir
#ID: 00582231
#Ejercicio 4

nombre_archivo = input('Ingresa nombre de archivo: ')
archivo = open(nombre_archivo)

palabras_lista = list()
for linea in archivo:
    palabras = linea.split()
    for palabra in palabras:
        if palabra not in palabras_lista:
            palabras_lista.append(palabra)

palabras_lista.sort()
print(palabras_lista)