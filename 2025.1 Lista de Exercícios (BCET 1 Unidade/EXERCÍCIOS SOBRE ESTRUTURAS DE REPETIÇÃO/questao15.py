'''
Escreva um programa que monitore o crescimento de uma planta ao longo do tempo. O programa deve: (for)
Simular um crescimento de 0 cm a 150 cm, aumentando 5 cm por dia.
Simular a perda de altura devido ao estresse hídrico, diminuindo de 150 cm a 0 cm em decrementos de 7 cm.
Simular o crescimento de X cm a Y cm com um incremento de N cm (X, Y e N definidos pelo usuário).
Nota: Na última contagem, X, Y e n devem ser definidos fora da função range.

'''

# Simulação do crescimento da planta de 0 cm a 150 cm, aumentando 5 cm por dia
print("Crescimento da planta:")
for altura in range(0, 151, 5):
    print(f"Altura: {altura} cm")

# Simulação da perda de altura devido ao estresse hídrico, diminuindo 7 cm por dia
print("\nPerda de altura devido ao estresse hídrico:")
for altura in range(150, -1, -7):
    print(f"Altura: {altura} cm")

# Simulação do crescimento com valores definidos pelo usuário
X = int(input("Digite a altura inicial (X): "))
Y = int(input("Digite a altura final (Y): "))
N = int(input("Digite o incremento (N): "))

# Garantindo que o incremento funcione corretamente dentro do range
if N == 0:
    print("O incremento não pode ser 0.")
elif (X < Y and N > 0) or (X > Y and N < 0):
    print("\nCrescimento personalizado:")
    for altura in range(X, Y + (1 if X < Y else -1), N):
        print(f"Altura: {altura} cm")
else:
    print("Os valores inseridos não permitem um crescimento adequado.")