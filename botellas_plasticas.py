def calcular_pago_botellas(cant_pequenias:int, cant_grandes:int):
    pago_pequenias = 0.1*cant_pequenias
    pago_grandes = 0.25*cant_grandes
    return (round(pago_pequenias + pago_grandes, 2)) 
print(calcular_pago_botellas(200,1000))

