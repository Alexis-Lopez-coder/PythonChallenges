# Escribir una funcion que reciba como argumento un año y un mes
# Verificar si el mes de ese año tiene un viernes 13
import calendar

def viernes13(year, mes):
    dias = calendar.monthcalendar(year, mes)
    for i in dias:
        if i[4] == 13:
            return calendar.month_name[mes] + " del " + str(year) + " si tiene un viernes 13"
    return calendar.month_name[mes] + " del " + str(year) + " no tiene un viernes 13"

print(viernes13(2021, 8))