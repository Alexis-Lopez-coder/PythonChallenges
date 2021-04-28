# Funcion que retorne los primeros tres decimales de un numero.
# Si la parte decimal es cero, se retornara la palabra "ENTERO"

def numeros(num):
    a = int(num)
    b = abs(num) - abs(int(num))
    if b == 0:
        return a, "ENTERO"
    else:
        return a, round(b, 3)


print(numeros(15))