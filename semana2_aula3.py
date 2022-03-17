"""Indexaçção de strings"""
s = 'abcd'
print(len(s))  # indexa quantos elementos tem na string
print(s[3])   # em pyton as posições começão a contagem a partir do zero
print(s[-2])  # indexa a partir da direita, número de posições especificadas usando o sinal de subtração
t = s[-1] == s[3]
print(t)
u = s[0:2]  # indexa a especificada até a posição final solicitada, mas não a inclui
# ex: posição inicia em zero e termina na posição dois, mas não está incluída
print(u)
v = s[-3:-1]  # começa em -3 e vai até -1, mas não o inclui
print(v)
x = s[:3]  # quando a posição inicial não é especificada, a indexação setá a partir da posição zero
print(x)
y = s[-2:]  # quando a posição final não é especificada, a indexação vai até o final da string
print(y)
