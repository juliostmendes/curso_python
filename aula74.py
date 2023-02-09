"""
Assunto: Closure e funções que retornam outras funções
"""

# Seria como criar uma função


def criar_saudacao(saudacao):

    def saudar(nome):
        return f'{saudacao}, {nome}!'

    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Bom Noite')

# Printo minha função s1 e s2
print(falar_bom_dia('Julio'))
print(falar_boa_noite('Julio'))