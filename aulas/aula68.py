"""
Assunto: Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 1  # Está no escopo módulo


def escopo():
    # global x  # Eu puxo a variável global para dentro da função
    x = 10  # Está no escopo local e é diferente do outro x

    def outra_funcao():
        # global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)