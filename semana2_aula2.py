"""Expressões relacionais, operadores lógicos"""

# expressões relacionais retornam respostas do tipo lógico, também podem ser chamadas booleans.
a = 2 == 2  # expressão relacional "==" compara ou testa a igualdade entre dois elementos e retorna "TRUE" ou "FALSE".
b = 'Hello' == 'World'
print(a, b)
c = 2 * 3 != 6  # expressão relacional "!=" compara a desigualdade entre dois elementos e retorna "TRUE" ou "FALSE".
d = 'Hello' != 'World'
print(c, d)
e = 3 > 3  # As expressões relacionais "<" ou ">" testa se o primeiro elemento é maior ou menor,
# e retorna "TRUE" ou "FALSE".
f = 3 <= 3  # As expressões relacionais "<=" ou "=>" testam se o primeiro elemento é "maior ou igual",
# ou "menor ou igual" e retorna "TRUE" ou "FALSE".
print(e, f)
print(type(f))  # comparações lógicas e relacionais tem saída do tipo booleano.
g = 2 + 3 >= 3  # expressões aritméticas tem precedência e relação às expressões relacionais.
print(g)
h = 1 > 3 or 1 + 3 > 2  # expressão lógica "or" testa se uma ou todas as expressões são verdadeiras,
# e retorna "TRUE" ou "FALSE".
i = 1 > 3 and 1 + 3 > 2  # expressão lógica "and" testa se todas as expressões são verdadeiras,
# e retorna "TRUE" ou "FALSE".
j = not 1 > 3 and 1 + 3 > 2  # expressão lógica "not" inverte a resposta "TRUE' em "FALSE" e "FALSE" em "TRUE".
print(h, i, j)
k = 4 in [5, 6, 4, 1]  # expressão lógica "in" ou "not in" compara se um elemento pertence ou não a um conjunto.
L = 5 not in [1, 2, 3, 4, 5]
print(k, L)
m = 4 is not str  # Expressão lógica "is not" ou "is" compara se os elementos pertencem ao mesmo tipo,
# e retorna "TRUE" ou "FALSE"
n = 5.0 is int(5)
print(m, n)

# ordem de precedência dos operadores:
# Parênteses mais internos
# Operadores aritméticos
# Operadores relacionais
# Operadores lógicos

#  Precedência de operadores — Leitura de cima para baixo e da esquerda para direita.
# aritméticos:
#  "**"  — potência
#  "*", "/", "%", "//"  — multiplicação, divisão, módulo (resto da divisão), cociente da divisão (sem decimais)
#  "+", "-"  — soma e subtração

# relacionais:
# "<=", "<", ">", ">="  — menor ou igual a, menor que, maior que, maior ou igual a
# "==" "!="  — igual a, diferente de

# atribuição:
# "=", "%=", "/=", "-=", "+=", "*=", "**="

# operadores lógicos:
# "is", is not
# "in", "in not"
# "not", "or", "and"
