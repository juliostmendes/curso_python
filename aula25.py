# Assunto: Interpolação básica de strings
"""
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
# x = hex minusculo, X = hex maiusculo
print('O hexadecimal de %d é %08X' % (1500, 1500))  # o 08x serve para formatar para 8 algoritmos