import tkinter as tk
from tkinter import scrolledtext
import math  # Biblioteca para funções matemáticas

# Variáveis globais
modo_escuro = True
historico = []
modo_cientifico = False  # Controle do modo científico

def calcular():
    try:
        expressao = entrada.get()
        # Substitui símbolos científicos antes do eval
        expressao = expressao.replace('π', str(math.pi))
        expressao = expressao.replace('e', str(math.e))
        expressao = expressao.replace('^', '**')
        expressao = expressao.replace('√', 'math.sqrt')
        expressao = expressao.replace('sin', 'math.sin')
        expressao = expressao.replace('cos', 'math.cos')
        expressao = expressao.replace('tan', 'math.tan')
        expressao = expressao.replace('log', 'math.log10')
        expressao = expressao.replace('ln', 'math.log')
        
        resultado = str(eval(expressao))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, resultado)
        historico.append(f"{expressao} = {resultado}")
        atualizar_historico()
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def inserir_texto(texto):
    entrada.insert(tk.END, texto)

def limpar():
    entrada.delete(0, tk.END)

def atualizar_historico():
    historico_texto.delete(1.0, tk.END)
    for calculo in historico[-5:]:
        historico_texto.insert(tk.END, calculo + "\n")

def alternar_tema():
    global modo_escuro
    modo_escuro = not modo_escuro
    
    if not modo_escuro:  # Modo claro
        janela.configure(bg='#F5F5F5')
        entrada.configure(bg='white', fg='black', insertbackground='black')
        for btn in botoes_widgets:
            if btn['text'] in ['/', '*', '-', '+', '^', '√', 'sin', 'cos', 'tan', 'log', 'ln', 'π', 'e']:
                btn.configure(bg='#FF9800', fg='white')  # Laranja
            elif btn['text'] == 'C':
                btn.configure(bg='#F44336', fg='white')  # Vermelho
            elif btn['text'] == '=':
                btn.configure(bg='#4CAF50', fg='white')  # Verde
            elif btn['text'] == '☀️':
                btn.configure(bg='#616161', fg='white')
            elif btn['text'] == '🔬':
                btn.configure(bg='#2196F3', fg='white')  # Azul
            else:
                btn.configure(bg='#E0E0E0', fg='black')
        historico_texto.configure(bg='white', fg='black')
    else:  # Modo escuro
        janela.configure(bg='#2E2E2E')
        entrada.configure(bg='#424242', fg='white', insertbackground='white')
        for btn in botoes_widgets:
            if btn['text'] in ['/', '*', '-', '+', '^', '√', 'sin', 'cos', 'tan', 'log', 'ln', 'π', 'e']:
                btn.configure(bg='#FF5722', fg='white')  # Laranja
            elif btn['text'] == 'C':
                btn.configure(bg='#E53935', fg='white')  # Vermelho
            elif btn['text'] == '=':
                btn.configure(bg='#43A047', fg='white')  # Verde
            elif btn['text'] == '☀️':
                btn.configure(bg='#616161', fg='white')
            elif btn['text'] == '🔬':
                btn.configure(bg='#2196F3', fg='white')  # Azul
            else:
                btn.configure(bg='#616161', fg='white')
        historico_texto.configure(bg='#424242', fg='white')

def alternar_modo_cientifico():
    global modo_cientifico
    modo_cientifico = not modo_cientifico
    atualizar_botoes_cientificos()

def atualizar_botoes_cientificos():
    if modo_cientifico:
        # Mostra botões científicos
        btn_raiz.grid(row=2, column=4, sticky="nsew")
        btn_potencia.grid(row=3, column=4, sticky="nsew")
        btn_sin.grid(row=4, column=4, sticky="nsew")
        btn_cos.grid(row=5, column=4, sticky="nsew")
        btn_tan.grid(row=6, column=4, sticky="nsew")
        btn_log.grid(row=2, column=5, sticky="nsew")
        btn_ln.grid(row=3, column=5, sticky="nsew")
        btn_pi.grid(row=4, column=5, sticky="nsew")
        btn_e.grid(row=5, column=5, sticky="nsew")
    else:
        # Esconde botões científicos
        btn_raiz.grid_forget()
        btn_potencia.grid_forget()
        btn_sin.grid_forget()
        btn_cos.grid_forget()
        btn_tan.grid_forget()
        btn_log.grid_forget()
        btn_ln.grid_forget()
        btn_pi.grid_forget()
        btn_e.grid_forget()

def tecla_pressionada(event):
    tecla = event.char
    if tecla.isdigit() or tecla in '+-*/.^':
        inserir_texto(tecla)
    elif tecla == '\r':  # Enter
        calcular()
    elif tecla == '\x08':  # Backspace
        entrada.delete(len(entrada.get())-1, tk.END)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora Científica")
janela.geometry("600x600")
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
entrada.grid(row=0, column=0, columnspan=6, sticky="nsew")

# Frame para o histórico
frame_historico = tk.Frame(janela, bg='#424242')
frame_historico.grid(row=1, column=0, columnspan=6, sticky="nsew")

historico_texto = scrolledtext.ScrolledText(
    frame_historico,
    font=('Arial', 10),
    bg='#424242',
    fg='white',
    height=5,
    wrap=tk.WORD
)
historico_texto.pack(fill='both', expand=True)

# Lista de botões básicos
botoes_basicos = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('C', 5, 2), ('+', 5, 3),
    ('=', 6, 0, 3),  # Botão "=" ocupa 3 colunas
    ('☀️', 6, 3),    # Botão para alternar tema
    ('🔬', 6, 4, 2)  # Botão para alternar modo científico (ocupa 2 colunas)
]

botoes_widgets = []

# Criação dos botões básicos
for (texto, linha, coluna, *span) in botoes_basicos:
    if texto == '=':
        btn = tk.Button(
            janela,
            text=texto,
            command=calcular,
            bg='#43A047',
            fg='white',
            font=('Arial', 14),
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
    elif texto == '🔬':
        btn = tk.Button(
            janela,
            text=texto,
            command=alternar_modo_cientifico,
            bg='#2196F3',
            fg='white',
            font=('Arial', 14),
            bd=0
        )
        btn.grid(row=linha, column=coluna, columnspan=span[0], sticky="nsew")
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
    botoes_widgets.append(btn)

# Botões científicos (inicialmente ocultos)
btn_raiz = tk.Button(janela, text='√', command=lambda: inserir_texto('√('), bg='#FF5722', fg='white', font=('Arial', 14), bd=0)
btn_potencia = tk.Button(janela, text='^', command=lambda: inserir_texto('^'), bg='#FF5722', fg='white', font=('Arial', 14), bd=0)
btn_sin = tk.Button(janela, text='sin', command=lambda: inserir_texto('sin('), bg='#FF5722', fg='white', font=('Arial', 14), bd=0)
btn_cos = tk.Button(janela, text='cos', command=lambda: inserir_texto('cos('), bg='#FF5722', fg='white', font=('Arial', 14), bd=0)
btn_tan = tk.Button(janela, text='tan', command=lambda: inserir_texto('tan('), bg='#FF5722', fg='white', font=('Arial', 14), bd=0)
btn_log = tk.Button(janela, text='log', command=lambda: inserir_texto('log('), bg='#FF5722', fg='white', font=('Arial', 14), bd=0)
btn_ln = tk.Button(janela, text='ln', command=lambda: inserir_texto('ln('), bg='#FF5722', fg='white', font=('Arial', 14), bd=0)
btn_pi = tk.Button(janela, text='π', command=lambda: inserir_texto('π'), bg='#FF5722', fg='white', font=('Arial', 14), bd=0)
btn_e = tk.Button(janela, text='e', command=lambda: inserir_texto('e'), bg='#FF5722', fg='white', font=('Arial', 14), bd=0)

botoes_widgets.extend([btn_raiz, btn_potencia, btn_sin, btn_cos, btn_tan, btn_log, btn_ln, btn_pi, btn_e])

# Configuração do redimensionamento
for i in range(7):
    janela.grid_rowconfigure(i, weight=1)
for i in range(6):  # Agora temos 6 colunas (2 adicionais para funções científicas)
    janela.grid_columnconfigure(i, weight=1)

# Vincula o teclado
janela.bind('<Key>', tecla_pressionada)

janela.mainloop()