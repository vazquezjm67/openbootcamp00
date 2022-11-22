class Calculadora:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def suma(self):
        print(str(self.a+self.b))

    def resta(self):
        return self.a - self.b
    def multiplica(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b


ope1=Calculadora(4,2)
ope1.suma()
if __name__ == '__main__':
    print('estoy')













