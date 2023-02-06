"""
Exercício
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
#
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
#
Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
# Verifica tamanho da entrada
while True:
    numero_digitado = input('Digite o seu CPF:')
    if len(numero_digitado) != 14:
        print('É necessário digitar o CPF com a pontuação correta')
        continue
    break

# Verifica formatação da entrada
try:
    numero_digitado = numero_digitado.split('-')
    primeiros_valores_cpf, digito_cpf = numero_digitado
except Exception:
    print(Exception)
    print('Houve erro na leitura do CPF')
    print('Sigo o seguinte formato: xxx.xxx.xxx-xx')

aux = 10
soma = 0
# Soma dos dígitos
try:
    for digito in primeiros_valores_cpf:
        if digito == '.':
            continue
        soma += int(digito) * aux
        aux -= 1
except Exception:
    print(Exception)
    print('Houve erro no calculo')

# Resultado final
soma = soma * 10
resultado = soma % 11
primeiro_digito = 0 if resultado > 9 else resultado
if primeiro_digito == int(digito_cpf[0]):
    print('O primeiro dígito do CPF está correto')
else:
    print('O primeiro dígito do CPF NÃO está correto')