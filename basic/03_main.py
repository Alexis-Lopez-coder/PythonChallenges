# Escribir un programa que la funcion acepte dos enteros, los divida y regrese el resultado con dos decimales
# ademas del resto entre esos dos numeros
def quot_rem(num1, num2):
    return round(num1 / num2, 2), num1 - num2

print(quot_rem(179, 176))