valor_compra = float(input("Digite o valor total da compra: "))
'''
 Dentro da variável valor_compra é solcitado com a função input para o usuário colocar um valor,
 sendo ela do tipo float
'''

#OBS> **Em cada laço de decisão foi descrito ao lado o seu tipo correspondente**

valor_antigo = valor_compra
# Esta variável guarda o valor inserido para usuário, o qual não foi sofrer modificações 
if valor_compra < 200: # Estrutura Condicional Encadeada
    # Aqui um inicia um laço de decisão que compara se o valor inserido pelo usuário é menor que 200
    valor_compra = valor_compra - (valor_compra*0.05)
    # Aqui é atualizado os dados da variável "Valor_compra" com a fórmula correspondente ao desconto aplicado
    desconto = 5
    # Esta váriavel guarda qual desconto foi aplicado
elif valor_compra >= 200: # Estrutura Condicional Encadeada e estrutura condicional aninhada
    '''
    Aqui continua o laço de decisão (se o if inicial é falso) que é verdadeiro, 
    quando o valor da compra é menor ou igual a 200, entrando no laço dentro deste
    '''
    if valor_compra < 300: # estrutura condicional aninhada
        # Nesse laço após chegar a primeira condição, e chegado se o valor da compara é menor que 300
        valor_compra = valor_compra - (valor_compra*0.10)
        # Aqui é atualizado os dados da variável "Valor_compra" com a fórmula correspondente ao desconto aplicado
        desconto = 10 
        # Esta váriavel guarda qual desconto foi aplicado
    else: # estrutura condicional aninhada
        # Caso todas as outras condições sejam falsas aplica a última situação exposta
        valor_compra = valor_compra - (valor_compra*0.15)
        # Aqui é atualizado os dados da variável "Valor_compra" com a fórmula correspondente ao desconto aplicado
        desconto = 15
        # Esta váriavel guarda qual desconto foi aplicado
print(f"O valor de {valor_antigo} sofreu um desconto de {desconto}%")
# Imprime os valor inserido pelo usuário e o desconto correspondente
print(f"O Total com desconto foi de: {valor_compra}")
# Imprime valor total da compra com o desconto aplicado

'''
OBS> No Elif poderia ser substituido de forma simplificada por:

elif valor_compra < 300:
    valor_compra = valor_compra - (valor_compra*0.10)
    desconto = 10 
else
    valor_compra = valor_compra - (valor_compra*0.15)
    desconto = 15

O elif valor_compra < 300 já garante automaticamente que o valor é >= 200, logo que falhou no primeiro if 
'''
