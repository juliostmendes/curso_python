# Assunto: função input
# Coleta dados dos usuários
# nome = input('Qual o seu nome?')  
# print(f'O seu nome é {nome}')

# input() recebe str
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

# Typecasting de str para int
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')