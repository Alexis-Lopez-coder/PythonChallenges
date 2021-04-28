# Funcion que verifica si el resultado de una division es entera
import random

def verifica(a, b):
    print(a,"/",b)
    return True if a/b - (abs(int(a/b))) == 0 else False

print(verifica(random.randint(1,20), random.randint(1,20)))