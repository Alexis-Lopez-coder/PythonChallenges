# Escribir una funcion que reciba un numero que regrese su raiz cuadrada.
# El resultado solo debe de tener tres decimales

def raiz(num):
    return round(num ** (0.5), 3)
print(raiz(9))