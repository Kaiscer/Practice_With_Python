'''
Genera y muestra los números del 1 al 100 y calcula la suma de todos los números pares, por un
lado, y la suma de los números impares, por otro. Muestra los resultados.
'''

numPar = []
numImpar = []

for i in range(1, 101):
    if i % 2 == 0:
        numPar.append(i)
    else:
        numImpar.append(i)


sumP = 0
for i in numPar:
    sumP = sumP + i

print(numPar)
print(f'La suma de los número parares es: {sumP}')

sumImp = 0
for i in numImpar:
    sumImp = sumImp + i

print(numImpar)
print(f'La suma de los números impares es: {sumImp}')
