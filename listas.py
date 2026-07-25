# Lista de Compras
# Sistema com menu para gerenciar uma lista de compras: adicionar,
# remover, mostrar (com numeração), limpar e encerrar.

lista = []

while True:
    escolha = int(input("Escolha uma opção:\n1 - Adicionar produto\n2 - Remover produto\n3 - Mostrar lista\n4 - Limpar lista\n5 - Encerrar\nDigite aqui: "))

    if escolha == 1:
        novo_item = input("Adicione aqui seu novo item: ")
        lista.append(novo_item)
        print("Novo item adicionado: ", lista)

    elif escolha == 2:
        remover_item = input(f"Qual desses itens: {lista} você deseja remover? ")
        lista.remove(remover_item)
        print("Item removido: ", lista)

    elif escolha == 3:
        for i in range(len(lista)):
            print(f"Posição {i + 1}: {lista[i]}")

    elif escolha == 4:
        lista.clear()
        print(f"Lista limpa: {lista}")

    elif escolha == 5:
        print('Fechando Programa...')
        break

    else:
        print("Número de operação inválido")
