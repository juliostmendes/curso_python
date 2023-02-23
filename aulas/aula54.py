# Exercício
# Lista de compras
import os
lista_de_compras = []

while True:
    print('Selecione uma opção:')
    entrada = input('[i]nserir [a]pagar [l]istar: ').lower()
    
    if entrada == 'i':
        valor = input('Valor: ')
        lista_de_compras.append(valor)
        os.system('clear')
        continue

    elif entrada == 'a':
        item_str = input('Escolha o índice para apagar: ')
        
        try:
            item = int(item_str)
            del lista_de_compras[item]
        except:
            print('Indice inválido')

        continue
    elif entrada == 'l':
        os.system('clear')
        for i, valor in enumerate(lista_de_compras):
            print(i, valor)
        continue
    else:
        print('Digite uma entrada válida!')
        continue