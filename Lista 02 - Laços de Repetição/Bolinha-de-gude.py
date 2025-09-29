# André 0-> Bruno 1-> Clara 2
# Quantidades de Bolinha de Gude de cada Jogador
quantAndre, quantBruno, quantClara, numErros0, numErros1, numErros2  = int(input()), int(input()), int(input()), 0, 0, 0
# ---------------------------------------------
# Variáveis de eliminação
nomesEliminados, numEliminados = "", 0
# -----------------------
# Variáveis do jogo
stopJogo, numJogadores    = False, 3
# -----------------

while(not stopJogo):

    # Caso um jogador seja eliminado reduz 1 do range do loop de jogadores
    for jogador in range(numJogadores):
        if (not("André" in nomesEliminados and jogador == 0) and 
            not("Bruno" in nomesEliminados and jogador == 1) and 
            not("Clara" in nomesEliminados and jogador == 2)):
            resultadoLance = input()
            if (resultadoLance == "acertou"):
                if (jogador == 0):
                    quantAndre  += 2
                    quantBruno  -= 1
                    quantClara  -= 1
                    numErros0   = 0
                elif (jogador == 1):
                    quantAndre  -= 1
                    quantBruno  += 2
                    quantClara  -= 1
                    numErros1   = 0
                elif (jogador == 2):
                    quantAndre  -= 1
                    quantBruno  -= 1
                    quantClara  += 2
                    numErros2   = 0
            elif (resultadoLance == "errou"):
                if (jogador == 0): 
                    quantAndre -= 1
                    numErros0 += 1
                elif (jogador == 1): 
                    quantBruno -= 1
                    numErros1 += 1
                elif (jogador == 2): 
                    quantClara -= 1
                    numErros2 += 1
            
        # Caso André seja eliminado - Bruno 0 -> Clara 1
        if (quantAndre <= 0 and not("André" in nomesEliminados)):
            nomesEliminados += "André"
            numEliminados += 1
            print(f"André saiu do jogo")
        # Caso Bruno seja eleminado - André 0 -> Clara 1
        elif (quantBruno <= 0 and not("Bruno" in nomesEliminados)):
            nomesEliminados += "Bruno"
            numEliminados += 1
            print(f"Bruno saiu do jogo")
        # Caso Clara seja eliminada - André 0 -> Bruno 1
        elif (quantClara <= 0 and not("Clara" in nomesEliminados)):
            nomesEliminados += "Clara"
            numEliminados += 1
            print(f"Clara saiu do jogo")

        if (numErros0 == 3): print()
        
    if (numEliminados == 2): 
        stopJogo    = True
        if (not "André" in nomesEliminados): print(f"André ganhou")
        elif (not "Bruno" in nomesEliminados): print(f"Bruno ganhou")
        elif (not "Clara" in nomesEliminados): print(f"Clara ganhou")