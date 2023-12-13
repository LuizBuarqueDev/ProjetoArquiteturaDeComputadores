import random
import time

ar_condicionado_ligado = False
temperatura_escolhida = 25
temperatura_atual = random.randint(15, 50)
compressor_ligado = False


tempo_ligar = 0
tempo_desligar = 0


def ligar_compressor():
    global temperatura_atual
    while temperatura_escolhida < temperatura_atual:
        print("Temperatura Atual:", temperatura_atual)
        temperatura_atual -= 1
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


def verificar_timers():
  global ar_condicionado_ligado, timer_ligar, timer_desligar

  tempo_atual = int(time.time()/60)

  if ar_condicionado_ligado and tempo_ligar != 0 and tempo_atual >= timer_ligar:
      if not compressor_ligado:
          print("Ligando o ar condicionado")
          ligar_desligar()
      timer_ligar = 0 #reseta o timer ligar

  if ar_condicionado_ligado and tempo_desligar != 0 and tempo_atual >= timer_desligar:
      if compressor_ligado:
          print("Timer chegou ao fim. Desligando o ar condicionado")
          ligar_desligar()
      timer_desligar = 0

def monitorar_timer():
    global tempo_ligar, tempo_desligar

    tempo_atual = int(time.time() / 60)  # Convertendo para minutos

    tempo_restante_ligar = max(0, tempo_ligar - tempo_atual)
    tempo_restante_desligar = max(0, tempo_desligar - tempo_atual)

    return tempo_restante_ligar, tempo_restante_desligar

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
        tempo_ligar = int(input("Digite o tempo para ligar (minutos): "))
        tempo_desligar = int(input("Digite o tempo para desligar (minutos): "))

        # Definir os tempos de ligar e desligar baseados no tempo atual
        timer_ligar = int(time.time() / 60) + tempo_ligar
        timer_desligar = int(time.time() / 60) + tempo_desligar

        print(f"Ar condicionado ligará em {tempo_ligar} minutos e desligará em {tempo_desligar} minutos.")
        print("Timers configurados.")

        if ar_condicionado_ligado:
            tempo_restante_ligar, tempo_restante_desligar = monitorar_timer()
            print(f"Tempo restante para ligar: {tempo_restante_ligar} minutos")
            print(f"Tempo restante para desligar: {tempo_restante_desligar} minutos")

    verificar_timers()