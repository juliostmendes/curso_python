
"""
Assunto: Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while condicao:  # Todo bloco será executado enquanto a condição ser verdadeira
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}\n')

    if nome == 'sair':
        break  # O break quebra o laço

print('Acabou')