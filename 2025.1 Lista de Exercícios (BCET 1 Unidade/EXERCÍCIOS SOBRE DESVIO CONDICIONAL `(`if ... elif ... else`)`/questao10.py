'''
Escreva um programa que leia a idade de um operador e o tipo de licença que ele possui. Se ele tiver mais de 21 anos e possuir uma licença do tipo 'Especial' ou 'Avançada', o programa deve indicar 'Autorizado a operar'. Senão, deve indicar 'Não autorizado'. (if...else)
Lembre-se da precedência dos operadores lógicos: (1) not (2) and (3) or

'''

# Lê a idade do operador e o tipo de licença
idade_operador = int(input("Informe a idade do operador: "))
tipo_licenca = input("Informe o tipo de licença (Especial, Avançada, outra): ")

# Verifica se o operador está autorizado a operar
if idade_operador > 21 and (tipo_licenca == "Especial" or tipo_licenca == "Avançada"):
    print("Autorizado a operar")
else:
    print("Não autorizado")