"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


# Higher Order Function pois chama outra função
def executa(funcao, *args):
    return funcao(*args)


print(executa(saudacao, 'Bom dia', 'Luiz'))
print(executa(saudacao, 'Boa noite', 'Maria'))
