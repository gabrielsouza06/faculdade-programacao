'''
Escreva um programa que simule uma máquina de venda de café. O preço do café é uma constante (R$ 7). A máquina só aceita moedas de R$1 e notas de R$2. O programa deve solicitar pagamentos ao usuário até que o valor do café seja atingido ou ultrapassado. Ao final, exiba o troco, se houver. (while)

'''

# Definição do preço do café
PRECO_CAFE = 7

# Inicializando o valor pago
valor_pago = 0

print("Máquina de Café - Preço: R$ 7,00")
print("Aceita apenas moedas de R$ 1 e notas de R$ 2.\n")

# Loop para receber pagamentos até atingir ou ultrapassar o preço do café
while valor_pago < PRECO_CAFE:
    try:
        pagamento = int(input("Insira uma moeda de R$1 ou uma nota de R$2: "))
        if pagamento not in [1, 2]:
            print("Apenas moedas de R$1 e notas de R$2 são aceitas.")
            continue
        valor_pago += pagamento
        print(f"Total inserido: R$ {valor_pago},00")
    except ValueError:
        print("Entrada inválida! Digite apenas 1 ou 2.")

# Cálculo do troco, se houver
troco = valor_pago - PRECO_CAFE
if troco > 0:
    print(f"Troco: R$ {troco},00")

print("Café servido! Aproveite seu café. ")