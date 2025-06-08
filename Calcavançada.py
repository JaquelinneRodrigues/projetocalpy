import tkinter as tk
from tkinter import scrolledtext

# Variáveis globais
modo_escuro = True  # Começa no modo noturno
historico = []      # Armazena os cálculos

def calcular():
    try:
        expressao = entrada.get()
        resultado = str(eval(expressao))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, resultado)
        historico.append(f"{expressao} = {resultado}")  # Adiciona ao histórico
        atualizar_historico()
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def inserir_texto(texto):
    entrada.insert(tk.END, texto)

def limpar():
    entrada.delete(0, tk.END)

def atualizar_historico():
    historico_texto.delete(1.0, tk.END)  # Limpa o histórico atual
    for calculo in historico[-5:]:       # Mostra os últimos 5 cálculos
        historico_texto.insert(tk.END, calculo + "\n")

def alternar_tema():
    global modo_escuro
    modo_escuro = not modo_escuro  # Inverte o tema
    
    # Cores do modo DIURNO (claro)
    if not modo_escuro:
        janela.configure(bg='#F5F5F5')
        entrada.configure(bg='white', fg='black', insertbackground='black')
        for btn in botoes_widgets:
            if btn['text'] in ['/', '*', '-', '+']:
                btn.configure(bg='#FF9800', fg='white')  # Laranja
            elif btn['text'] == 'C':
                btn.configure(bg='#F44336', fg='white')  # Vermelho
            elif btn['text'] == '=':
                btn.configure(bg='#4CAF50', fg='white')  # Verde
            else:
                btn.configure(bg='#E0E0E0', fg='black')  # Cinza claro
        historico_texto.configure(bg='white', fg='black')
    # Cores do modo NOTURNO (escuro)
    else:
        janela.configure(bg='#2E2E2E')
        entrada.configure(bg='#424242', fg='white', insertbackground='white')
        for btn in botoes_widgets:
            if btn['text'] in ['/', '*', '-', '+']:
                btn.configure(bg='#FF5722', fg='white')  # Laranja
            elif btn['text'] == 'C':
                btn.configure(bg='#E53935', fg='white')  # Vermelho
            elif btn['text'] == '=':
                btn.configure(bg='#43A047', fg='white')  # Verde
            else:
                btn.configure(bg='#616161', fg='white')  # Cinza
        historico_texto.configure(bg='#424242', fg='white')

def tecla_pressionada(event):
    tecla = event.char
    if tecla.isdigit() or tecla in '+-*/.':
        inserir_texto(tecla)
    elif tecla == '\r':  # Enter
        calcular()
    elif tecla == '\x08':  # Backspace
        entrada.delete(len(entrada.get())-1, tk.END)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora Avançada")
janela.geometry("400x600")
janela.configure(bg='#2E2E2E')

# Campo de entrada
entrada = tk.Entry(
    janela,
    font=('Arial', 24),
    justify='right',
    bd=10,
    bg='#424242',
    fg='white',
    insertbackground='white'
)
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Frame para o histórico
frame_historico = tk.Frame(janela, bg='#424242')
frame_historico.grid(row=1, column=0, columnspan=4, sticky="nsew")

historico_texto = scrolledtext.ScrolledText(
    frame_historico,
    font=('Arial', 10),
    bg='#424242',
    fg='white',
    height=5,
    wrap=tk.WORD
)
historico_texto.pack(fill='both', expand=True)

# Lista de botões
botoes = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('C', 5, 2), ('+', 5, 3),
    ('=', 6, 0, 4),  # Botão "=" ocupa 4 colunas
    ('☀️', 6, 3)     # Botão para alternar tema
]

botoes_widgets = []  # Lista para armazenar os botões

# Criação dos botões
for (texto, linha, coluna, *span) in botoes:
    if texto == '=':
        btn = tk.Button(
            janela,
            text=texto,
            command=calcular,
            bg='#43A047',
            fg='white',
            font=('Arial', 16),
            bd=0
        )
        btn.grid(row=linha, column=coluna, columnspan=span[0], sticky="nsew")
    elif texto == '☀️':
        btn = tk.Button(
            janela,
            text=texto,
            command=alternar_tema,
            bg='#616161',
            fg='white',
            font=('Arial', 14),
            bd=0
        )
        btn.grid(row=linha, column=coluna, sticky="nsew")
    elif texto == 'C':
        btn = tk.Button(
            janela,
            text=texto,
            command=limpar,
            bg='#E53935',
            fg='white',
            font=('Arial', 14),
            bd=0
        )
        btn.grid(row=linha, column=coluna, sticky="nsew")
    else:
        btn = tk.Button(
            janela,
            text=texto,
            command=lambda t=texto: inserir_texto(t),
            bg='#616161',
            fg='white',
            font=('Arial', 14),
            bd=0
        )
        btn.grid(row=linha, column=coluna, sticky="nsew")
    botoes_widgets.append(btn)  # Adiciona o botão à lista

# Configuração do redimensionamento
for i in range(7):
    janela.grid_rowconfigure(i, weight=1)
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

# Vincula o teclado
janela.bind('<Key>', tecla_pressionada)

janela.mainloop()