# Escreva seu código aqui
''' RECEBA O QUANTIDADE DE REFEIÇOES DIARIAS
    RECEBA QUANTIDADE DE REÇÃO GASTAS EM UM REFEIÇÃO
    CAUCULE A QUANTIDADE DE REÇÃO GASTA EM UM DIA
    RECEBA O VALOR DA REÇÃO GASTA EM UM DIA
    CAUCULE VALOR DIARIO  / QUANTIDADE DE REFEIÇOES
    RECEBA O VALOR MEDIO GASTO EM CADA REFEIÇÃO
    EXIBA O VALOR MEDIO GATO E CADA REFEIÇÃO '''

# Entrada de dados
num_refeicoes = int(input("Digite o número de refeições diárias do gato: "))
qtd_racao_dia = float(input("Digite a quantidade total de ração consumida por dia (em gramas): "))

# Processamento
media_racao = qtd_racao_dia / num_refeicoes

# Saída
print(f"A quantidade média de ração consumida por refeição é: {media_racao:.2f} gramas")