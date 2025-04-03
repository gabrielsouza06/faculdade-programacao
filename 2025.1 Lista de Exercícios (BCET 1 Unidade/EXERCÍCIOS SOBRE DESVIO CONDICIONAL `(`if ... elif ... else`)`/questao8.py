'''
Escreva um programa que leia a pressão de três tubulações industriais. Utilize ifs independentes para verificar se a pressão de cada tubulação está dentro da faixa segura (entre 30 e 100 PSI). Informe quais tubulações estão FORA da faixa segura. (if...)
'''

# Lê a pressão de três tubulações industriais
pressao_tubulacao_1 = float(input("Informe a pressão da tubulação 1 (PSI): "))
pressao_tubulacao_2 = float(input("Informe a pressão da tubulação 2 (PSI): "))
pressao_tubulacao_3 = float(input("Informe a pressão da tubulação 3 (PSI): "))

# Verifica se a pressão de cada tubulação está dentro da faixa segura
print("Tubulações fora da faixa segura:")
if pressao_tubulacao_1 < 30 or pressao_tubulacao_1 > 100:
    print("Tubulação 1")
if pressao_tubulacao_2 < 30 or pressao_tubulacao_2 > 100:
    print("Tubulação 2")
if pressao_tubulacao_3 < 30 or pressao_tubulacao_3 > 100:
    print("Tubulação 3")