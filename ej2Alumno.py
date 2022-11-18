class Alumno:
    def __init__(self,nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def resultado(self):
        if self.nota >= 5:
            print(self.nombre+" aprobo con "+str(nota))
        else:
            print(self.nombre + " pringo con " + str(nota))



