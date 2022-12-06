"""
Escribe un programa en Python que permita calcular el número que esconde.
El usuario debe averiguar qué número esconde el programa.
Se pide números al usuario y se le informará de si el número es más grande o es más pequeño que el número a averiguar.
Si lo acierta, se le informará con el mensaje correspondiente.
• Muestra cuántas veces ha introducido un número erróneo el usuario hasta dar con el número correcto.
Una vez descubierto, si lo ha acertado en el primer intento, se mostrará el mensaje
“¡Enhorabuena! Lo has acertado a la primera”, si el número de veces es mayor que 3, se mostrará el mensaje:
“Por fin lo has acertado. Ha debido ser muy complicado para ti”.
En otros casos, se mostrará el mensaje: “Buen Trabajo! Lo has acertado”.

"""
import random

print("**** Adivina el número Escondido ***")


def requestNumber():
    while True:
        try:
            print("Ingresa un número del 1 a 20 y te diré si es el escondido")
            num = int(input())
            if 0 < num <= 20:
                break
            else:
                print("El número debe estar entre el rango indicado")
        except ValueError as error:
            print("El Debes ingresar un número entero")

    hidden = random.sample(range(1, 20), 1)
    attempts = 1
    if num == hidden:
        print("¡Enhorabuena! Lo has acertado a la primera")
    else:
        while num != hidden:
            num = int(input("Intentalo de nuevo \n"))
            attempts += 1
            if num == hidden and attempts < 3:
                print(f"¡Enhorabuena! lo has acertado en el {attempts}º intento, el número escondido era el  {hidden}")
                break
            elif attempts == 3:
                print(f"Ha debido ser muy complicado para ti, el número escondido era el  {hidden}")
                break


requestNumber()
