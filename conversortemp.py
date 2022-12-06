'''
Escribe un programa en Python que convierta la temperatura dada en grados Fahrenheit, si se
indica que son grados Celsius, o en grados Celsius, si se indica que son grados Fahrenheit.
'''


def requestOption():
    control = True

    while control:
        option = int(input("Ingresa la opción que deseas realizar: \n1- Convertir de grados Celsius a Fahrenheit "
                           "\n2- Convertir de grados Fahrenheit a Celsius \n0- Para salir \n"))
        match option:
            case 1:
                requestCelsius()
            case 2:
                requestFahrenheit()
            case 0:
                control = False
            case _:
                print("Valor incorrecto")


def requestFahrenheit():
    control = True
    while control:
        try:
            fah = float(input("Introduce los grados Fahrenheit \n"))
            control = False
        except ValueError as error:
            print("Valor incorrecto")

        celsius = (fah - 32) * 0.5556
        print(f'{fah}ºF es igual a {celsius}ºC')


def requestCelsius():
    control = True
    while control:
        try:
            celsius = float(input("Introduce los grados Celsius \n"))
            control = False
        except ValueError as error:
            print("Valor incorrecto")

        fahrenheit = (celsius * 1.8) + 31
        print(f'{celsius}ºC es igual a {fahrenheit}ºF')


requestOption()
