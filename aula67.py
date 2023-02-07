"""
Assunto: Valores padrão para parâmetros
Ao definir uma função os parâmtros pode
ter valores padrão. Caso o valor padrão será
usado.
Refatorar: editar o seu código
"""


# def soma (x, z=None, y=None) Nesse caso
# Como z tem uma valor padrão (None), o que vem
# depois dele precisa também
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2)
soma(3, 5)
soma(7, 9, 0)