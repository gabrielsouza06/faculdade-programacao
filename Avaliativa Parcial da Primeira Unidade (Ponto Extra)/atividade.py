# Importa bibliotecas necessárias
import tkinter as tk  # Interface gráfica
from tkinter import messagebox  # Caixas de mensagem (alertas)
import matplotlib.pyplot as plt  # Criação de gráficos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Integra matplotlib com Tkinter

# Define os valores de pedágio para cada tipo de veículo
valores = {
    "Moto": 0.00,
    "Carro": 5.40,
    "Ônibus": 12.90,
    "Caminhão": 21.70
}

# Inicializa dicionários para armazenar a quantidade de veículos e o valor arrecadado por tipo
quantidades = {tipo: 0 for tipo in valores}
arrecadacoes = {tipo: 0.0 for tipo in valores}

# Função que atualiza o painel lateral com informações gerais e chama a função para atualizar o gráfico
def atualizar_dashboard():
    total_veiculos = sum(quantidades.values())  # Soma total de veículos
    total_arrecadado = sum(arrecadacoes.values())  # Soma total de arrecadação
    tipo_mais_arrecadou = max(arrecadacoes, key=arrecadacoes.get)  # Tipo que mais arrecadou

    texto = ""
    for tipo in valores:
        texto += f"{tipo:<10}: {quantidades[tipo]:>3} veículos | R$ {arrecadacoes[tipo]:.2f}\n"

    texto += "\n"
    texto += f"Total veículos       : {total_veiculos}\n"
    texto += f"Total arrecadado     : R$ {total_arrecadado:.2f}\n"
    texto += f"💰 Mais arrecadou    : {tipo_mais_arrecadou}"

    painel_status.config(text=texto)  # Atualiza o texto do painel lateral
    atualizar_grafico()  # Atualiza o gráfico

# Função que registra um veículo, atualiza os valores e mostra mensagem de sucesso
def registrar(tipo):
    quantidades[tipo] += 1  # Incrementa a quantidade
    arrecadacoes[tipo] += valores[tipo]  # Soma o valor ao total arrecadado
    atualizar_dashboard()  # Atualiza os dados visuais
    messagebox.showinfo("Registro", f"{tipo} registrado com sucesso!")  # Alerta de confirmação

# Função que gera e exibe um relatório geral
def gerar_relatorio():
    total_veiculos = sum(quantidades.values())
    total_arrecadado = sum(arrecadacoes.values())
    
    # Calcula nova tarifa da Moto para aumentar arrecadação em 10%
    nova_taxa_moto = ((total_arrecadado * 1.10) - total_arrecadado) / max(quantidades["Moto"], 1)

    tipo_mais_arrecadou = max(arrecadacoes, key=arrecadacoes.get)
    tipo_maior_qtd = max(quantidades, key=quantidades.get)
    tipo_menor_qtd = min(quantidades, key=quantidades.get)

    # Monta o texto do relatório
    relatorio = "=== RELATÓRIO GERAL ===\n\n"

    for tipo in valores:
        relatorio += f"{tipo}:\n"
        relatorio += f" - Quantidade: {quantidades[tipo]}\n"
        relatorio += f" - Arrecadação: R$ {arrecadacoes[tipo]:.2f}\n\n"

    relatorio += f"Total de veículos: {total_veiculos}\n"
    relatorio += f"Total arrecadado: R$ {total_arrecadado:.2f}\n\n"
    relatorio += f"Tipo que mais arrecadou: {tipo_mais_arrecadou}\n"
    relatorio += f"Tipo com maior quantidade: {tipo_maior_qtd}\n"
    relatorio += f"Tipo com menor quantidade: {tipo_menor_qtd}\n\n"
    relatorio += f"Nova tarifa da Moto para +10% de arrecadação: R$ {nova_taxa_moto:.2f}"

    messagebox.showinfo("Relatório", relatorio)  # Exibe o relatório

# === GUI Principal ===
janela = tk.Tk()
janela.title("Sistema de Pedágio - BR 000")
janela.configure(bg="#f4f4f4")
janela.geometry("920x600")
janela.resizable(False, False)  # Impede redimensionamento da janela

# Título do sistema
tk.Label(janela, text="Sistema de Pedágio", font=("Segoe UI", 20, "bold"), bg="#f4f4f4").pack(pady=15)

# ==== Botões de Registro de veículos ====
frame_botoes = tk.Frame(janela, bg="#f4f4f4")
frame_botoes.pack(pady=10)

# Estilo visual dos botões
estilo_btn = {"width": 18, "height": 2, "font": ("Segoe UI", 10, "bold"), "bg": "#1976D2", "fg": "white"}

# Cria um botão para cada tipo de veículo
for tipo in valores:
    tk.Button(frame_botoes, text=f"Registrar {tipo}", command=lambda t=tipo: registrar(t), **estilo_btn).pack(side="left", padx=10)

# ==== Painel de Informações e Gráfico ====
frame_info = tk.Frame(janela, bg="#f4f4f4")
frame_info.pack(pady=10, padx=10, fill="both", expand=True)

# Painel lateral com status (quantidades e totais)
painel_status = tk.Label(frame_info, text="", font=("Courier New", 11), bg="white", fg="black",
                         justify="left", anchor="nw", relief="solid", width=40, height=20, padx=10, pady=10)
painel_status.pack(side="left", padx=10)

# Área do gráfico (barras horizontais)
figura, ax = plt.subplots(figsize=(4.5, 4))  # Tamanho do gráfico
canvas = FigureCanvasTkAgg(figura, master=frame_info)
canvas.get_tk_widget().pack(side="right", padx=10)

# Função que atualiza o gráfico de arrecadação
def atualizar_grafico():
    ax.clear()  # Limpa o gráfico anterior
    tipos = list(arrecadacoes.keys())
    valores_arrecadados = list(arrecadacoes.values())
    cores = ['gray', 'skyblue', 'orange', 'green']
    ax.bar(tipos, valores_arrecadados, color=cores)  # Cria gráfico de barras
    ax.set_title("Arrecadação por Veículo", fontsize=12)
    ax.set_ylabel("R$ Arrecadado")
    ax.set_ylim(0, max(valores_arrecadados + [1]) * 1.2)  # Define limite superior do eixo Y
    canvas.draw()  # Redesenha o gráfico na interface

# ==== Botões de Rodapé ====
frame_rodape = tk.Frame(janela, bg="#f4f4f4")
frame_rodape.pack(pady=10)

# Botão para gerar relatório
tk.Button(frame_rodape, text="Gerar Relatório", bg="#388E3C", fg="white", font=("Segoe UI", 10, "bold"),
          width=20, height=2, command=gerar_relatorio).pack(side="left", padx=10)

# Botão para sair do sistema
tk.Button(frame_rodape, text="Sair", bg="#D32F2F", fg="white", font=("Segoe UI", 10, "bold"),
          width=20, height=2, command=janela.destroy).pack(side="left", padx=10)

# Inicializa o painel e gráfico ao abrir o sistema
atualizar_dashboard()

# Executa a janela principal (loop da interface)
janela.mainloop()
