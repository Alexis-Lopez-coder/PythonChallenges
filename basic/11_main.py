# Escribe un funcion que reciba dos numero, esa funcion devolvera el siguiente numero mayor a y b,
# pero que sea divisible entre b.

def funcion(a, b):
    if a > b:
        num = a + 1
    else:
        num = a + 1
    while num % b != 0:
        num += 1
    return num
print(funcion(22, 2))