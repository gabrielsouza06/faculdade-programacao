'''
Escreva um programa que leia a quantidade de produtos fabricados e o tempo total de operação de uma máquina (em horas). Em seguida, classifique a eficiência da máquina como: (if...elif...else)
Muito eficiente: Se produzir mais de 500 produtos por hora.
Eficiente: Se produzir entre 300 e 500 produtos por hora.
Moderada: Se produzir entre 150 e 300 produtos por hora.
Baixa: Se produzir entre 50 e 150 produtos por hora.
Muito baixa: Se produzir menos de 50 produtos por hora.
Considere como cálculo da produção por hora, a equação:

Produção por Hora = Quantidade de Produtos Fabricados * Tempo Total de Operação

'''

# Lê a quantidade de produtos fabricados e o tempo total de operação da máquina
quantidade_produtos = int(input("Informe a quantidade de produtos fabricados: "))
tempo_operacao = float(input("Informe o tempo total de operação da máquina (em horas): "))

# Calcula a produção por hora
producao_hora = quantidade_produtos / tempo_operacao

# Classifica a eficiência da máquina
if producao_hora > 500:
    print("Eficiência da máquina: Muito eficiente")
elif producao_hora >= 300:
    print("Eficiência da máquina: Eficiente")
elif producao_hora >= 150:
    print("Eficiência da máquina: Moderada")
elif producao_hora >= 50:
    print("Eficiência da máquina: Baixa")
else:
    print("Eficiência da máquina: Muito baixa")