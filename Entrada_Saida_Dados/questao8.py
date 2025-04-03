# Escreva seu código aqui
''' RECEBA A QUANTIDADE DE AGUA EM CADA VASILHAS EM ML
    RECEBA A QUANTIDADE DE VASILHAS BEBIDAS EM 1 DIA
    CAULE A QUANTIDADE DE VASILHAS * A QUANTIDADE DE ALGUA EM CADA VISILHA
    '''
# Entrada de dados
vol_vasilha = float(input("Digite o volume médio de cada vasilha de água (em ml): "))
num_vasilhas = int(input("Digite o número de vasilhas de água consumidas ao longo do dia: "))

# Processamento
total_agua = vol_vasilha * num_vasilhas

# Saída
print(f"O total de água ingerida no dia é: {total_agua:.2f} ml")