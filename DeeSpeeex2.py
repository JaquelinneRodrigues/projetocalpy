# Solicita ao usuário o primeiro número inteiro
numero1 = int(input("Digite o primeiro número inteiro: "))  
# input() captura o valor digitado e int() converte para número inteiro

# Solicita ao usuário o segundo número inteiro
numero2 = int(input("Digite o segundo número inteiro: "))

# Calcula a soma dos dois números
soma = numero1 + numero2

# Exibe o resultado formatado
print(f"A soma de {numero1} + {numero2} é igual a {soma}")
# f-string permite inserir variáveis diretamente no texto