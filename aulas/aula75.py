# Exercícios
# Crie funções que duplicam, triplicam e quadriplicam
# o número recebido como parâmetro.


def criar_multiplicador(multiplicador):

    def multiplicar(numero):
        return numero * multiplicador

    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

numero = 2

print(duplicar(numero))
print(triplicar(numero))
print(quadriplicar(numero))