import tkinter as tk

def calcular():
    try:
        expressao = entrada.get()
        resultado = str(eval(expressao))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, resultado)
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def inserir_texto(texto):
    entrada.insert(tk.END, texto)

def limpar():
    entrada.delete(0, tk.END)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora Colorida")
janela.geometry("300x400")
janela.configure(bg='#2E2E2E')  # Cor de fundo da janela (cinza escuro)

# Campo de entrada
entrada = tk.Entry(
    janela,
    font=('Arial', 18),
    justify='right',
    bd=10,
    bg='#424242',  # Cor de fundo do campo
    fg='white',    # Cor do texto
    insertbackground='white'  # Cor do cursor
)
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Lista de botões (texto, linha, coluna, cor de fundo, cor do texto)
botoes = [
    ('7', 1, 0, '#616161', 'white'),
    ('8', 1, 1, '#616161', 'white'),
    ('9', 1, 2, '#616161', 'white'),
    ('/', 1, 3, '#FF5722', 'white'),  # Laranja
    ('4', 2, 0, '#616161', 'white'),
    ('5', 2, 1, '#616161', 'white'),
    ('6', 2, 2, '#616161', 'white'),
    ('*', 2, 3, '#FF5722', 'white'),
    ('1', 3, 0, '#616161', 'white'),
    ('2', 3, 1, '#616161', 'white'),
    ('3', 3, 2, '#616161', 'white'),
    ('-', 3, 3, '#FF5722', 'white'),
    ('0', 4, 0, '#616161', 'white'),
    ('.', 4, 1, '#616161', 'white'),
    ('C', 4, 2, '#E53935', 'white'),  # Vermelho
    ('+', 4, 3, '#FF5722', 'white'),
    ('=', 5, 0, '#43A047', 'white')   # Verde
]

# Cria os botões com cores personalizadas
for (texto, linha, coluna, *cores) in botoes:
    if texto == '=':
        btn = tk.Button(
            janela,
            text=texto,
            command=calcular,
            bg=cores[0],  # Cor de fundo
            fg=cores[1],  # Cor do texto
            font=('Arial', 14),
            bd=0  # Remove borda do botão
        )
        btn.grid(row=linha, column=coluna, columnspan=4, sticky="nsew")
    else:
        btn = tk.Button(
            janela,
            text=texto,
            command=lambda t=texto: inserir_texto(t),
            bg=cores[0],
            fg=cores[1],
            font=('Arial', 14),
            bd=0
        )
        btn.grid(row=linha, column=coluna, sticky="nsew")

# Configura o redimensionamento
for i in range(6):
    janela.grid_rowconfigure(i, weight=1)
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

janela.mainloop()