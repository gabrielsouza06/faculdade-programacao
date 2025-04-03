'''
Escreva um programa que leia o tipo de solo (arenoso, argiloso, siltoso) e a disponibilidade de água (alta ou baixa) e indique o sistema de irrigação mais adequado.
Arenoso + Alta disponibilidade: Pivô central
Arenoso + Baixa disponibilidade: Gotejamento
Argiloso + Alta disponibilidade: Aspersão
Argiloso + Baixa disponibilidade: Microaspersão
Siltoso (qualquer disponibilidade): Irrigação por sulcos
Caso a combinação informada não seja reconhecida, informe que não é possível indicar um sistema de irrigação. (match case)

DICA: Se o tipo de solo for Siltoso, a recomendação será sempre a mesma, independentemente da disponibilidade de água (alta ou baixa). Para representar essa situação no código, utilize o operador _ (dessa forma: case "Siltoso", _ :) para indicar que qualquer valor é aceito nessa condição.
'''

# Solicita o tipo de solo e a disponibilidade de água ao usuário
tipo_solo = input("Informe o tipo de solo (arenoso, argiloso, siltoso): ")
disponibilidade_agua = input("Informe a disponibilidade de água (alta ou baixa): ")

# Indica o sistema de irrigação mais adequado usando match case
match tipo_solo, disponibilidade_agua:
    case "arenoso", "alta":
        print("Sistema de irrigação recomendado: Pivô central")
    case "arenoso", "baixa":
        print("Sistema de irrigação recomendado: Gotejamento")
    case "argiloso", "alta":
        print("Sistema de irrigação recomendado: Aspersão")
    case "argiloso", "baixa":
        print("Sistema de irrigação recomendado: Microaspersão")
    case "siltoso", _:
        print("Sistema de irrigação recomendado: Irrigação por sulcos")
    case _:
        print("Não é possível indicar um sistema de irrigação para a combinação informada.")