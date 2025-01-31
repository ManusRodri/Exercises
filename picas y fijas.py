def picas_fijas (numero_secreto:int, intento:int) -> dict:
    lista_numero_secreto_separado = []
    lista_numero_secreto = str(numero_secreto)
    for i in range (len(lista_numero_secreto)):
        lista_numero_secreto_separado.append(lista_numero_secreto[i])

    lista_intento_separado = []
    lista_intento= str(intento)
    for i in range (len(lista_intento)):
        lista_intento_separado.append(lista_intento[i])

    picas = 0
    fijas = 0

    lista_numero_secreto1: int = lista_numero_secreto_separado [0:1]
    lista_numero_secreto2: int = lista_numero_secreto_separado [1:2]
    lista_numero_secreto3: int = lista_numero_secreto_separado [2:3]
    lista_numero_secreto4: int = lista_numero_secreto_separado [3:4]

    lista_intento1: int = lista_intento_separado [0:1]
    lista_intento2: int = lista_intento_separado [1:2]
    lista_intento3: int = lista_intento_separado [2:3]
    lista_intento4: int = lista_intento_separado [3:4]

    if lista_intento1 == lista_numero_secreto1:
        fijas += 1

    elif lista_intento1 == lista_numero_secreto2:
        picas += 1

    elif lista_intento1 == lista_numero_secreto3:
        picas += 1

    elif lista_intento1 == lista_numero_secreto4:
        picas += 1

    else:
       None


    if lista_intento2 == lista_numero_secreto1:
        picas += 1

    elif lista_intento2 == lista_numero_secreto2:
        fijas += 1

    elif lista_intento2 == lista_numero_secreto3:
        picas += 1

    elif lista_intento2 == lista_numero_secreto4:
        picas += 1

    else:
       None


    if lista_intento3 == lista_numero_secreto1:
        picas += 1

    elif lista_intento3 == lista_numero_secreto2:
        picas += 1

    elif lista_intento3 == lista_numero_secreto3:
        fijas += 1

    elif lista_intento3 == lista_numero_secreto4:
        picas += 1

    else:
       None


    if lista_intento4 == lista_numero_secreto1:
        picas += 1

    elif lista_intento4 == lista_numero_secreto2:
        picas += 1

    elif lista_intento4 == lista_numero_secreto3:
        picas += 1

    elif lista_intento4 == lista_numero_secreto4:
        fijas += 1

    else:
        None

    return {"Picas": picas, "Fijas": fijas}
    
    
print (picas_fijas(1263,1238),)
