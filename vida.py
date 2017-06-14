''' Classe Pessoa '''

class Pessoa:
    def __init__ (self, nome, peso, altura, idade = 0):
        self.nome = nome
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)

    def envelhecer (self):
        self.idade += 1
        if self.idade <= 21:
            self.altura += 0.5
            print('Altura: %.2f' %(self.altura))
        else:
           print('Altura: %.2f' %(self.altura)) 
    def engordar (self, kg):
        self.peso += kg
        print('Você engordou: %.2f, Seu Novo Peso é: %.2f' %(kg, self.peso))
    def emagrecer (self, kg):
        self.peso -= kg
        print('Novo Peso: %.2f' %self.peso)
    def crescer (self, cm):
        self.altura += cm
        print('Altura: %.2f' %(self.altura))
