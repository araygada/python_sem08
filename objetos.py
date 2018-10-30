class Persona(object):
    # -------------------------------------------
    # ATRIBUTOS
    # -------------------------------------------

    nombre = ""
    apellido = ""
    edad = 0
    cedula = ""

    # -------------------------------------------
    # METODOS
    # -------------------------------------------
    """Esto es un metodo constructor en Python. Se llama cada vez que se va a crear un objeto. 
    La responsabilidad de un contructor en un objeto es realizar la iniciacion"""

    def __init__(self, nombre, apellido, cedula, edad = None):
        self.nombre  = nombre
        self.apellido = apellido
        self.edad = edad
        self.cedula = cedula
#        args[0]
#        if "profesion" in kwargs:
#            self.profesion = kwargs["profesion"]

    @property
    def full_name(self):
        return "{} {}".format(self.nombre, self.apellido)

persona = Persona(
    "Alberto",
    "Raygada",
    "17630723",
"""    None,
    12, "hola", ["h", "m"],
    profesion = "informatica"
"""
)

#print(persona.nombre)
#print(persona.__dir__)
#persona.__setattr__("atributo", 1234)
#print(persona.atributo)

#print(persona.full_name())
print(persona.full_name)
