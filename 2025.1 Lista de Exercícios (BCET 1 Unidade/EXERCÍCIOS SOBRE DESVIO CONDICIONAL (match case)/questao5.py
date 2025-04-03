'''
Escreva um programa que, ao receber a grandeza a ser medida, sugira um sensor adequado. (match case)
Temperatura: Termopar
Pressão: Transdutor piezoelétrico
Vibração: Acelerômetro
Distância: Sensor ultrassônico
Caso a grandeza informada não seja identificada, informe que não é possível recomendar um sensor.
'''

# Solicita a grandeza a ser medida ao usuário
grandeza = input("Informe a grandeza a ser medida: ")

# Sugere um sensor adequado usando match case
match grandeza:
    case "Temperatura":
        print("Sensor recomendado: Termopar")
    case "Pressão":
        print("Sensor recomendado: Transdutor piezoelétrico")
    case "Vibração":
        print("Sensor recomendado: Acelerômetro")
    case "Distância":
        print("Sensor recomendado: Sensor ultrassônico")
    case _:
        print("Não é possível recomendar um sensor para a grandeza informada.")