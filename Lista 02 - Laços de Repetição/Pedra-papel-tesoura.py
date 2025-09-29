# Inputs iniciais
doces                             = int(input())
jogador1, vida1, jogador2, vida2  = input(), 10, input(), 10
# ---------------
# Variáveis do Jogo
stopJogo    = False
numRodada   = 0
# ---------------------------
# Verifica se Arthur está no jogo
if (jogador1 != "Arthur" and jogador2 != "Arthur"):
    print(f"Epa!!! E cadê o dono dos doces??") # Caso não esteja
# -------------------------------
else:
    print(f"A batalha vai começar!") # Caso esteja no Jogo
    while(not stopJogo):
        numRodada += 1  # Incrementa a quantidade Rodadas em um jogo
        stopRodada, ganhadorRodada  = False, "" # Condição de fim de Rodada
        # Decremntação do número de doces
        if (numRodada == 1 and doces % 10 != 0):
            print(f"Pra aquecer, essa primeira vale menos, só {doces%10} doces!")
            doces -= (doces % 10)
        else:
            print(f"Batalha número {numRodada}!")
            doces -= 10
        # -------------------------------
        while(not stopRodada):
            # Jogadas de cada jogador
            jogada1 = input() # Jogada do jogador 1
            jogada2 = input() # Jogada do jogador 2
            if (jogada1 == jogada2): print(f"Eita, jogaram a mesma coisa dessa vez.")
            else: 
                if (jogada1 == "papel" and jogada2 == "tesoura"):
                    vida1 -= 3
                    vida2 += 1
                elif (jogada1 == "pedra" and jogada2 == "papel"):
                    vida1 -= 2
                    vida2 += 2
                elif (jogada1 == "tesoura" and jogada2 == "pedra"):
                    vida1 -= 4
                elif (jogada2 == "papel" and jogada1== "tesoura"):
                    vida2 -= 3
                    vida1 += 1
                elif (jogada2 == "pedra" and jogada1 == "papel"):
                    vida2 -= 2
                    vida1 += 2
                elif (jogada2 == "tesoura" and jogada1 == "pedra"):
                    vida2 -= 4
                # Tratamento de Caso com vida negativa
                if (vida1 <= 0): vida1, stopRodada  = 0, True
                elif (vida2 <= 0): vida2, stopRodada    = 0, True
                # ------------------------------------
                print(f"Esse turno terminou com {jogador1} tendo {vida1} de vida e {jogador2} tendo {vida2}!")
            # -----------------------
        # Definindo Ganhador da Rodada
        if (vida1 == 0): ganhadorRodada = jogador2
        elif (vida2 == 0): ganhadorRodada   = jogador1
        print(f"A rodada {numRodada} vai para {ganhadorRodada}, que garante seus doces!")
        # -----------------
        vida1, vida2    = 10, 10    # Reset das vidas dos jogadores
        # Condicao de fim de jogo
        if (doces == 0): stopJogo    = True
        # -----------------------