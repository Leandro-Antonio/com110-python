"""Alguns exemplos de expressões aritméticas"""

a = 2**3  # expoente é representado por dois asteriscos
print(a)
b = 5//2  # divisão com duas barras (ou cociente) dispensa o resto da divisão
print(b)
c = 5/2  # divisão com uma barra exibe também as casas decimais
print(c)
d = 4 / (1 + 3)  # executa primeiro o que está dentro dos parenteses
print(d)
e = 4321 / 3 + 10  # operação de divisão vem antes da operação de soma
print(e)
f = 4321 / (2 + 10)  # operação dentro dos parenteses é executada e depois a divisão
print(f)
g = 3 + 2 * 2  # mesma regra da álgebra s multiplicação e divisão precedem a soma e subtração
print(g)
h = 2 - 3 + 1  # em operações de mesma precedência a operação ocorre da esquerda para a direita
print(h)
i = 2 * 3  # a saída da operação de dois números inteiros será outro número inteiro
print(type(i))
print(i)
j = 2 * 3.5
# o resultado da operação de um inteiro com um float será outro float mesmo que o resultado decimal seja zero
print(type(j))
print(j)
k = 4 / 2  # o resultado da divisão de dois inteiros será um float
print(type(k))
print(k)
L = 4 // 2  # a divisão de dois inteiros (cociente) com uso de duas barras retorna um inteiro
print(type(L))
print(L)
m = 5 % 2  # o resultado do módulo (resto) de uma divisão retorna um inteiro
print(type(m))
print(m)
n = abs(3 - 5)  # a função "abs()" retorna um número absoluto de uma operação (sem sinal negativo)
print(n)
o = (5, 12, 7, 2)
print(min(o))  # a função "min()" e "max()" retornam o valor mínimo "numeral ou alfabético" de listas ou tuplas
