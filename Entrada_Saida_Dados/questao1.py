# Escreva seu código aqui
'''
LEIA QUANTIDADE DE HECTARES
RECEBA A QUANTIDADE DE LITROS DE ÁGUA
Calcular a quantidade de água utilizada por hectare dividindo a quantidade total de água pelo número de hectares.
Exibir o resultado da divisão.
Se a quantidade de hectares for zero, exibir uma mensagem de erro para evitar divisão por zero.'''

# Entrada de dados

hectares = float(input("Digite a quantidade de hectares: "))
agua_litros = float(input("Digite a quantidade de litros de água utilizada: "))

if hectares > 0:
# Processamento
    agua_por_hectare = agua_litros / hectares

# Saída
    print(f"A quantidade de água utilizada por hectare é: {agua_por_hectare:.2f} litros")
else:
    print("Erro: A quantidade de hectares deve ser maior que zero.")
