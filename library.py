
def sayHello(name,age="reservada tu edad"):
    print("Hola %s con que tienes %s" % (name, age))

def pintar_linea(longitud, datos={'punta': '*', 'extremo': '?', 'relleno': '+'}, isTop=False):
    line = datos['relleno']*(longitud-1)
    if isTop:
        line += datos['punta']
    else:
        line += datos['extremo']
    print(line)

def crear_piramide(altura, datos={'punta': '*', 'extremo': '?', 'relleno': '+'}):
    for i in range(1,altura+1):
        if i == (altura):
            pintar_linea(i, datos, True)
        else:
            pintar_linea(i, datos)

def crear_piramide_i(altura, datos={'punta': '*', 'extremo': '?', 'relleno': '+'}):
    for i in range(altura,0,-1):
        pintar_linea(i, datos)
def crear_piramidota(altura, datos={'punta': '*', 'extremo': '?', 'relleno': '+'}):
    crear_piramide(altura,datos)
    crear_piramide_i(altura-1,datos)
def crear_piramide_decorada(altura, datos={'punta': '*', 'extremo': '?', 'relleno': '+'}):
    crear_piramidota(altura,datos)
