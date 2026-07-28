# Calculadora de IMC (com tratamento de erros)
# Peso e altura informados pelo usuário
# Calcula o IMC e classifica, com tratamento de entradas inválidas
# e mensagens de erro personalizadas via raise

while True:
    try:
        peso = float(input('Informe o peso em kg: '))
        altura = float(input('Informe a altura em m: '))
        if peso <= 0 or altura <= 0:
            raise ValueError("Não pode números negativos")
        break
    except ValueError as erro:
        print(erro)

imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}, classificação: Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é {imc:.2f}, classificação: Peso normal')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é {imc:.2f}, classificação: Sobrepeso')
else:
    print(f'Seu IMC é {imc:.2f}, classificação: Obesidade')
