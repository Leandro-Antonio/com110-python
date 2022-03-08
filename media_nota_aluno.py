"""Apresentar a média aritmética a parrtir de 4 notas
Aprovar o aluno caso nota seja maior ou igual a 5"""

N1 = float(input('Digite a primeira nota:'))
N2 = float(input('Digite a segunda nota:'))
N3 = float(input('Digite a terceira nota:'))
N4 = float(input('Digite a quarta nota'))

media = (N1+N2+N3+N4)/4

print('Reprovado' if media < 5  else 'Aprovado')
print (media)
