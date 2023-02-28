"""
Assunto: Introdução ao try/except
try: tenta executar o código
except: ocorre algum erro ao tentar executar
"""
numero_str = input('Vou dobrar o número que você digitar: ')
# Importante para tratamenro de erros
try:
    numero_float = float(numero_str)  
    print(f'O dobro de {numero_str} é {numero_float*2}')
# Toda vez que ocorrer um erro no try o código pula para o bloco except
except:
    print('Isso não é um número')