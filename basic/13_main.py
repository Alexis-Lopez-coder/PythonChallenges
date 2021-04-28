# Calcular el factorial de un numero random
import random
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

n = random.randint(1, 10)
print("Factorial de "+str(n)+" es", factorial(n))