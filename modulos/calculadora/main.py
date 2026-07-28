# Calculadora Modularizada
# Menu principal que importa e utiliza as funções do módulo operacoes.py

from operacoes import somar, subtrair, multiplicar, dividir, calcular_media, calcular_imc, tabuada

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
