# Assunto: Formação com método format
a = 'A'
b = 'B'
c = 1.1
string = 'a={nome1} b={nome2} c={nome3:.2f}'
# .format pega os argumentos na ordem por padrão
# Mas se eu quiser posso pegar pelos índices
formato = string.format(
    nome1=a, nome2=b, nome3=c  # parametro nomeado
) 

print(formato)