import random
import time
import threading
from scipy.integrate import odeint

# Variáveis globais para o controle do ar condicionado
ar_condicionado_ligado = False
compressor_ligado = False
temperatura_ambiente = random.randint(10, 50)
temperatura_escolhida = 25  # Temperatura padrão do Ar
termostato = temperatura_ambiente
tempo_alternar = 0
timer = None

t_0 = temperatura_ambiente
t_amb = temperatura_escolhida
K = 0.1
t = range(0, 61, 1)


# Função para calcular a temperatura usando a Lei do Resfriamento de Newton
def lei_do_resfriamento_de_newton(T, t, T_amb, k):
    dT_dt = -k * (T - T_amb)
    solution = odeint(dT_dt, t_0, t, args=(t_amb, K))


# Função para calcular a temperatura atual a cada segundo e exibir na tela
def calcular_temperatura():
    global temperatura_ambiente, temperatura_escolhida, K
    for _ in range(60):  # 60 segundos
        dT_dt = -K * (temperatura_ambiente - temperatura_escolhida)
        temperatura_ambiente += dT_dt  # Atualiza a temperatura ambiente


def mostrar_temperatura():
    print(f"Temperatura Atual: {temperatura_ambiente:.2f}°C")
    calcular_temperatura()


# Função para ligar o compressor
def ligar_compressor():
    global termostato, compressor_ligado
    print("Baixando a temperatura...")
    print("Temperatura Atual:", termostato)

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
            # Iniciar o cálculo da temperatura em uma thread separada
            thread_temperatura = threading.Thread(target=calcular_temperatura)
            thread_temperatura.start()
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
        print("5. Mostrar temperatura atual")
    print('-' * 30)


def start_time(inicio_timer):
    # Inicializa o temporizador em uma thread separada
    global timer
    timer = threading.Timer(inicio_timer * 1, ligar_desligar)
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

    elif entrada == "5":
        mostrar_temperatura()

    else:
        print("Digite uma opção válida")

    mostrar_menu()  # Mostra o menu após ação do usuário
