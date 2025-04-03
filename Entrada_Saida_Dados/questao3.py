# Escreva seu código aqui
''' RECEBE O VALOR DO COMPRIMENTO
    RECEBE O VALOR DA LARGURA
    RECEBE O VALOR DA ALTURA
    CAUCULO (COMPRIMENTO*LARGURA)*ALTURA
    SALVA O CAUCULO NA VARIAVEM VOLUME
    EXIBA A VARIAVEL VOLUME  '''

# Entrada de dados
comprimento = float(input("Digite o comprimento do terreno: "))
largura = float(input("Digite a largura do terreno: "))
altura = float(input("Digite a altura do terreno: "))

# Processamento
volume = (comprimento * largura) * altura

# Saída
print(f"O volume do terreno é: {volume:.2f} metros cúbicos")