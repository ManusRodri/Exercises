def calcular_costo_queso_fresco (costo_leche: float, cantidad_leche: float, costos_adicionales: float) -> float:
    costo_queso_fresco = costo_leche * cantidad_leche + costos_adicionales
    return round(costo_queso_fresco,2)

def calcular_cantidad_queso (cantidad_leche:float) ->float:
    constante_densidad_leche = 1.03
    cantidad_queso = (cantidad_leche * constante_densidad_leche)/ 10
    return round(cantidad_queso,2)

def calcular_dias_maduracion (cantidad_leche:float, temperatura_almacenamiento:float, humedad_relativa:float) ->int:
    cantidad_queso = calcular_cantidad_queso(cantidad_leche)
    tiempo_base = 5
    constante_de_maduracion = 0.1
    dias_maduracion = tiempo_base + constante_de_maduracion * ((humedad_relativa*cantidad_queso)/temperatura_almacenamiento)
    return round(dias_maduracion)

def calcular_costo_queso_madurado (costo_leche:float, cantidad_leche:float, costos_adicionales:float, costo_almacenamiento:float, temperatura_almacenamiento:float, humedad_relativa:float) ->float:
    costo_queso_fresco = calcular_costo_queso_fresco(costo_leche, cantidad_leche, costos_adicionales)
    dias_maduracion = calcular_dias_maduracion(cantidad_leche, temperatura_almacenamiento, humedad_relativa)
    costo_queso_maduro = costo_queso_fresco + costo_almacenamiento * dias_maduracion
    return round(costo_queso_maduro,2)

def calcular_tamanio_porcion (angulo_corte:float) ->float:
    tamanio_porcion = angulo_corte / 360
    return round(tamanio_porcion,2)

def calcular_costo_porcion_madurado (costo_leche:float, cantidad_leche:float, costos_adicionales:float, costo_almacenamiento:float, temperatura_almacenamiento:float, humedad_relativa:float, angulo_corte:float) ->float:
    costo_queso_maduro = calcular_costo_queso_madurado(costo_leche, cantidad_leche, costos_adicionales, costo_almacenamiento, temperatura_almacenamiento, humedad_relativa)
    tamanio_porcion = calcular_tamanio_porcion(angulo_corte)
    costo_porcion_maduro = costo_queso_maduro * tamanio_porcion
    return round(costo_porcion_maduro,2)
