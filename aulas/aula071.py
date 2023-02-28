"""
Assunto: args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# Por convensão se utiliza *args, mas poderia ter qualquer nome
# Por padrão args é uma tupla


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

# Pode-se usar desempacotamento para a função sum
numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Se passarmos esse números direto não funcionará
# por isso utilizamos desempacotamento
print(sum(numeros))  # Soma de números
print(*numeros)