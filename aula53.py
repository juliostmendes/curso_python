"""
enumerate - enumera iteráveis (índices)
"""
#[(0, 'Julio',), (1, 'Maria'), (2, 'Gustavo), (3, 'João')]
lista = ['Julio', 'Maria', 'Gustavo']
list.append('João')

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)

# Os valores são esgotadados
for item in lista_enumerada:
    print(item)

# Uma forma de escrever mais vezes é utilizar o enumerate assim:
for item in enumerate(lista):
    print(item)


for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# Os valores são desempacotados
# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')