'''
Escreva um programa que exiba a contagem de um relógio digital, simulando as horas, minutos e segundos de 00:00:00 até 23:59:59. (for aninhado)

'''

# Simulação do relógio digital de 00:00:00 até 23:59:59
for hora in range(24):  # Loop para as horas (0 a 23)
    for minuto in range(60):  # Loop para os minutos (0 a 59)
        for segundo in range(60):  # Loop para os segundos (0 a 59)
            print(f"{hora:02}:{minuto:02}:{segundo:02}")  # Formatação com dois dígitos