def precio_min (p1:int,p2:int):
    menor_costo = ((p1+p2) - abs(p1-p2))//2
    return menor_costo
print(precio_min(2000,2100))