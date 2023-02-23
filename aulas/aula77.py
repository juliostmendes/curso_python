# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '2', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*3?',
        'Opções': ['12', '25', '15', '20'],
        'Resposta': '15',
    },
    {
        'Pergunta': 'Qual a capital de Cuba?',
        'Opções': ['Havana', 'Bogotá', 'Caracas', 'Brasília'],
        'Resposta': 'Havana',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou :)')
    else:
        print('Errou X')

    print()

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')