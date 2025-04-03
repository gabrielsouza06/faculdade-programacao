'''
Escreva um programa que leia três números (X, Y e Z) e calcule as seguintes equações:
Divisão normal: X / Y
Divisão inteira: X // Y
Resto da divisão: X % Y
Exponenciação: X ** Y
Equação 1: X + Y * Z - X / Y ** Z
Equação 2: (X + Y) * Z - X / Y ** Z
Equação 3: X + Y * Z - (X / Y) ** Z
'''
def main():
    # Leitura dos valores
    X = float(input("Digite o valor de X: "))
    Y = float(input("Digite o valor de Y: "))
    Z = float(input("Digite o valor de Z: "))
    
    # Cálculos
    divisao_normal = X / Y
    divisao_inteira = X // Y
    resto_divisao = X % Y
    exponenciacao = X ** Y
    equacao_1 = X + Y * Z - X / Y ** Z
    equacao_2 = (X + Y) * Z - X / Y ** Z
    equacao_3 = X + Y * Z - (X / Y) ** Z
    
    # Exibição dos resultados
    print(f"Divisão normal: {divisao_normal}")
    print(f"Divisão inteira: {divisao_inteira}")
    print(f"Resto da divisão: {resto_divisao}")
    print(f"Exponenciação: {exponenciacao}")
    print(f"Equação 1: {equacao_1}")
    print(f"Equação 2: {equacao_2}")
    print(f"Equação 3: {equacao_3}")

if __name__ == "__main__":
    main()

