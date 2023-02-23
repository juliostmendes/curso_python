"""
Exercício
Calculadora com while
"""
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0
    
    # Verifica se houve a entrada de números
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    # Reinicia o while se ouver erro
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    operadores_permitidos = '+-/*' 
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    
    # Calcular
    if operador == '+':
        print(numero_1_float + numero_2_float)
    elif operador == '-':
        print(numero_1_float - numero_2_float)
    elif operador == '/':
        print(numero_1_float / numero_2_float)
    elif operador == '*':
        print(numero_1_float * numero_2_float)
    else:
        print('Houve algum erro')
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break