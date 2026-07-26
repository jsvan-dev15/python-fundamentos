# Biblioteca Matemática
# Conjunto de funções matemáticas reutilizáveis, acessadas através
# de um menu interativo.

def somar(a, b):
    soma = a + b
    return soma

def subtrair(a, b):
    diminuir = a - b
    return diminuir

def multiplicar(a, b):
    multiplicando = a * b
    return multiplicando

def dividir(a, b):
    dividindo = a / b
    return dividindo

def calcular_media(a, b):
    media = (a + b) / 2
    return media

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

while True:
    escolha = int(input("Escolha uma opção:\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n5 - Média\n6 - IMC\n7 - Tabuada\n8 - Sair\nDigite aqui: "))

    if escolha == 1:
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))
        resultado = somar(a, b)
        print(resultado)

    elif escolha == 2:
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))
        resultado = subtrair(a, b)
        print(resultado)

    elif escolha == 3:
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))
        resultado = multiplicar(a, b)
        print(resultado)

    elif escolha == 4:
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))
        resultado = dividir(a, b)
        print(resultado)

    elif escolha == 5:
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))
        resultado = calcular_media(a, b)
        print(resultado)

    elif escolha == 6:
        peso = float(input("Peso em kg: "))
        altura = float(input("Altura em m: "))
        resultado = calcular_imc(peso, altura)
        print(resultado)

    elif escolha == 7:
        numero = int(input("Informe um número: "))
        tabuada(numero)

    elif escolha == 8:
        print("Fechando programa...")
        break

    else:
        print("Número de operação inválido")
