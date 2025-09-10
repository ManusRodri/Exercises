def volumen(altura: float, ancho: float, largo: float) -> float:
    area_de_la_base = ancho*largo
    v = area_de_la_base * altura
    return (round(v, 2))
print (volumen(2, 3, 9.2))

def area_total(altura: float, ancho: float, largo: float) -> float:
    bl = largo*ancho
    hl = largo*altura
    hb = altura*ancho
    area = 2*(bl + hl + hb)
    return (round(area, 2))
print (area_total(2, 3, 9.2))
