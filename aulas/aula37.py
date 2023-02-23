"""
Assunto: Continue
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1
    
    # Quando entra no continue ele volta pro while
    if contador == 6:
        print('6 ignorado')  
        continue  

    # Como temos o continue antes do print
    # não será printado os números entre 10 e 30
    if contador >= 10 and contador <= 30:
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')