import csv, sys
from datetime import datetime

argumentos = sys.argv

def checkEstado(parametro):
    return parametro == "PENDIENTE" or parametro == "APROBADO" or parametro == "RECHAZADO"

if len(argumentos) >= 5:
    nombreArchivo, DNI, salida, tipoCheque = argumentos[1], argumentos[2], argumentos[3], argumentos[4]
    
    if len(argumentos) == 6:
        if checkEstado(argumentos[5]):
            estado = argumentos[5]
        else:
            rangoFecha= argumentos[5].split(":")

    if len(argumentos) == 7:
        if checkEstado(argumentos[5]):
            estado= argumentos[5]
            rangoFecha= argumentos[6].split(":")

