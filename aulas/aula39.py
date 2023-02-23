"""
Exercício
Assunto: Iterando string com while
"""
#         01234
# nome = 'Julio'  # Iteráveis
#      -  54321
nome = 'Julio Santos'
tamanho_nome = len(nome)
contador = 0
nova_string = ''  # nome com asteriscos

while contador < tamanho_nome:
    nova_string += f'*{nome[contador]}'  # itera com as letras do nome
    contador += 1
    
nova_string += '*'
print(nova_string)