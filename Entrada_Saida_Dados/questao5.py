# Escreva seu código aqui
'''
    RECEBE A QUANTIDADE DE FRUTAS
    RECEBE A QUANTIDADE DE FRUTAS NECESARIAS PARA FORMAR O KG
    RECEBE O VALOR DE KG
    CAUCULO QUANTIDADE DE KG PRODUZIDOS * VALOR DE CADA KG
    SALVA VALOR DA COLHEITA DE FRUTAS
    EXIBE O VALOR DDA COLHEITA DE FRUTAS'''

# Entrada de dados
qtd_frutas = float(input("Digite a quantidade de frutas colhidas: "))
frutas_por_kg = float(input("Digite a quantidade de frutas por kg: "))
preco_kg = float(input("Digite o preço por kg: "))

# Processamento
qtd_kg = qtd_frutas / frutas_por_kg
valor_total = qtd_kg * preco_kg

# Saída
print(f"O valor total da colheita de frutas é: R$ {valor_total:.2f}")
