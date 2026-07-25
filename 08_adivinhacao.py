# Jogo da Adivinhação
# O computador tem um número secreto fixo, e o usuário tenta adivinhar.
# Possui níveis de dificuldade que limitam o número de tentativas,
# e mostra o histórico de todos os palpites ao final.

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
    palpite = int(input("Digite um número: "))
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
