"""
Execício
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os
palavra_secreta = 'marisco'
letras_certas = ''
contador_tentativas = 0
while True:
    letra_atual = input('Digite uma letra: ').lower()
    contador_tentativas += 1

    if len(letra_atual) > 1:
        print('Digite apenas uma letra')
        continue
    
    if letra_atual in palavra_secreta:
        letras_certas += letra_atual
    
    palavra_temporaria = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            palavra_temporaria += letra_secreta
        else:
            palavra_temporaria += '*'

    print(f'Palavra atual: {palavra_temporaria}')

    # Verifica se string está completa
    if palavra_temporaria == palavra_secreta:
        os.system('clear')
        print('PARABENS VOCÊ GANHOU!!!')
        print('A palavra era', palavra_secreta)
        print(f'Tentativas totais:{contador_tentativas}')
        letras_certas = ''
        contador_tentativas = 0       