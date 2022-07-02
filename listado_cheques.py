import csv, sys
from datetime import datetime

argumentos = sys.argv

def checkEstado(parametro):
    return parametro == "PENDIENTE" or parametro == "APROBADO" or parametro == "RECHAZADO"

if len(argumentos) >= 5:
    nombreArchivo, DNI, salida, tipoCheque = argumentos[1], argumentos[2], argumentos[3], argumentos[4]
    