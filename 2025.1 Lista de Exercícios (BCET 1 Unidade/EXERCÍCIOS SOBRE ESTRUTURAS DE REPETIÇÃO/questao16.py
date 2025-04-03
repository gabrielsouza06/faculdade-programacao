'''
Escreva um programa que calcule o total e média de vendas semanais de uma loja. O programa deve solicitar ao usuário o valor das vendas de cada dia da semana (de segunda-feira a domingo) por meio de um for. (for)

'''

# Lista com os dias da semana
dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

# Inicializando a variável para armazenar o total de vendas
total_vendas = 0

# Loop para solicitar as vendas de cada dia
total_dias = len(dias_da_semana)
for dia in dias_da_semana:
    while True:
        try:
            venda = float(input(f"Digite o valor das vendas de {dia}: "))
            if venda < 0:
                print("O valor das vendas não pode ser negativo. Tente novamente.")
                continue
            total_vendas += venda
            break
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

# Cálculo da média semanal de vendas
media_vendas = total_vendas / total_dias

# Exibindo os resultados
print("\nResumo das vendas da semana:")
print(f"Total de vendas: R$ {total_vendas:.2f}")
print(f"Média diária de vendas: R$ {media_vendas:.2f}")