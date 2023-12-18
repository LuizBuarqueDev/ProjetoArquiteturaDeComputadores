import random
import time
import threading

ar_condicionado_ligado = False
compressor_ligado = False
evaporadora_ligada = False
temperatura_ambiente = random.randint(10, 50)
temperatura_escolhida = 25
termostato = temperatura_ambiente
tempo_alternar = 0
timer = None

t_0 = temperatura_ambiente
t_amb = temperatura_escolhida
K = 0.1
ultima_temperatura_resfriamento = None


def calcular_temperatura_continua():
    global temperatura_ambiente, temperatura_escolhida, K, ultima_temperatura_resfriamento, evaporadora_ligada
    try:
        while not evaporadora_ligada:
            dT_dt = -K * (temperatura_ambiente - temperatura_escolhida)
            temperatura_ambiente += dT_dt
            if ar_condicionado_ligado and not evaporadora_ligada:
                ultima_temperatura_resfriamento = temperatura_ambiente
            time.sleep(1)
    except Exception as e:
        print(f"Erro ao calcular temperatura: {e}")


def mostrar_temperatura():
    global temperatura_ambiente
    try:
        print(f'''\033[1mTemperatura Atual: {temperatura_ambiente:.2f}°C\033[0m''')
    except Exception as e:
        print(f"Erro ao mostrar temperatura: {e}")


def ligar_compressor():
    global termostato, compressor_ligado
    try:
        print("Baixando a temperatura...")
        print("Temperatura Atual:", termostato)
        thread_temperatura = threading.Thread(target=calcular_temperatura_continua)
        thread_temperatura.start()
        compressor_ligado = False
        mostrar_menu()
    except Exception as e:
        print(f"Erro ao ligar compressor: {e}")


def ligar_condensador():
    global evaporadora_ligada, compressor_ligado
    print('''\033[36mModo alterado para Modo Condensador \033[0;0m''')
    evaporadora_ligada = False
    compressor_ligado = True
    ligar_compressor()


def ligar_ventilador():
    global evaporadora_ligada, compressor_ligado
    print('''\033[36mModo alterado para Modo Ventilador \033[0;0m''')
    evaporadora_ligada = True
    compressor_ligado = False
    if ultima_temperatura_resfriamento is not None:
        temperatura_ambiente = ultima_temperatura_resfriamento
    else:
        print('''\033[31mNão há temperatura anterior registrada no modo Ventilador.\033[0;0m''')


def alterar_modo():
    if ar_condicionado_ligado:
        if evaporadora_ligada:
            ligar_condensador()
        else:
            ligar_ventilador()
    else:
        print('''\033[31mO ar condicionado está desligado. Ligue-o primeiro.\033[0;0m''')


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


def start_time(inicio_timer):
    global timer
    timer = threading.Timer(inicio_timer * 1, ligar_desligar)
    timer.start()


def mostrar_menu():
    print("\n=== Controle Ar Condicionado ===")
    if not ar_condicionado_ligado:
        print("""\033[1mAr Desligado \033[0m""")
        print("1. Ligar Ar Condicionado")
        print("4. Definir Timer")
    else:
        print("""\033[1mAr Ligado \033[0m""")
        print("1. Desligar Ar Condicionado")
        print("2. Ajustar temperatura")
        print("3. Alterar modo")
        print("4. Definir Timer")
        print("5. Mostrar temperatura atual")
    print('-' * 30)


mostrar_menu()
while True:
    try:
        entrada = str(input("Digite a opção desejada: "))

        if entrada == "1":
            ligar_desligar()

        elif entrada == "2" and ar_condicionado_ligado:
            temperatura_escolhida = int(input("Digite a nova temperatura desejada: "))
            print(f'''\033[32mTemperatura ajustada para {temperatura_escolhida}°C\033[0;0m''')

        elif entrada == "3" and ar_condicionado_ligado:
            alterar_modo()

        elif entrada == "4":
            tempo_alternar = int(input(
                f"Digite em quanto tempo o ar condicionado deve {'desligar' if ar_condicionado_ligado else 'ligar'} (em minutos): "))
            print(f'''\033[32mO temporizador foi configurado para {tempo_alternar} minutos\033[0;0m''')
            start_time(tempo_alternar)

        elif entrada == "5":
            mostrar_temperatura()

        else:
            print('''\033[31mDigite uma opção válida\033[0;0m''')

        mostrar_menu()

    except Exception as e:
        print(f"Erro geral: {e}")
