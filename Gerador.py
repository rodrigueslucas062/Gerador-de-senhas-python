import random

letra_maiuscula = chr(random.randint(65, 90))
letra_minuscula = chr(random.randint(90, 122))
char_especiais = chr(33)
lista_numeros = []

for i in range(8):
    numeros = random.randrange(9)
    lista_numeros.append(numeros)

random.shuffle(lista_numeros)
lista_numeros = str(lista_numeros) [1: -1]
lista_numeros = lista_numeros.replace
