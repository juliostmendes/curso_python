"""
Lista de listas e seus índices
"""

# O mesmo princípio de matriz
# Pode ser aplicado em lista, tuplas, etc
salas = [
    [
        'Maria',
        'Helena',
    ],
    [
        'Elaine',
    ],
    [
        'Luiz',
        'João',
        'Eduarda',
    ],
]

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)