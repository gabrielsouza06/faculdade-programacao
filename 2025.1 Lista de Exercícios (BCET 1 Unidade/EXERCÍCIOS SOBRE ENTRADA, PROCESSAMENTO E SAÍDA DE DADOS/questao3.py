'''
Escreva um programa que leia o valor inicial investido, a taxa de juros mensal (%) e o número de meses. O programa deve calcular o montante final considerando juros compostos.
Considere :

P = Capital inicial
r = Taxa de juros (dividida por 100 para converter em decimal)
t = Tempo (em meses)
M = Montante final (saída)
'''
# Solicita o valor inicial investido, a taxa de juros mensal e o número de meses ao usuário
valor_inicial = float(input("Informe o valor inicial investido: "))
taxa_juros_mensal = float(input("Informe a taxa de juros mensal (%): "))
numero_meses = int(input("Informe o número de meses: "))

# Calcula o montante final considerando juros compostos
montante_final = valor_inicial * (1 + taxa_juros_mensal / 100) ** numero_meses

# Exibe o montante final
print("O montante final é:", montante_final)