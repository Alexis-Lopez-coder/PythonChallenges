# Funcion que retorne la longitud de un numero sin usar len()

def longitud(n):
    c = 0
    for i in str(n):
        c += 1
    return c

print(longitud(1000))