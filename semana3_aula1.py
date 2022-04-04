"""Semana 3 aula 1 - Listas tuplas e operadores"""

pets = ['cão', 'gato', 'peixe']
print(pets)
print(type(pets))
L = [1, 'ab', [], [1, 2]]
print(L)
print(type(L))
print(pets[1])
L = [1, 2, 3]
print(L)
L[2] = 4  # Listas são mutáveis
print(L)

# nome = 'Maria'
# print(nome)
# nome[0] = 'm'  # Erro, string é imutável
# print(nome)

# tuplas são semelhantes às listas, porém são imutáveis

# dias = ('seg', 'ter', 'qua')
# print(dias)
# dias[2] = 'qui'  # Erro, tuplas são imutáveis
# print(dias)

pets.append('cão')  # método ".append" adiciona ao final da lista o elemento especificado
print(pets)
print(pets.count('cão'))  # método ".count" conta quantos elementos especificados existem na lista

pets.insert(1, 'galinha')  # insere na lista, na posição especificada um determinado elemento
print(pets)

pets.pop()  # método ".pop" remove o último elemento da lista
print(pets)

pets.pop(1)  # o método ".pop" remove o elemento da posição especificada
print(pets)

pets.insert(1, 'galinha')
print(pets)

pets.remove('peixe')  # o método ".remove" remove o elemento especificado
print(pets)

pets.reverse()  # o método ".reverse" inverte a ordem da lista
print(pets)

pets.sort()  # o método ".sort" organiza a lista em ordem alfabética ou numérica
print(pets)
