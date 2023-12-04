import random

ar_condicionado_ligado = False
temperatura_escolhida = 25
compressor = False


def ligar_desligar():
    global  ar_condicionado_ligado
    ar_condicionado_ligado = not ar_condicionado_ligado


while True :
    print("Controle Ar Condicionado")

    print("1. Ligar/ Desligar")
    print("2. Ajustar temperatura")
    print("3. Altera modo")
    print("4. Definir Time")

    entrada = int(input("Digite a opção desejada:"))
    if entrada == 1:
        ligar_desligar()
