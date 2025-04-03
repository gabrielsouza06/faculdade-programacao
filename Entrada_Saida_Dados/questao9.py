# Escreva seu código aqui
''' RECEBA A DOSASEM DO MEDICAMENTO
    RECEBA O PESSO DO ANIVAL
    RECEBA A CONCENTRAÇÃO DO MEDICAMENTO
    CAUCULE  Quantidade Correta = (Peso * Dosagem) / Concentração
    RECEBA A QUANTIDADE CORRETA DO MEDICAMENTO
    EXIBA A QUANTIDADE CORRETA DO MEDICAMENTO'''

# Entrada de dados
dosagem = float(input("Digite a dosagem do medicamento: "))
peso_animal = float(input("Digite o peso do animal: "))
concentracao = float(input("Digite a concentração do medicamento: "))

# Processamento
qtd_correta = (peso_animal * dosagem) / concentracao

# Saída
print(f"A quantidade correta a ser administrada é: {qtd_correta:.2f}")