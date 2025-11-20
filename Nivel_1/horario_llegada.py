def hora_llegada_vuelos (hora_salida:int,minuto_salida:int,segundo_salida:int,duracion_horas:int,duracion_minutos:int,duracion_segundos):
    hora_llegada1 = hora_salida + duracion_horas
    hora_llegada2 = minuto_salida + duracion_minutos
    hora_llegada3 = segundo_salida + duracion_segundos
    segundo_llegada1 = hora_llegada1*(60*60)
    segundo_llegada2 = hora_llegada2*60
    segundo_llegada3 = hora_llegada3
    segundo_llegada_final= segundo_llegada1 + segundo_llegada2 +segundo_llegada3
    hora_llegada_final = segundo_llegada_final // (60*60)
    minuto_llegada1 = ((segundo_llegada_final // 60) % 60) % 60
    minuto_llegada2 = segundo_salida + duracion_segundos
    segundo_llegada4 = minuto_llegada1*60
    segundo_llegada5 = minuto_llegada2
    segundo_llegada_final1= segundo_llegada4 + segundo_llegada5
    minuto_llegada_final1 = segundo_llegada_final1 // 60
    segundo_llegada6 = ((minuto_llegada_final1 // 60) % 60) % 60
    segundo_llegada7 = segundo_salida + duracion_segundos
    segundo_llegada_final2 = segundo_llegada7
    return "{0}:{1}:{2}".format(hora_llegada_final,minuto_llegada_final1,segundo_llegada_final2)
print (hora_llegada_vuelos(14,15,20,0,52,10))
