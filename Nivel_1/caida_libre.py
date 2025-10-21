import math 

def caida_libre(altura: float) -> float:

    vo = 0
    a = 9.8
    d = altura
    vf = float(math.sqrt(vo**2 + 2 * a * d))

    return (round(vf,2))

print (caida_libre(200),"m/s")


