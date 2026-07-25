# Sistema de Login
# Permite até 3 tentativas de acesso, bloqueando o sistema se todas falharem

usuario = "jsvan123"
pin = 123
contador = 0

while True:
    usuario_digitado = input("Informe o usuário: ")
    pin_digitado = int(input("Informe o pin: "))
    contador += 1
    if usuario_digitado == usuario and pin_digitado == pin:
        print(f"Bem vindo {usuario}")
        break
    else:
        print("Usuário ou pin incorretos")
    if contador >= 3:
        print("Sistema bloqueado")
        break
