# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# Valor da variável


def multiplicacao(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado


numeros = 1, 2, 3, 4, 5, 6, 7, 8
#print(multiplicacao(*numeros))

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar


def e_par(numero):
    if numero % 2 == 0:
        return 'É par'
    return 'É impar'


# print(e_par(10))
# print(e_par(15))
# print(e_par(798))