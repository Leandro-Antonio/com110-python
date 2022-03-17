"""Exercícios de apoio"""
# Pratique o conteúdo da semana fazendo os exercícios do livro Introdução a Computação Usando Python que seguem abaixo:
# Exercício 2.1
# Escreva expressões algébricas Python correspondentes aos seguintes comandos:
# (a) A soma dos 5 primeiros inteiros positivos.
a = 1 + 2 + 3 + 4 + 5
print(a)

# (b) A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
b = (23 + 19 + 31) / 3
print(b)

# (c) O número de vezes que 73 cabe em 403.
c = 403 // 73
print(c)

# (d) O resto de quando 403 é dividido por 73.
d = 403 % 73
print(d)

# (e) 2 à 10ª potência.
e = 2 ** 10
print(e)

# (f) O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
f = abs(54 - 57)
print(f)

# (g) O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
g = [34.99, 29.95, 31.50]
print(min(g))

# Exercício 2.2
# Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:
# (h) A soma de 2 e 2 é menor que 4.
h = 2 + 2 < 4
print(h)

# (i) O valor de 7 // 3 é igual a 1 + 1.
i = 7 // 3 == 1 + 1
print(i)

# (j) A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
j = (3 ** 2) + (4 ** 2) == 25
print(j)
# (k) A soma de 2, 4 e 6 é maior que 12.
k = (2 + 4 + 6) > 12
print(k)

# (L) 1387 é divisível por 19.
L = 1387 % 19 == 0
print(L)

# (m) 31 é par? (Dica: o que o resto lhe diz quando você divide por 2?)
m = 31 % 2 == 0
print(m)

# (N) O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.
N = min(34.99, 29.95, 31.50) < 30.00
print(N)

# Exercício 2.3
# Escreva instruções Python que correspondem às ações a seguir e execute-as:
# (o) Atribua o valor inteiro 3 à variável o.
o = int(3)
print(o)

# (p) Atribua 4 à variável p.
p = 4
print(p)

# (q) Atribua à variável q o valor da expressão o * o + p * p.
q = (o * o) + (p * p)
print(q)

# Exercício 2.4
# Comece executando as instruções de atribuição:
# >>> s1 = 'ant'
s1 = 'ant'
# >>> s2 = 'bat'
s2 = 'bat'
# >>> s3 = 'cod'
s3 = 'cod'
# Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:
# (r) 'ant bat cod'
r = s1 + ' ' + s2 + ' ' + s3
print(r)

# (s) ant ant ant ant ant ant ant ant ant ant'
s = 10 * (s1 + ' ')
print(s)
# (t) 'ant bat bat cod cod cod'
t = s1 + ' ' + 2 * (s2 + ' ') + 3 * (s3 + ' ')
print(t)
# (u) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
u = (s1 + ' ' + s2 + ' ') * 7
print(u)
# (v) 'batbatcod batbatcod batbatcod batbatcod batbatcod'
v = (s2 + s2 + s3 + ' ') * 5
print(v)
# Exercício 2.5
# Comece executando a atribuição:
# s = '0123456789'
s = '0123456789'
# Agora, escreva expressões usando a string s e o operador de indexação que é avaliado como:
# (x) '0'
print(s[0])
# (y) '1'
print(s[1])
# (w) '6'
print(s[6])
# (z) '8'
print(s[8])
# (a) '9'
print(s[9])
