# Sistema de Cadastro com Persistência em JSON
# Os dados são salvos em cadastro.json e carregados automaticamente
# ao iniciar o programa, permitindo que os cadastros sobrevivam
# ao fechar e reabrir o programa.

import json
import os

if os.path.exists("cadastro.json"):
    with open("cadastro.json", "r") as arquivo:
        cadastro = json.load(arquivo)
else:
    cadastro = {}

while True:
    escolha = int(input("Escolha uma opção:\n1 - Cadastrar pessoa\n2 - Mostrar todos os cadastros\n3 - Encerrar\n4 - Procurar por pessoa\n5 - Editar pessoa\nDigite aqui: "))

    if escolha == 1:
        nome = str(input("Qual o seu primeiro nome? "))
        idade = int(input("Qual a sua idade? "))
        cidade = str(input("Qual a sua cidade? "))
        cadastro[nome] = {"nome": nome, "idade": idade, "cidade": cidade}
        with open("cadastro.json", "w") as arquivo:
            json.dump(cadastro, arquivo)
        print(cadastro)

    elif escolha == 2:
        print(cadastro)

    elif escolha == 3:
        print('Fechando programa...')
        break

    elif escolha == 4:
        procurar = str(input("Digite o nome da pessoa que estiver procurando: "))
        if procurar in cadastro:
            print("Essa pessoa está cadastrada:", cadastro[procurar])
        else:
            print("Pessoa não encontrada")

    elif escolha == 5:
        procurar = str(input("Digite o nome da pessoa que estiver procurando para edição: "))
        if procurar in cadastro:
            print("Informe o novo nome, idade e cidade abaixo:\n")
            nome = str(input("Qual o novo nome? "))
            idade = int(input("Qual a nova idade? "))
            cidade = str(input("Qual a nova cidade? "))
            cadastro[procurar] = {"nome": nome, "idade": idade, "cidade": cidade}
            with open("cadastro.json", "w") as arquivo:
                json.dump(cadastro, arquivo)
        else:
            print("Pessoa não encontrada")

    else:
        print("Número inválido")
