'''
Escreva um programa que leia a **velocidade de rotação (RPM)** de quatro motores industriais e informe qual a menor rotação indicada. Utilize apenas 2 variáveis para determinar o menor valor. (`if...`)

Dicas:
* Defina as variáveis “`menor_RPM`” e “`auxiliar`”
* A cada nova leitura da RPM, descarte a menor velocidade por meio de um if e reutilize a variável auxiliar.

se auxiliar < menor RPM, então
  menor RPM = auxiliar
'''
# Define as variáveis menor_RPM e auxiliar
menor_RPM = float('inf')  # Inicializa com infinito para garantir que a primeira leitura seja menor
auxiliar = 0

# Lê a velocidade de rotação de quatro motores industriais
for i in range(4):
    auxiliar = float(input(f"Informe a velocidade de rotação do motor {i + 1} (RPM): "))
    if auxiliar < menor_RPM:
        menor_RPM = auxiliar

# Exibe a menor rotação indicada
print("A menor rotação indicada é:", menor_RPM)