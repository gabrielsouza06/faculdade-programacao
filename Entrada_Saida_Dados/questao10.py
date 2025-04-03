# Escreva seu código aqui
''' RECEBA O VALOR DO DIA 1 AU DIA 7
    AGRUPR O TEMPO TOTAL DE CAMINHADA REALIZADA EM 1 SEMANA
    CAUCULE A QUANTIDADEE DE CAMINHADA REALIZADA EM 1 SEMANA / 7
    RECEBA O VALOR DA MEDIA DE CAMINHADAS REALIZADAS
    EXIBA O VALOR DA MEDIA DE CAMINHAS  '''

# Entrada de dados
def calcular_media_caminhadas():
try:
    tempo_total = float(input("Digite o tempo total de caminhadas realizadas na semana (em minutos): "))
    if tempo_total < 0:
        raise ValueError("O tempo total de caminhadas não pode ser negativo.")

    # Processamento
    media_diaria = tempo_total / 7

    # Saída
    print(f"A média diária de tempo gasto em caminhadas é: {media_diaria:.2f} minutos")

except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")

calcular_media_caminhadas()