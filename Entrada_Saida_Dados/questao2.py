# Escreva seu código aqui
''' RECEBA O PREÇO DO PRODUDO
    RECEBA A PORCENTAGEM DO DESCONTO
    CAUCULAR O VALOR DO DESCONTO EM CIMA DO VAOR REAL
    RECEBER O VALOR DO DESCONTO
    EXIBIR O VALOR DO DESCONTO  '''

  # Entrada de dados
preco_produto = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desconto (em porcentagem): "))

# Processamento
valor_desconto = (preco_produto * desconto) / 100
preco_final = preco_produto - valor_desconto

# Saída
print(f"O valor do desconto é: R$ {valor_desconto:.2f}")
print(f"O preço final do produto é: R$ {preco_final:.2f}")