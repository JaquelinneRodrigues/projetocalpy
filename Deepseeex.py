# Função para exibir o menu
def mostrar_menu():
    print("\n" + "=" * 30)
    print("MENU PRINCIPAL".center(30))
    print("=" * 30)
    print("1. Opção 1 - Saudação")
    print("2. Opção 2 - Calculadora Simples")
    print("3. Opção 3 - Verificar Par/Ímpar")
    print("4. Sair")
    print("=" * 30)

# Função da Opção 1 - Saudação
def opcao1():
    print("\n" + "-" * 30)
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}! Bem-vindo ao programa!")
    print("-" * 30 + "\n")

# Função da Opção 2 - Calculadora Simples
def opcao2():
    print("\n" + "-" * 30)
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"\nResultados:")
    print(f"Soma: {num1 + num2}")
    print(f"Subtração: {num1 - num2}")
    print(f"Multiplicação: {num1 * num2}")
    print(f"Divisão: {num1 / num2 if num2 != 0 else 'Erro: Divisão por zero!'}")
    print("-" * 30 + "\n")

# Função da Opção 3 - Verificar Par/Ímpar
def opcao3():
    print("\n" + "-" * 30)
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print(f"{numero} é PAR!")
    else:
        print(f"{numero} é ÍMPAR!")
    print("-" * 30 + "\n")

# Programa Principal
while True:
    mostrar_menu()  # Mostra o menu
    escolha = input("Escolha uma opção (1-4): ")

    if escolha == "1":
        opcao1()  # Chama função da Opção 1
    elif escolha == "2":
        opcao2()  # Chama função da Opção 2
    elif escolha == "3":
        opcao3()  # Chama função da Opção 3
    elif escolha == "4":
        print("\nSaindo do programa... Até logo! 👋\n")
        break  # Encerra o loop e sai do programa
    else:
        print("\nOpção inválida! Tente novamente.\n")

    # Pergunta se deseja continuar (opcional)
    continuar = input("Pressione ENTER para voltar ao menu...")