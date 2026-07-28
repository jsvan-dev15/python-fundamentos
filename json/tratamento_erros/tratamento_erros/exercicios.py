# Tratamento de Erros
# Exercícios de try/except: divisão protegida, conversor protegido
# e validador de idade com repetição até entrada válida.

# Exercício 1: Divisão protegida
try:
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    resultado = numero1 / numero2
    print(resultado)
except ZeroDivisionError:
    print("não pode ser divisível por 0")


# Exercício 2: Conversor protegido
try:
    numero1 = int(input("Digite um número: "))
    print(numero1)
except ValueError:
    print("número inválido")


# Exercício 3: Validador de idade
while True:
    try:
        idade = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Informe um valor válido")
