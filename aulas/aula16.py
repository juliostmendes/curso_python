# Assunto: Condicionais if, elif, else

entrada = input('Você quer "entrar" ou "sair"? ')

# Só um dos blocos será executado
if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')