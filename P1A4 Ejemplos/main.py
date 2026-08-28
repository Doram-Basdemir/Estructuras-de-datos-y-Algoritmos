#Nombre: Doram Basdemir
#ID: 00582231
#Ejercicios de ejemplo

frutas = ['manzana', 'pera', 'uva']
numeros = [5, 10, 15]
vacia = []
print(frutas, numeros, vacia)

colores = ['rojo', 'verde', 'azul']
print(colores[0])

numeros = [5, 10]
numeros[1] = 20
print(numeros)

print('verde' in colores)
print('negro' in colores)

colores = ['rojo', 'verde', 'azul']
for color in colores:
    print(color)

numeros = [5, 10, 15]
for i in range(len(numeros)):
    numeros[i] = numeros[i] * 2
print(numeros)

a = [10, 20, 30]
b = [40, 50, 60]
c = a + b
print(c)

print([7] * 5)
print([2, 4, 6] * 2)

t = ['p', 'q', 'r', 's', 't', 'u']
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

t[1:3] = ['m', 'n']
print(t)

t = ['lunes', 'martes', 'miercoles']
t.append('jueves')
print(t)

t1 = ['norte', 'sur']
t2 = ['este', 'oeste']
t1.extend(t2)
print(t1)

t = ['zorro', 'oso', 'perro', 'gato', 'ave']
t.sort()
print(t)

t = ['rojo', 'verde', 'azul']
x = t.pop(1)
print(t)
print(x)

t = ['perro', 'gato', 'ave']
del t[1]
print(t)

t = ['lunes', 'martes', 'miercoles']
t.remove('martes')
print(t)

t = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
del t[1:5]
print(t)

nums = [8, 22, 5, 19, 3, 41]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums) / len(nums))

s = 'texto'
t = list(s)
print(t)

s = 'el sol brilla hoy'
t = s.split()
print(t)
print(t[2])

s = 'uno-dos-tres'
delimitador = '-'
print(s.split(delimitador))

t = ['el', 'sol', 'brilla', 'hoy']
delimitador = ' '
print(delimitador.join(t))

manejador = open('correo.txt')
for linea in manejador:
    linea = linea.rstrip()
    if not linea.startswith('From '):
        continue
    palabras = linea.split()
    print(palabras[2])

numlista = list()
while True:
    inp = input('Ingresa un numero: ')
    if inp == 'fin':
        break
    valor = float(inp)
    numlista.append(valor)

promedio = sum(numlista) / len(numlista)
print('Promedio:', promedio)