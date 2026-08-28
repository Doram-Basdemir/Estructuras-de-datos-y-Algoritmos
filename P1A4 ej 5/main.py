#Nombre: Doram Basdemir
#ID: 00582231
#Ejercicio 5

nombre_archivo = input('Ingresa un nombre de archivo: ')
archivo = open(nombre_archivo)

contador = 0
for linea in archivo:
    palabras = linea.split()
    if len(palabras) == 0:
        continue
    if palabras[0] != 'From':
        continue
    print(palabras[1])
    contador = contador + 1

print('Hay', contador, 'lineas en el archivo con la palabra From al inicio')