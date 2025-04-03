'''
Escreva um programa que leia o tipo de elevador (residencial, comercial ou industrial) e sua idade em anos. O programa deve indicar a frequência da inspeção obrigatória: (if aninhado)
Elevadores residenciais:

Até 10 anos: sem inspeção obrigatória.
De 11 a 20 anos: inspeção a cada 2 anos.
Mais de 20 anos: inspeção anual.
Elevadores comerciais:

Até 8 anos: sem inspeção obrigatória.
De 9 a 15 anos: inspeção a cada 2 anos.
Mais de 15 anos: inspeção anual.
Elevadores industriais:

Inspeção obrigatória anual, independente da idade.

'''

# Lê o tipo de elevador e sua idade
tipo_elevador = input("Informe o tipo de elevador (residencial, comercial, industrial): ")
idade_elevador = int(input("Informe a idade do elevador (em anos): "))

# Indica a frequência da inspeção obrigatória
if tipo_elevador == "residencial":
    if idade_elevador <= 10:
        print("Frequência da inspeção: Sem inspeção obrigatória")
    elif idade_elevador <= 20:
        print("Frequência da inspeção: Inspeção a cada 2 anos")
    else:
        print("Frequência da inspeção: Inspeção anual")
elif tipo_elevador == "comercial":
    if idade_elevador <= 8:
        print("Frequência da inspeção: Sem inspeção obrigatória")
    elif idade_elevador <= 15:
        print("Frequência da inspeção: Inspeção a cada 2 anos")
    else:
        print("Frequência da inspeção: Inspeção anual")
elif tipo_elevador == "industrial":
    print("Frequência da inspeção: Inspeção anual")