# Assunto: Introdução ao desempacotamento

# resto vai ser uma list com os valores que sobraram
nome1, nome2, *_ = ['Maria', 'Helena', 'Julio', 'Carlos']
print(nome1)
print(nome2)
print(_)