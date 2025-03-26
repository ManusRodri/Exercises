def calcular_IMC (peso:float, altura:float) -> float:
    IMC = peso / altura**2
    return float(IMC)

def calcular_porcentaje_grasa (peso:float, altura:float, edad:int, valor_genero:float)-> float:
    grasa_corporal = 1.2 * calcular_IMC(peso, altura) + 0.23 * edad - 5.4 - valor_genero
    return float(grasa_corporal)

def calcular_calorias_en_reposo (peso:float, altura:float, edad:int, valor_genero:float)-> float:
    TMB = (10*peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return TMB

def  calcular_calorias_en_actividad (peso:float, altura:float, edad:float, valor_genero:float, valor_actividad:float)-> float:
        TMB_actividad_fisica = calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * valor_actividad
        return TMB_actividad_fisica

def consumo_calorias_recomendado_para_adelgazar (peso:float, altura:float, edad:int, valor_genero:float)->str:
    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    lim_sup = TMB*0.75
    lim_inf = TMB*0.8
    return "Para adelgazar es recomendado que consuma entre " + str(lim_inf) + " y " + str(lim_sup) + " de calorias al dia"