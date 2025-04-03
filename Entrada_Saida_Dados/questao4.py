# Escreva seu código aqui
''' RECEBER NUMERO DE SACAS DE CAFÉ COLHIDOS
    RECEBE O VALOR INDIVIDUAL DE CADA SACA DE CAFÉ
    CAUCULA QUANTIDADE DE SACAS DE CAFÉ * VALOR DE CADA SACA DE CAFÉ
    RECEBE O VALOR DE DO CAUCULO
    EXIBE O VALOR DE CAUCULO '''

# Entrada de dados
num_sacas = int(input("Digite o número de sacas de café colhidas: "))
preco_saca = float(input("Digite o preço por saca de café: "))

# Processamento
valor_total = num_sacas * preco_saca

# Saída
print(f"O valor total da colheita é: R$ {valor_total:.2f}")