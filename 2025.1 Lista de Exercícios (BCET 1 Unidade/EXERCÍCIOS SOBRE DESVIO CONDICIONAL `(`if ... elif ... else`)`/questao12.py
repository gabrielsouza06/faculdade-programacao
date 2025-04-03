'''
Escreva um programa que leia a idade de um motor (em anos) e seu histórico de falhas (nenhum, leve, moderado ou grave) para classificar o nível de risco como 'Baixo', 'Médio' ou 'Alto', seguindo as regras: (if...elif...else)
ALTO: Se o motor tiver mais de 15 anos ou o histórico de falhas for 'grave'.
BAIXO: Se o motor tiver menos de 5 anos e o histórico for 'nenhum'.
MÉDIO: Se o motor tiver entre 5 e 15 anos e o histórico não for grave, ou se o motor tiver menos de 5 anos e o histórico for 'leve' ou 'moderado'.
Questão: Existe alguma combinação não coberta? Seria possível utilizar o else para uma das condições?

'''

# Lê a idade do motor e seu histórico de falhas
idade_motor = int(input("Informe a idade do motor (em anos): "))
historico_falhas = input("Informe o histórico de falhas do motor (nenhum, leve, moderado, grave): ")

# Classifica o nível de risco do motor
if idade_motor > 15 or historico_falhas == "grave":
    print("Nível de risco do motor: Alto")
elif idade_motor < 5 and historico_falhas == "nenhum":
    print("Nível de risco do motor: Baixo")
elif 5 <= idade_motor <= 15 and historico_falhas != "grave" or idade_motor < 5 and historico_falhas in ("leve", "moderado"):
    print("Nível de risco do motor: Médio")

'''Questão: Existe alguma combinação não coberta? Seria possível utilizar o else para uma das condições?
Resposta: Todas as combinações de idade e histórico de falhas estão cobertas pelas condições do código.
Sim, seria possível utilizar o else para a última condição, pois ela abrange todas as demais possibilidades não cobertas pelas condições anteriores.
O código ficaria assim:

if idade_motor > 15 or historico_falhas == "grave":
    print("Nível de risco do motor: Alto")
elif idade_motor < 5 and historico_falhas == "nenhum":
    print("Nível de risco do motor: Baixo")
else:
    print("Nível de risco do motor: Médio")'''