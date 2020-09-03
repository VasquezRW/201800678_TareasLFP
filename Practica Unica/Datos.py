class Persona:

    def __init__(self):
        self.nombre = None
        self.edad = None
        self.activo = None
        self.promedio = None

    # Setters de la persona

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setActivo(self, activo):
        self.activo = activo

    def setPromedio(self, promedio):
        self.promedio = promedio

    # Setters de la persona

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getActivo(self):
        return self.activo

    def getPromedio(self):
        return self.promedio
