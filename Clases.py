
class Silla(object):
#Initialize the propieties of an instance
    def __init__(self, no_patas=4, material='madera', tiene_coderas=False, color='Negro' ):
        self.no_patas = no_patas
        self.material = material
        self.tiene_coderas = tiene_coderas
        self.color = color

class Person(object):
    #Constructor
    def __init__(self, gender='male', nationality='Mexican'):
        self.name = "I need a name"
        self.lastname = "Waiting for a name"
        self.age = 0
        self.gender = gender
        self.nationality = nationality

class Automovil(object):
    #Constructor
    def __init__(self, Motor):
        self.marca
        self.modelo
        self.anio
        self.motor = Motor
    def arrancar(self):
        print("Listo para irnos")
    def acelerar(self):
        print("Aumento la velocidad")
    def frenar(self):
        print("Disminuyo la velocidad")

class Motor(object):
    #Constructor
    def __init__(self):
        self.potencia
        self.numeroSerie
        self.capacidad
    def encender(self):
        print("Marcha")
    def acelerar(self):
        print("More gas!!")
