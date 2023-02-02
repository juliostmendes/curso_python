"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']

# Gera um range com n indices = ao tamanho da lista
indices = range(len(lista))  

# Percorre o range()
for indice in indices:
    print(indice, lista[indice])