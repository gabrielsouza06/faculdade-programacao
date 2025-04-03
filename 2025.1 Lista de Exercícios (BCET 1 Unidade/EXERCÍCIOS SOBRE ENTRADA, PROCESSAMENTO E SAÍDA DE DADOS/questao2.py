def main():
    """
    Calcula o novo salário de um funcionário após um reajuste percentual.
    O usuário informa o salário base e o percentual de aumento.
    """

    # Solicita o salário base e o percentual de aumento ao usuário
    salario_base = float(input("Informe o salário base do funcionário: "))
    percentual_aumento = float(input("Informe o percentual de aumento: "))

    # Calcula o novo salário após o reajuste
    novo_salario = salario_base + (salario_base * percentual_aumento / 100)

    # Exibe o novo salário
    print(f"O novo salário após o reajuste é: {novo_salario:.2f}")


if __name__ == "__main__":
    main()
