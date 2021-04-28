# Escribe una funcon que que acepte tres variables y regrese la suma de las tres
# variables. Si las variables son iguales, entoces regresar el doble de la suma de las tres variables

def suma(a, b, c):
    if a == b and a == c and b == c:
        return 2 * (a + b + c) 
    return a + b + c
print(suma(4,4,4))