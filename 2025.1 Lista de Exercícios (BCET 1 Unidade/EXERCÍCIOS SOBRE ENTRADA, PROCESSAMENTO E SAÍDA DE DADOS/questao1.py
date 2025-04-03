def main():
    """
    Simula a troca de saldo entre duas contas bancárias.
    O usuário informa os valores das contas A e B,
    e o programa inverte os saldos usando a técnica de swap.
    """

    # Solicita os valores das contas A e B ao usuário
    valor_conta_A = float(input("Informe o valor da conta A: "))
    valor_conta_B = float(input("Informe o valor da conta B: "))

    # Exibe os valores das variáveis A e B antes da troca
    print("\nValores antes da troca:")
    print(f"Conta A: {valor_conta_A:.2f}")
    print(f"Conta B: {valor_conta_B:.2f}")

    # Realiza a troca dos saldos usando a técnica de swap
    valor_conta_A, valor_conta_B = valor_conta_B, valor_conta_A

    # Exibe os valores das variáveis A e B depois da troca
    print("\nValores depois da troca:")
    print(f"Conta A: {valor_conta_A:.2f}")
    print(f"Conta B: {valor_conta_B:.2f}")


if __name__ == "__main__":
    main()