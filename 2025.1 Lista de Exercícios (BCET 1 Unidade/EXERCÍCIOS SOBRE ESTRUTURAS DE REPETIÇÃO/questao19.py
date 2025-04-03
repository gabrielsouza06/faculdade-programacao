'''
Escreva um programa que simule um jogo de adivinhação da temperatura de uma cidade misteriosa. O computador escolhe uma temperatura entre -10°C e 40°C, e o jogador tem até 8 tentativas (constante) para acertar. A cada erro, o programa informa se a temperatura real é mais quente ou mais fria do que o palpite. (while)
Para que o computador gere uma temperatura aleatóriq, utilize a função randint da biblioteca random:

'''

import random

# Gera a temperatura secreta entre -10°C e 40°C
temperatura_secreta = random.randint(-10, 40)

# Definição do número máximo de tentativas
MAX_TENTATIVAS = 8

tentativas = 0
print("Bem-vindo ao jogo de adivinhação da temperatura!\n")
print("Tente adivinhar a temperatura de uma cidade misteriosa entre -10°C e 40°C.")

# Loop para as tentativas
while tentativas < MAX_TENTATIVAS:
    try:
        palpite = int(input(f"Tentativa {tentativas + 1}/{MAX_TENTATIVAS} - Digite seu palpite: "))
        
        if palpite == temperatura_secreta:
            print("Parabéns! Você acertou a temperatura misteriosa! 🎉")
            break
        elif palpite < temperatura_secreta:
            print("A temperatura real é mais quente. 🔥")
        else:
            print("A temperatura real é mais fria. ❄️")
        
        tentativas += 1
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

# Se o jogador não acertar após todas as tentativas
if tentativas == MAX_TENTATIVAS and palpite != temperatura_secreta:
    print(f"Fim do jogo! A temperatura misteriosa era {temperatura_secreta}°C. ")