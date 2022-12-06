'''

Escribe un programa en Python que modifique la lista mares siguiendo el orden siguiente:

'''

mares1 = ['mediterráneo', 'cantábrico', 'báltico', 'adriático', 'tirreno', 'egeo']

mares2 = ['rojo', 'muerto', 'caspio', 'negro', 'arábigo', 'sulu']

mares = []

for i in mares1:
    mares.append(i)

for i in mares2:
    mares.append(i)

print(mares)

# Cambia a la vez los valores de los elementos undécimo y duodécimo de la lista mares por los valores
# 'del norte' y 'alborán'. Muestra la lista mares

mares[10] = 'del norte'
mares[11] = 'alboran'

print(mares)

# En la lista mares, inserta un elemento más con el valor 'báltico'. Muestra la lista mares

mares.append("báltico")
print(mares)

# Borra el quinto elemento de la lista mares. Muestra la lista mares

# mares.pop(4)

print(mares)

# Muestra la longitud de la lista mares
print(len(mares))

# Muestra los valores repetidos en la lista mares usando el método correspondiente

modifyList = set()
maresDuplicates = [x for x in mares if x in modifyList or modifyList.add(x)]
print(maresDuplicates)

# Elimina el tercer elemento de la lista mares y guárdalo en la variable mar1

mar1 = mares[2]
mares.pop(2)
print(mar1)
print(mares)

# Elimina el último elemento de la lista mares y guárdalo en la variable mar2

mar2 = len(mares) - 1
mares.pop(mar2)

print(mares)

#Guarda el valor del noveno elemento en la variable mar3

mar3 = mares[8]

print(mar3)

# Muestra los valores de las variables mar1, mar2 y mar3

print(f'Valor de mar1: {mar1} \nValor de mar2: {mar2} \nValor de mar3: {mar3}')

# Elimina el primer elemento de la lista mares con valor 'báltico'. Muestra la lista mares

for i in mares:
    delete = i

print(mares)
if delete == 'bálticos':
    print("Elemento eliminado")
else:
    print("El elemento no se encuentra en la lista")

# Elimina todos los elementos de la lista mares

mares.clear()
print(f'Elementos de la lista: {mares}')

# Ordena por orden alfabético de 'a' a 'z' los elementos de la lista mares1
mares1.sort()
print(mares1)

# Ordena por orden alfabético de 'z' a 'a' los elementos de la lista mares2

mares2.sort(key=None, reverse=True)
print(mares2)






