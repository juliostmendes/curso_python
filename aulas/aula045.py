"""
For por baixo dos panos
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entrega o próximo valor
iter -> e entrega seu iterador
"""
# texto = 'Julio'.__iter__()
#texto = iter('Julio')  # __iter__()
# print(texto.__next__())
#print(next(texto))

# for letra in texto
texto = 'Julio'  # iterável
iteratador = iter(texto)  # iterador

# Funcionamento do for por baixo dos panos
while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break