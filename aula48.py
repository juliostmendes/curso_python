"""
Assunto: Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item no final 
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   
lista = [10, 20, 30, 40]
lista.append('Julio')
nome = lista.pop()
lista.append(123)
del lista[-1]
# lista.clear()  # Limpa lista
lista.insert(0, 5)  # Adiciona 5 no índice 0
print('Lista', lista)

#######
lista_a = [1,2,3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print('Lista D', lista_d)
# lista[2] = 300
# del lista[2]  # Deleta selecionado e atualiza indices
# print(lista)
# print(lista[2])