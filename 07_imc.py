# Calculadora de IMC
# Calcula o IMC a partir de peso e altura, classifica o resultado
# e trata entradas inválidas (peso ou altura menores ou iguais a zero)

peso = float(input('Informe o peso em kg: '))
altura = float(input('Informe a altura em m: '))

if peso <= 0 or altura <= 0:
    print('Valores inválidos. Peso e altura devem ser maiores que zero.')
else:
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print(f'Seu IMC é {imc:.2f}, classificação: Abaixo do peso')
    elif imc >= 18.5 and imc < 25:
        print(f'Seu IMC é {imc:.2f}, classificação: Peso normal')
    elif imc >= 25 and imc < 30:
        print(f'Seu IMC é {imc:.2f}, classificação: Sobrepeso')
    else:
        print(f'Seu IMC é {imc:.2f}, classificação: Obesidade')
