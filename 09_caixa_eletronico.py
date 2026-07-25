# Caixa Eletrônico
# Simula operações bancárias básicas: depósito, saque, consulta de saldo
# e histórico de operações. Impede saques que deixariam o saldo negativo.

historico = ""
saldo = 0

while True:
    escolha = int(input("Escolha uma opção:\n1 - Depositar\n2 - Sacar\n3 - Consultar Saldo\n4 - Encerrar\n5 - Ver histórico\nDigite aqui: "))

    if escolha == 1:
        quantidade_deposito = float(input("Quanto deseja depositar? "))
        print(f"Depósito de {quantidade_deposito} foi realizado")
        saldo += quantidade_deposito
        historico = historico + f"Depósito de {quantidade_deposito}; "

    elif escolha == 2:
        quantidade_saque = float(input(f"Quanto deseja sacar? Seu saldo atual é {saldo}: "))
        if quantidade_saque > saldo:
            print("Saldo insuficiente")
        else:
            print(f"Saque de {quantidade_saque} realizado")
            saldo -= quantidade_saque
            historico = historico + f"Saque de {quantidade_saque}; "

    elif escolha == 3:
        print(f"Saldo atual: {saldo}")

    elif escolha == 4:
        print("Encerrando o programa...")
        break

    elif escolha == 5:
        print(f"Histórico de operações: {historico}")

    else:
        print("Opção inválida")
