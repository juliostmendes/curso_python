# Exercícios
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# Exercício 1

# numero = input('Digite um número inteiro: ')

# try:
#     numero_int = int(numero)
#     numero_par = (numero_int % 2) == 0
#     if numero_par:
#         print('O número digitado é par')
#     else:
#         print('O número digitado é impar')
    

# except:
#     print('É necessário digitar um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# Exercício 2

# horario = input('Que horas são? ')

# try:
#     horario_int = int(horario)
#     if horario_int >= 0 and horario_int < 12:
#         print('Bom dia :)')
#     elif horario_int >= 12 and horario_int <18:
#         print('Boa tarde :)')
#     elif horario_int >= 18 and horario_int < 24:
#         print('Boa noite :)')
#     else:
#         print('O horário precisa ser um valor entre 0 e 23')
# except:
#     print('É necessário digitar um horário válido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# Exercício 3

nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 0:
    if tamanho_nome <= 4:
        print('Seu nome é curto')

    elif tamanho_nome == 5 or tamanho_nome == 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')

else:
    print('Nome inválido')