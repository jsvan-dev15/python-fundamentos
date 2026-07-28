# Operações matemáticas
# Módulo com funções reutilizáveis de cálculo, usadas pelo main.py

def somar(a, b):
    soma = a + b
    return soma

def subtrair(a, b):
    diminuir = a - b
    return diminuir

def multiplicar(a, b):
    multiplicando = a * b
    return multiplicando

def dividir(a, b):
    dividindo = a / b
    return dividindo

def calcular_media(a, b):
    media = (a + b) / 2
    return media

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
