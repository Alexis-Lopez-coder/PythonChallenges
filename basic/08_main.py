# Programa que retorne "Biz" si un numero dado es multiplo de 3, retorne "Buz" si el numero es multiplo de 5
# Retorne "BizBuz" si es multiplo de 3 y tambien de 5

def bizbuz(n):
    if n % 3 == 0 and n % 5 != 0:
        return "Biz"
    if n % 5 == 0 and n % 3 != 0:
        return "Buz"
    if n % 3 == 0 and n % 5 == 0:
        return "BizBuz"

print(bizbuz(9))