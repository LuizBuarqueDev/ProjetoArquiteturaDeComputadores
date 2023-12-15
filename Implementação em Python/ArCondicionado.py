import random
import time
import threading

ar_condicionado_ligado = False
compressor_ligado = False
temperatura_ambiente = random.randint(10, 50)
temperatura_escolhida = 25
termostato = temperatura_ambiente
tempo_desligar = 0


def ligar_compressor():
    global termostato, compressor_ligado
    while temperatura_escolhida < termostato:
        print("Temperatura Atual:", termostato)
        termostato -= 1
        time.sleep(0.15)
    compressor_ligado = False
    print("Fim do resfriamento.")


def ligar_desligar():
    global ar_condicionado_ligado, compressor_ligado
    ar_condicionado_ligado = not ar_condicionado_ligado
    if ar_condicionado_ligado:
        compressor_ligado = True
        ligar_compressor()
        print("<Ar condicionado ligado.>")
    else:
        compressor_ligado = False
        print("<Ar condicionado desligado.>")


def run_timer(tempo_definido):
    while tempo_definido > 0:
        tempo_definido -= 1
        time.sleep(0.5)
        print(f"{tempo_definido}; ", end="")
    ligar_desligar()


while True:
    print("\nControle Ar Condicionado")
    print("Ar")
    print("1. Ligar/Desligar")
    print(f"4. Definir Timer\n {'-' * 50}")

    if ar_condicionado_ligado:
        print("**Ar Ligado**")
        print("1. Ligar/Desligar")
        print("2. Ajustar temperatura")
        print("3. Alterar modo")
        print("4. Definir Timer")

    entrada = int(input("Digite a opção desejada: "))

    if entrada == 1:
        print("Ligando/Desligando")
        ligar_desligar()

    elif entrada == 2 and ar_condicionado_ligado:
        nova_temperatura = int(input("Digite a nova temperatura desejada: "))
        temperatura_escolhida = nova_temperatura
        print("Temperatura ajustada para", temperatura_escolhida, "°C")

    elif entrada == 3 and ar_condicionado_ligado:
        print("Modo de operação alterado")
        # alterar o modo de operação

    elif entrada == 4:
        tempo_definido = int(input(
            f"Digite em quanto tempo o ar condicinado deve {"ligar" if not ar_condicionado_ligado else "desligar"}: "))
        print(f"O timer esta configurado para {tempo_definido}")

        inicio_timer = threading.Thread(target=run_timer, args=(tempo_definido,))
        inicio_timer.start()
        inicio_timer.join()

    else:
        print("Digite uma opção valida")
