def calcular_iva_propina_total_factura(costo_factura:int):
    propina = costo_factura*0.1
    iva = costo_factura*0.19
    total= costo_factura + iva + propina
    return str(round(iva)) + ',' + str(round(propina)) + ',' + str(round(total))
print(calcular_iva_propina_total_factura(200000))