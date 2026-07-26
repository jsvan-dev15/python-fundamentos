# Sistema de Cadastro
# Utiliza um dicionário de dicionários: cada pessoa cadastrada é um
# dicionário (nome, idade, cidade), guardado dentro do dicionário
# principal usando o nome como chave.

cadastro = {}

while True:
    escolha = int(input("Escolha uma opção:\n1 - Cadastrar pessoa\n2 - Mostrar todos os cadastros\n3 - Encerrar\n4 - Procurar por pessoa\nDigite aqui: "))

    if escolha == 1:
        nome = str(input("Qual o seu primeiro nome? "))
        idade = int(input("Qual a sua idade? "))
        cidade = str(input("Qual a sua cidade? "))
        cadastro[nome] = {"nome": nome, "idade": idade, "cidade": cidade}
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

    else:
        print("Número inválido")
