#!/usr/bin/python


class Calculadora() :
    """docstring for la clase Calculadora
    Esto es una Calculadora"""
    def __init__(self, arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def suma(self):
        return self.arg1+ self.arg2

    def resta(self):
        return self.arg1-self.arg2

class CalculadoraPlus(Calculadora) : #CalculadoraPlus hereda de calculadora . Si no hay init busca el de su padre
    """docstring for la clase Calculadora
    Esto es una Calculadora"""
    def __init__(self, arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def multi(self):
        return self.arg1*self.arg2

    def div(self):
        return self.arg1/self.arg2

    def suma(self):
        return float (self.arg1) + float (self.arg2)

micalculadora = Calculadora(5,3)
print micalculadora.suma()
micalculadora.arg2 = 1
print micalculadora.resta()
micalc2 = CalculadoraPlus(4,3)
print micalc2.suma()  #va a ejecutar la suma de Calculadora porque CalculadoraPlus no tiene suma
print micalc2.multi()
