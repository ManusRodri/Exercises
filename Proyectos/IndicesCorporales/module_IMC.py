def calcular_IMC(peso:float, altura:float):
    return round(peso/pow(altura,2),2)

def calcular_porcentaje_grasa(peso:float, altura:float, edad:int, valor_genero:float):
    IMC = calcular_IMC(peso,altura)
    return round(1.2 * IMC + .23*edad - 5.4 - valor_genero,2)

def calorias_en_reposo(peso:float, altura:float, edad:int, valor_genero:float):
    return round((10*peso) + (6.25*altura) - (5*edad) + valor_genero,2)

def calorias_en_actividad(peso:float, altura:float, edad:int, valor_genero:float, valor_actividad:float):
    TMB = calorias_en_reposo(peso, altura, edad, valor_genero)
    return round(TMB*valor_actividad,2)

def calorias_diarias_adelgazar(peso:float, altura:float, edad:int, valor_genero:float):
    TMB = calorias_en_reposo(peso, altura, edad, valor_genero)
    lim_sup = TMB*0.75
    lim_inf = TMB*0.8
    return "Para adelgazar es recomendado que consuma entre " + str(lim_inf) + " y " + str(lim_sup) + " de calorias al dia"