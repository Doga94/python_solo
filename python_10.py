#Desafío
'''
Crea una función que reciba una cadena de texto que contenga la hora en formato doce horas:
Horas:Minutos AM/PM

Desafío:
Retornar una cadena de texto con la hora en formato 24 horas:

Horas:Minutos
'''
import datetime

def hora_formatos():
    hora = input("Ingrese una hora en formato de 12h (Hora:minuto AM/PM): ")
    hora = datetime.datetime.strptime(hora, "%I:%M %p").time()
    return hora

hora = hora_formatos()
print("La hora en formato 12h es: ", hora.strftime("%I:%M %p"))
print("La hora en formato de 24h es: ", hora.strftime("%H:%M"))


