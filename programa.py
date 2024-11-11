import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# Dicionário para traduzir os dias da semana
DIAS_DA_SEMANA = {
    "Monday": "segunda-feira",
    "Tuesday": "terça-feira",
    "Wednesday": "quarta-feira",
    "Thursday": "quinta-feira",
    "Friday": "sexta-feira",
    "Saturday": "sábado",
    "Sunday": "domingo"
}

def aplicar_mascara_data(event):
    """Aplica máscara de data no formato DD/MM/AAAA enquanto o usuário digita."""
    texto = entry_data.get()
    texto = ''.join(filter(str.isdigit, texto))  # Remove todos os caracteres não numéricos

    # Adiciona a máscara de data conforme a quantidade de caracteres
    if len(texto) >= 3:
        texto = texto[:2] + '/' + texto[2:]
    if len(texto) >= 6:
        texto = texto[:5] + '/' + texto[5:]
    if len(texto) > 10:
        texto = texto[:10]

    # Atualiza o campo com o texto formatado
    entry_data.delete(0, tk.END)
    entry_data.insert(0, texto)

def traduzir_dia_semana(dia_semana_en):
    """Traduz o dia da semana de inglês para português."""
    return DIAS_DA_SEMANA.get(dia_semana_en, dia_semana_en)

def calcular_data_final(data_inicial, dias):
    """Calcula a data final e o dia da semana correspondente."""
    data_final = data_inicial + timedelta(days=dias - 1)
    dia_semana_en = data_final.strftime("%A")
    dia_semana_pt = traduzir_dia_semana(dia_semana_en)
    return data_final, dia_semana_pt

def calcular_proximo_dia_util(data):
    """Calcula o próximo dia útil após a data final."""
    proximo_dia_util = data
    while proximo_dia_util.weekday() >= 5:  # 5 = Sábado, 6 = Domingo
        proximo_dia_util += timedelta(days=1)
    dia_semana_en = proximo_dia_util.strftime("%A")
    dia_semana_pt = traduzir_dia_semana(dia_semana_en)
    return proximo_dia_util, dia_semana_pt

def calcular_data():
    """Função principal para calcular a data final e o próximo dia útil."""
    try:
        data_inicial = datetime.strptime(entry_data.get(), "%d/%m/%Y")
        dias = int(entry_dias.get())
        
        # Calcula a data final e o dia da semana
        data_final, dia_semana_final = calcular_data_final(data_inicial, dias)
        
        # Calcula o próximo dia útil
        proximo_dia_util, dia_semana_util = calcular_proximo_dia_util(data_final)
        
        # Exibe o resultado
        label_resultado.config(
            text=(
                f"Data final: {data_final.strftime('%d/%m/%Y')} ({dia_semana_final})\n"
                f"Próximo dia útil: {proximo_dia_util.strftime('%d/%m/%Y')} ({dia_semana_util})\n"
                f"Considerando começar em {entry_data.get()}"
            )
        )
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira uma data válida no formato DD/MM/AAAA e um número de dias.")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Data")
root.geometry("350x350")
root.resizable(False, False)

# Widgets de entrada e botão
tk.Label(root, text="Data inicial (DD/MM/AAAA):", font=("Arial", 12)).pack(pady=10)
entry_data = tk.Entry(root, font=("Arial", 12), width=15)
entry_data.pack(pady=5)
entry_data.bind("<KeyRelease>", aplicar_mascara_data)  # Ativa a máscara ao digitar
entry_data.focus_set()  # Define o foco no campo de data ao iniciar

tk.Label(root, text="Quantidade de dias:", font=("Arial", 12)).pack(pady=10)
entry_dias = tk.Entry(root, font=("Arial", 12), width=15)
entry_dias.pack(pady=5)

tk.Button(root, text="Calcular Data Final", font=("Arial", 12), command=calcular_data).pack(pady=20)

# Label para exibir o resultado
label_resultado = tk.Label(root, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

root.mainloop()