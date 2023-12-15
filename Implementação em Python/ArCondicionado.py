import random
import time
import threading

# Variáveis globais para o controle do ar condicionado
ar_condicionado_ligado = False
compressor_ligado = False
temperatura_ambiente = random.randint(10, 50)
temperatura_escolhida = 25  # Temperatura padrão do Ar
termostato = temperatura_ambiente
tempo_alternar = 0
timer = None  # Variável global para o temporizador


# Função para ligar o compressor e resfriar
def ligar_compressor():
    global termostato, compressor_ligado
    print("Baixando a temperatura...")
    print("Temperatura Atual:", termostato, end="")
    while temperatura_escolhida < termostato:
        print(end=f"; {termostato - 1}")
        termostato -= 1
        time.sleep(0.15)

    compressor_ligado = False
    print("\nFim do resfriamento.")


# Função para ligar/desligar o ar condicionado
def ligar_desligar():
    global tempo_alternar, timer
    if tempo_alternar > 0:
        tempo_alternar = 0
        if timer:
            timer.cancel()  # Cancela o temporizador atual
        start_time(tempo_alternar)
    else:
        global ar_condicionado_ligado, compressor_ligado
        ar_condicionado_ligado = not ar_condicionado_ligado
        if ar_condicionado_ligado:
            compressor_ligado = True
            print("\nLigando o ar condicionado...")
            ligar_compressor()
            if tempo_alternar > 0:
                start_time(tempo_alternar)
        else:
            compressor_ligado = False


# Função para mostrar o menu
def mostrar_menu():
    print("\n=== Controle Ar Condicionado ===")
    if not ar_condicionado_ligado:
        print("**Ar desligado**")
        print("1. Ligar Ar Condicionado")
        print("4. Definir Timer")
    else:
        print("**Ar Ligado**")
        print("1. Desligar Ar Condicionado")
        print("2. Ajustar temperatura")
        print("3. Alterar modo")
        print("4. Definir Timer")
    print('-' * 30)


def start_time(inicio_timer):
    # Inicializa o temporizador em uma thread separada
    global timer
    timer = threading.Timer(inicio_timer * 60, ligar_desligar)
    timer.start()


# Loop principal
mostrar_menu()
while True:
    entrada = str(input("Digite a opção desejada: "))

    if entrada == "1":
        ligar_desligar()

    elif entrada == "2" and ar_condicionado_ligado:
        temperatura_escolhida = int(input("Digite a nova temperatura desejada: "))
        print("Temperatura ajustada para", temperatura_escolhida, "°C")

    elif entrada == "3" and ar_condicionado_ligado:
        print("Opção ainda não implementada - Alterar Modo")

    elif entrada == "4":
        tempo_alternar = int(input(
            f"Digite em quanto tempo o ar condicionado deve {'desligar' if ar_condicionado_ligado else 'ligar'} (em minutos): "))
        print(f"O temporizador foi configurado para {tempo_alternar} minutos")
        start_time(tempo_alternar)

    else:
        print("Digite uma opção válida")

    mostrar_menu()  # Mostra o menu após ação do usuário
