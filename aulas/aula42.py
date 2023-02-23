frase = 'O python é uma linguagem de programação '\
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

i = 0
qtd_letra_mais_comum = 0
letra_mais_comum = ''
while i < len(frase):
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_letra_mais_comum < qtd_atual:
        qtd_letra_mais_comum = qtd_atual
        letra_mais_comum = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_comum}" que apareceu '
    f'{qtd_letra_mais_comum}x'
)