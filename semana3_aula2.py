"""Estudando módulo math"""
import fractions
import math  # importa o módulo math

print(math.sqrt(4))  # a função ".sqrt()" calcula a raiz quadrada do valor especificado
print(math.log(8, 2))  # a função ".log(m, n)" calcula o log de m na base n
print(math.ceil(5.6))  # a função ".ceil()" arredonda um float para cima
print(math.floor(5.6))  # a função ".floor()" arredonda um float para baixo
print(math.pi)  # a função ".pi" exibe parte da pseudo de constante pi. Não é uma constante verdadeira, pois pode
# receber uma nova atribuição o que não ocorre em constantes.
# math.pi = 2  # atribui o valor 2 ao nome pi do módulo math
# print(math.pi)
print(math.e)  # a função ".e" exibe parte do número de euler.

a = fractions.Fraction(1, 2)  # o módulo fraction é usado para representar e realizar operações com frações
b = fractions.Fraction(3, 4)
c = a + b
print(c)

print(fractions.Fraction(1, 2)**1075)  # a função ".Fraction" exibe números com mais casas decimais que o float
print(0.5**1075)  # o float arredonda para zero, porém o float é mais rápido que o fraction
