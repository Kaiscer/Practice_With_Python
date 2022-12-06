'''
• Escribe un programa en Python que cree una lista NO protegida llamada mares1 con 6 posiciones
(mediterráneo, cantábrico, báltico, adriático, tirreno, egeo).
• Crea otra lista llamada mares2 con 6 posiciones (rojo, muerto, caspio, negro, arábigo, sulu).
• Se creará también una lista nueva llamada mares que tenga 12 posiciones que serán las 6
• posiciones de mares1 más las 6 posiciones de mares2.
• El programa mostrará la siguiente información

'''

mares1 = ['mediterráneo', 'cantábrico', 'báltico', 'adriático', 'tirreno', 'egeo']

mares2 = ['rojo', 'muerto', 'caspio', 'negro', 'arábigo', 'sulu']

mares = []

for i in mares1:
    mares.append(i)

for i in mares2:
    mares.append(i)

print(mares)
# La longitud de la lista mares1

print(len(mares1))

# Los valores de todas las posiciones de la lista mares1

for i in mares1:
    print(i)

# La longitud de la lista mares2

print(len(mares2))

# Los valores de todas las posiciones de la lista mares2

for i in mares2:
    print(i)

# La longitud de la lista mares

print(len(mares))

# Los valores de todas las posiciones de mares

for i in mares:
    print(i)



# Los valores de las posiciones 1, 2 y 3 de mares1

for i in mares1[:3]:
    print(i)



# El índice o posición del mar ‘egeo’ en mares1

print(mares1.index('egeo'))



# Los valores de las posiciones 4, 5 y 6 de mares2

for i in mares2[3:6]:
    print(i)



# El índice o posición del mar caspio en mares2

print(mares2.index('caspio'))


# El índice o posición del mar caspio en mares

print(mares.index('caspio'))
