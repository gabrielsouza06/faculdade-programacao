'''Escreva um programa que leia a **largura de uma estrada** (metros) e a **quantidade de tráfego diário** (veículos/dia). Se a largura for menor que 7 metros (constante) ou o tráfego for maior que 20.000 veículos/dia (constante), classifique a estrada como 'Alto Risco de Acidentes'. Senão, classifique como 'Baixo Risco de Acidentes'. (`if...else`)

* Defina as constantes `LARGURA_MINIMA` e `TRAFEGO_MAXIMO`

LARGURA_MINIMA = 7
TRAFEGO_MAXIMO = 20000

'''

# Define as constantes LARGURA_MINIMA e TRAFEGO_MAXIMO
LARGURA_MINIMA = 7
TRAFEGO_MAXIMO = 20000

# Lê a largura da estrada e a quantidade de tráfego diário
largura_estrada = float(input("Informe a largura da estrada (metros): "))
trafego_diario = int(input("Informe a quantidade de tráfego diário (veículos/dia): "))

# Classifica a estrada como 'Alto Risco de Acidentes' ou 'Baixo Risco de Acidentes'
if largura_estrada < LARGURA_MINIMA or trafego_diario > TRAFEGO_MAXIMO:
    print("Classificação da estrada: Alto Risco de Acidentes")
else:
    print("Classificação da estrada: Baixo Risco de Acidentes")