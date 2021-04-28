# Funcion que calcule cuantos numeros hay en un string

def calculo (cadena):
    c = 0
    for i in cadena:
        try:
            if type(eval(i)) == int:
                c += 1
        except Exception:
            pass
        
    return c
print(calculo("adasdas8535468adad1313asd"))