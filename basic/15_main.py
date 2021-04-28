import random

def es_primo(num):
    print(num)
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return
    print("Es primo")
    return


es_primo(random.randint(2,20))