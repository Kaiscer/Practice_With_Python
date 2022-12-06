'''
Escribe un programa en Python que pida al usuario dos números.
• Si la suma de ambos números es mayor que 100 se mostrará el resultado de la suma y el
mensaje: 'La suma supera la centena'.
De lo contrario se mostrará el resultado de la suma y el mensaje ‘el resultado de la suma no supera la centena’.
'''
dataOk = True
while dataOk:
    try:
        number1 = float(input("Introduce un número: "))
        number2 = float(input("Introduce otro número: "))
        dataOk = False
    except ValueError as error:
        print("Debes introducir un número")


sum = number1 + number2

if sum > 100:
    print("La suma supera la centena")
elif sum == 100:
    print("La suma es igual a la centena")
else:
    print("El resultado no supera la centena")

