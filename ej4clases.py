class Vehiculo():
    def __init__(self, color, ruedas, puertas ):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas

    def __str__(self):
        return self.color + str(self.ruedas) + str(self.puertas)

class Coche(Vehiculo):
    def __init__(self, velocidad, cilindrada, color, ruedas, puertas):
        super().__init__(color, ruedas, puertas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def __str__(self):
        return super().__str__()+str(self.velocidad)+str( self.cilindrada)


micoche=Coche(10,2000,"rojo" ,4 ,5 )


print(micoche)









