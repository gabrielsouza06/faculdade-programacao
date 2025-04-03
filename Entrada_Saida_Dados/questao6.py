# Escreva seu código aqui
''' RECEBE O PESSO DE UM ANIMAL
    CAUCULE PESSO DO ANIMAL * 0.453592
    SAUVE O VALOR DO PESSO DO ANIMAL EM KG
    EXIBA O VALOR DO PESSO DO ANIMAL EM KG '''

# Entrada de dados
peso_libras = float(input("Digite o peso do animal em libras: "))

# Processamento
peso_kg = peso_libras * 0.453592

# Saída
print(f"O peso do animal em kg é: {peso_kg:.2f} kg")