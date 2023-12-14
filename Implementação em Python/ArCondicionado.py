import random
import time

ar_condicionado_ligado = False
temperatura_escolhida = 25
temperatura_atual = random.randint(15, 50)
compressor_ligado = False


tempo_desligar = 0


def ligar_compressor():
    global temperatura_atual
    while temperatura_escolhida < temperatura_atual:
        print("Temperatura Atual:", temperatura_atual)
        temperatura_atual -= 1
        time.sleep(0.15)
    print("Fim do resfriamento.")


def ligar_desligar():
    global ar_condicionado_ligado, compressor_ligado
    ar_condicionado_ligado = not ar_condicionado_ligado
    if ar_condicionado_ligado:
        compressor_ligado = True
        ligar_compressor()

    else:
        compressor_ligado = False
        print("Ar condicionado desligado.")

def timer ():
    global tempo_desligar
    while tempo_desligar > 0:
        print(f"Tempo restante : {tempo_desligar}")
        tempo_desligar -= 1
        time.sleep(60)


while True:
    print("\nControle Ar Condicionado")
    print("Ar")
    print("1. Ligar/Desligar")
    if ar_condicionado_ligado:
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

    elif entrada == 4 and ar_condicionado_ligado:
        tempo_desligar = int(input("Digite o tempo para desligar (minutos): "))
        timer()


        print(f"Ar condicionado desligará em {tempo_desligar} minutos.")
        print("Timers configurados.")