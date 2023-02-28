# Assunto: Possíveis melhorias do código
# Utilizar .replace em caso de números com . e -
#
# cpf = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
import re
import sys

entrada = input('CPF [746.824.890-70]: ')
cpf = re.sub(  # Biblioteca re (regular expretion)
    r'[^0-9]', '', entrada)

# CPF com números iguais não devem ser válidos
entrada_e_sequencial = entrada == entrada[0] * len(entrada)
if entrada_e_sequencial:
    print('O CPF é sequencial')
    sys.exit()

nove_digitos = cpf[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0

for numero in nove_digitos:
    resultado_digito_1 += int(numero) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for numero in dez_digitos:
    resultado_digito_1 = int(numero) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == cpf_gerado:
    print(cpf, 'é válido')
else:
    print(cpf, 'inválido')