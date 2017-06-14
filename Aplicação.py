''' Aplicação '''

from vida import Pessoa

nome = input('Digite seu nome: ')
peso =  float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
idade = int(input('Digite sua idade: '))


p1 = Pessoa(nome, peso, altura, idade)

print('Nome: %s Idade: %d' %(p1.nome, p1.idade))


p1.envelhecer()
p1.engordar(1.0)
p1.emagrecer(2.0)
p1.crescer(0.5)


