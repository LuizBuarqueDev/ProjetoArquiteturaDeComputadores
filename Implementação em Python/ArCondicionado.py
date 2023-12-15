import random
import time
import threading

# Variáveis globais para o controle do ar condicionado
ar_condicionado_ligado = False
compressor_ligado = False
temperatura_ambiente = random.randint(10, 50)
temperatura_escolhida = 25
termostato = temperatura_ambiente
tempo_alternar = 0


# Função para ligar o compressor e resfriar
def ligar_compressor():
    global termostato, compressor_ligado
    print("Temperatura Atual:", end="")
    while temperatura_escolhida < termostato:
        print(end=f"; {termostato}")
        termostato -= 1
        time.sleep(0.15)

    compressor_ligado = False
    print("\nFim do resfriamento.")


# Função para ligar/desligar o ar condicionado
def ligar_desligar():
    global tempo_alternar
    if tempo_alternar > 0:
        tempo_alternar = 0
        start_time(tempo_alternar)

    else:
        global ar_condicionado_ligado, compressor_ligado
        ar_condicionado_ligado = not ar_condicionado_ligado
        if ar_condicionado_ligado:
            compressor_ligado = True
            ligar_compressor()
            print("<Ar condicionado ligado.>")
        else:
            compressor_ligado = False
            print("<Ar condicionado desligado.>")


# Função para executar o temporizador
def run_timer():
    global tempo_alternar
    while tempo_alternar > 0:
        tempo_alternar -= 1
        time.sleep(10)
        print(f"{tempo_alternar}; ", end="")
    print(" ")
    ligar_desligar()


# Função para mostrar o menu
def mostrar_menu():
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


def start_time(inicio_timer):
    # Inicializa o temporizador em uma thread separada
    inicio_timer = threading.Thread(target=run_timer)
    inicio_timer.start()


# Loop principal
while True:
    mostrar_menu()
    entrada = int(input("Digite a opção desejada: "))

    if entrada == 1:
        print("Ligando/Desligando")
        ligar_desligar()

    elif entrada == 2 and ar_condicionado_ligado:
        temperatura_escolhida = int(input("Digite a nova temperatura desejada: "))
        print("Temperatura ajustada para", temperatura_escolhida, "°C")

    elif entrada == 3 and ar_condicionado_ligado:
        print("Modo de operação alterado")
        # Adicione o código para alterar o modo de operação

    elif entrada == 4:
        tempo_alternar = int(input(
            f"Digite em quanto tempo o ar condicionado deve {'ligar' if not ar_condicionado_ligado else 'desligar'}: "))
        print(f"O timer está configurado para {tempo_alternar}")
        start_time(tempo_alternar)

    else:
        print("Digite uma opção válida")
