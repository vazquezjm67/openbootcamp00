#año bisiesto

def bisiesto(numero):
    if numero % 4 == 0 and (numero % 100 != 0 or numero % 400 == 0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")

bisiesto(1967)

