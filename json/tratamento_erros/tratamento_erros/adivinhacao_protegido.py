# Jogo da Adivinhação (com tratamento de erros)
# O computador tem um número secreto fixo, e o usuário tenta adivinhar.
# Possui níveis de dificuldade, histórico de palpites, e agora também
# proteção contra entradas inválidas (texto no lugar de número).

contador = 0
historico = ""
numero_escolhido = 31

escolha = input('Qual dificuldade você escolhe? Fácil, Médio ou Difícil: ')

if escolha == "Fácil":
    limite_tentativas = 10
elif escolha == "Médio":
    limite_tentativas = 5
else:
    limite_tentativas = 3

while True:
    try:
        palpite = int(input("Digite um número: "))
    except ValueError:
        print("Valor inválido")
        continue

    contador += 1
    historico = historico + str(palpite) + " "
    if palpite == numero_escolhido:
        break
    else:
        print('Você errou, tente de novo.')
    if contador >= limite_tentativas:
        print('Você acabou com suas tentativas.')
        break

if palpite == numero_escolhido:
    print(f"Você acertou em {contador} tentativas! Histórico de palpites: {historico}")
else:
    print(f"Você perdeu! O número era {numero_escolhido}")
