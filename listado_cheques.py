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

        else:
            rangoFecha= argumentos[5].split(":")
            estado= argumentos[6]

else:
    print("ERROR. Cantidad incorrec")

archivo= open(nombreArchivo, 'r', encoding='latin1')
archivoCSV= csv.reader(archivo)

resultado=[]
nroCheque=[]
for linea in archivoCSV:
    if linea[-3] == DNI and linea[-2] == tipoCheque:
        if len(argumentos)==6:
            if checkEstado(argumentos[5]):
                if linea[-1] == estado:
                    resultado.append(linea)
                    if linea[0] in nroCheque:
                        raise Exception("Numero de cheque duplicado!")
                    else:
                        nroCheque.append(linea[0])
            else:
                if int(linea[-5]) >= datetime.timestamp(datetime.strptime(rangoFecha[0], "%d-%m-%Y")) and int(linea[-4]) <= datetime.timestamp(datetime.strptime(rangoFecha[1], "%d-%m-%Y")):
                    resultado.append(linea)
                    if linea[0] in nroCheque:
                        raise Exception("Numero de cheque duplicado!")
                    else:
                        nroCheque.append(linea[0])
        else:
            resultado.append(linea)
            if linea[0] in nroCheque:
                raise Exception("Numero de cheque duplicado!")
            else:
                nroCheque.append(linea[0])
        
        if len(argumentos) == 7:
            if linea[-1] == estado and (linea[-5] >= datetime.timestamp(datetime.strptime(rangoFecha[0], "%d-%m-%Y")) and int(linea[-4]) <= datetime.timestamp(datetime.strptime(rangoFecha[1], "%d-%m-%Y"))):
                resultado.append(linea)
                if linea[0] in nroCheque:
                    raise Exception("Numero de cheque duplicado!")
                else:
                    nroCheque.append(linea[0])

if salida == "PANTALLA":
    print(resultado)
    archivo.close()
else:
    dt = datetime.now()
    archivoSalida=open(f'{DNI}_{int(round(datetime.timestamp(dt)))}', 'w', newline='')
    archivoSalida.write("FechaOrigen,FechaPago,Valor,NroCuenta \n")
    
    guardado=[]
    fila=[]
    for i in range(len(resultado)):
        guardado.append(resultado[i][-5])
        guardado.append(resultado[i][-4])
        guardado.append(resultado[i][-6])
        guardado.append(resultado[i][3])
        fila.append(guardado)

        guardado=[]
    with archivoSalida:     
        write = csv.writer(archivoSalida)
        write.writerows(fila)
 
    archivoSalida.close()
    archivo.close()