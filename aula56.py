"""
Assunto: split, join e strip
split e join com lista e str
split - divide um string
join - une uma string
"""
frase = '   Olha só, essa frase não foi programada   '
lista_frases_cruas = frase.split(',')  # Divide de acordo com o caracter escolhido
lista_frase = []
for i, frase in enumerate(lista_frases_cruas):
    # strip, rstrip, lstrip
    lista_frase.append(lista_frases_cruas[i].strip())  # Corta espaços do começo e no fim da string

print(lista_frases_cruas)
print(lista_frase)
frases_unidas = '-'.join('abc')  # Une a lista com um caracter
print(frases_unidas)