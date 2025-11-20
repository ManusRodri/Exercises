def calcular_fuerza_gravedad (masa_1:float, masa_2:float, distancia:float):
    G = 6.67E-11
    fuerza_gravedad = (G * masa_1 * masa_2) / (distancia)**2
    return fuerza_gravedad

def calcular_constante_K (masa:float):
    G = 6.67E-11
    constante_K = (4 * (3.14)**2) / (G * masa)
    return constante_K

def calcular_periodo (masa:float, distancia_media:float):
    K = calcular_constante_K (masa)                             # esta es la forma para volver a llamar una funcion a una variable y se debe quitar el tipo que es el argumento
    periodo = (K * distancia_media**3)**(1/2)
    return round(periodo, 3)                                    # se pone ", 3" para redondearlo a 3 decimales

def calcular_distancia_media (masa:float, periodo:float):
    K = calcular_constante_K (masa)
    P = periodo                                                 # se pone solo periodo en vez de llamar a la funcion ya que la funcion tiene 2 argumentos y uno de esos es el que se trata de averiguar y ademas solo se pone periodo ya que ya esta predeterminado
    distancia_media = (P**2 / K)**(1/3)
    return distancia_media

def calcular_aceleracion (vf:float, vi:float, dt:float):
    aceleracion = (vf - vi) / dt
    return aceleracion

def calcular_magnitud_de_la_fuerza (masa:float, vf:float, vi:float, dt:float):
    A = calcular_aceleracion (vf, vi, dt)
    fuerza = masa * A
    return fuerza

def calcular_momento (masa:float, velocidad:float):
    momento = masa * velocidad
    return momento

def calcular_velocidad_colision (masa_1:float, masa_2:float, velocidad_1:float, velocidad_2:float):
    momento_1 = calcular_momento (masa_1, velocidad_1)
    momento_2 = calcular_momento (masa_2, velocidad_2)
    velocidad_colision = (momento_1 + momento_2) / (masa_1 + masa_2)
    return round(velocidad_colision,3)
