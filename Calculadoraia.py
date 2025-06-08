import tkinter as tk  # Importa a biblioteca para criar a interface gráfica

def calcular():
    try:
        expressao = entrada.get()  # Pega o texto da entrada
        resultado = str(eval(expressao))  # Calcula a expressão matemática (CUIDADO: eval pode ser perigoso se usado incorretamente)
        entrada.delete(0, tk.END)  # Limpa a entrada
        entrada.insert(tk.END, resultado)  # Mostra o resultado
    except Exception:
        entrada.delete(0, tk.END)  # Se der erro, limpa a entrada
        entrada.insert(tk.END, "Erro")  # Mostra "Erro"

def inserir_texto(texto):
    entrada.insert(tk.END, texto)  # Insere o texto no final da entrada

def limpar():
    entrada.delete(0, tk.END)  # Limpa toda a entrada

# Configuração da janela principal
janela = tk.Tk()  
janela.title("Calculadora Intuitiva")  # Título da janela
janela.geometry("300x400")  # Tamanho da janela (largura x altura)

# Campo de entrada (onde os números e operações aparecem)
entrada = tk.Entry(janela, font=('Arial', 18), justify='right', bd=10)
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew")  # Posiciona a entrada

# Lista de botões (texto, linha, coluna)
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)  # O botão "=" ocupa 4 colunas
]

# Cria os botões dinamicamente
for (texto, linha, coluna, *span) in botoes:
    if texto == '=':
        btn = tk.Button(janela, text=texto, command=calcular, bg='lightblue', font=('Arial', 14))
        btn.grid(row=linha, column=coluna, columnspan=span[0], sticky="nsew")
    elif texto == 'C':
        btn = tk.Button(janela, text=texto, command=limpar, bg='salmon', font=('Arial', 14))
        btn.grid(row=linha, column=coluna, sticky="nsew")
    else:
        btn = tk.Button(janela, text=texto, command=lambda t=texto: inserir_texto(t), font=('Arial', 14))
        btn.grid(row=linha, column=coluna, sticky="nsew")

# Configura o redimensionamento das linhas/colunas
for i in range(6):
    janela.grid_rowconfigure(i, weight=1)
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

janela.mainloop()  # Mantém a janela aberta