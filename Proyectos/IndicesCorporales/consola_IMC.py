import module_IMC as m
def menu():
    print(' 1. calculo IMC\n',
          '2. calculo porcentaje de grasa\n', 
          '3. calculo calorias en reposo\n',
          '4. calculo calorias en actividad fisica\n',
          '5. caluclo calorias para adelgazar\n')
    eleccion = int(input('Elija la opcion que desea calcular: '))
    match eleccion:
        case 1:
            opcion1()
            menu()
        case 2:
            opcion2()
            menu()
        case 3:
            opcion3()
            menu()
        case 4:
            opcion4()
            menu()
        case 5:
            opcion5()
            menu()
        case _:
            print('Opcion no valida')
            menu()

def opcion1():
    peso = float(input('Ingrese su peso en Kg: '))
    altura = float(input('Ingrese su altura en metros: '))
    print('Su IMC es de ' + str(m.calcular_IMC(peso, altura)))

def opcion2():
    peso = float(input('Ingrese su peso en Kg: '))
    altura = float(input('Ingrese su altura en metros: '))
    edad = int(input('Ingrese su edad en años: '))
    genero = input('Ingrese M si es masculino o F para femenino: ')
    if genero == 'M':
        genero = 10.8
    else:
        genero = 0
    print('Su porcentaje de grasa es de ' + str(m.calcular_porcentaje_grasa(peso, altura, edad, genero)))

def opcion3():
    peso = float(input('Ingrese su peso en Kg: '))
    altura = float(input('Ingrese su altura en centimetros: '))
    edad = int(input('Ingrese su edad en años: '))
    genero = input('Ingrese M si es masculino o F para femenino: ')
    if genero == 'M':
        genero = 5
    else:
        genero = -161
    print('Sus calorias en reposo son ' + str(m.calorias_en_reposo(peso, altura, edad, genero)))

def opcion4():
    peso = float(input('Ingrese su peso en Kg: '))
    altura = float(input('Ingrese su altura en centimetros: '))
    edad = int(input('Ingrese su edad en años: '))
    genero = input('Ingrese M si es masculino o F para femenino: ')
    if genero == 'M':
        genero = 5
    else:
        genero = -161
    actividad = input('Ingrese su actividad fisica: poco, ligero, moderado, deportista o atleta: ')
    match actividad:
        case 'poco':
            actividad = 1.2
        case 'ligero':
            actividad = 1.375
        case 'moderado':
            actividad = 1.55
        case 'deportista':
            actividad = 1.725
        case 'atleta':
            actividad = 1.9
        case _:
            print('opcion de actividad fisica no valida, por favor escriba todo en minuscula como se le indico antes')
            menu()
    print('Sus calorias en actividad son ' + str(m.calorias_en_actividad(peso, altura, edad, genero, actividad)))

def opcion5():
    peso = float(input('Ingrese su peso en Kg: '))
    altura = float(input('Ingrese su altura en centimetros: '))
    edad = int(input('Ingrese su edad en años: '))
    genero = input('Ingrese M si es masculino o F para femenino: ')
    if genero == 'M':
        genero = 5
    else:
        genero = -161
    print(m.calorias_diarias_adelgazar(peso, altura, edad, genero))

menu()