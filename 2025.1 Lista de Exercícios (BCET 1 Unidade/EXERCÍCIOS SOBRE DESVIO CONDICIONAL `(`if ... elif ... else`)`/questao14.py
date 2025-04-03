'''
Escreva um programa que leia a quantidade de cursos adquiridos e a categoria do curso (T - Tecnologia, B - Business, D - Design). (if aninhado)
Tecnologia: R$200

Até 3 cursos: desconto de 5%
Acima de 3 cursos: desconto de 10%
Business: R$300

Até 3 cursos: desconto de 4%

Acima de 3 cursos: desconto de 8%

Design: R$250

Acima de 3 cursos: desconto de 6%

'''

# Lê a quantidade de cursos adquiridos e a categoria do curso
quantidade_cursos = int(input("Informe a quantidade de cursos adquiridos: "))
categoria_curso = input("Informe a categoria do curso (T - Tecnologia, B - Business, D - Design): ")

# Calcula o preço com desconto
if categoria_curso == "T":
    preco = 200 * quantidade_cursos
    if quantidade_cursos <= 3:
        preco_desconto = preco - (preco * 0.05)
    else:
        preco_desconto = preco - (preco * 0.1)
    print("Preço com desconto:", preco_desconto)
elif categoria_curso == "B":
    preco = 300 * quantidade_cursos
    if quantidade_cursos <= 3:
        preco_desconto = preco - (preco * 0.04)
    else:
        preco_desconto = preco - (preco * 0.08)
    print("Preço com desconto:", preco_desconto)
elif categoria_curso == "D":
    preco = 250 * quantidade_cursos
    if quantidade_cursos > 3:
        preco_desconto = preco - (preco * 0.06)
    else:
        preco_desconto = preco
    print("Preço com desconto:", preco_desconto)