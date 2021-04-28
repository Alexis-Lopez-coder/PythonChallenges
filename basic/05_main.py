# Retornar la lista de numeros de el factorial de un numero

def factorial(num):
    if num == 1 or num == 0:
        return 1
    f = 1
    lista = [1]
    while num > 1:
        f *= num
        lista.append(f)
        num -= 1
    return lista

# Forma recursiva
def factorial2(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial2(num - 1)

print(factorial(5))
