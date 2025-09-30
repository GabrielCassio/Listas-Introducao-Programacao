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
    numRestantes  = (numJogadores - numEliminados)
    # Caso um jogador seja eliminado reduz 1 do range do loop de jogadores
    for jogador in range(numJogadores):        
        if (not("andre" in nomesEliminados and jogador == 0) and 
            not("bruno" in nomesEliminados and jogador == 1) and 
            not("clara" in nomesEliminados and jogador == 2) and
            not numEliminados == 2):
            resultadoLance = input()
            if (resultadoLance == "acertou"):
                if (jogador == 0):
                    numErros0   = 0 # Reset dos Erros consecutivos
                    if (numRestantes == 3):
                        quantAndre += 2
                        quantBruno -= 1
                        quantClara -= 1
                    elif (numRestantes == 2):
                        quantAndre += 1
                        if (not "bruno" in nomesEliminados): quantBruno -= 1
                        else: quantClara -= 1
                elif (jogador == 1):
                    numErros1   = 0 # Reset dos Erros consecutivos
                    if (numRestantes == 3):
                        quantAndre -= 1
                        quantBruno += 2
                        quantClara -= 1
                    elif (numRestantes == 2):
                        quantBruno += 1
                        if (not "andre" in nomesEliminados): quantAndre -= 1
                        else: quantClara -= 1
                elif (jogador == 2):
                    numErros2   = 0 # Reset dos Erros consecutivos
                    if (numRestantes == 3):
                        quantAndre -= 1
                        quantBruno -= 1
                        quantClara += 2
                    elif (numRestantes == 2):
                        quantClara += 1
                        if (not "bruno" in nomesEliminados): quantBruno -= 1
                        else: quantAndre -= 1
            elif (resultadoLance == "errou"):
                if (jogador == 0): numErros0 += 1
                elif (jogador == 1): numErros1 += 1
                elif (jogador == 2): numErros2 += 1
            
        # Casos de Eliminação de Jogadores
        # Caso André seja eliminado - Bruno 0 -> Clara 1
        if ((quantAndre <= 0 or numErros0 == 3) and not("andre" in nomesEliminados)):
            nomesEliminados += "andre"
            numEliminados += 1
            if (numErros0 == 3): print(f"andre perdeu feio")
            else: print(f"andre saiu do jogo")
        # Caso Bruno seja eleminado - André 0 -> Clara 1
        elif ((quantBruno <= 0 or numErros1 == 3) and not("bruno" in nomesEliminados)):
            nomesEliminados += "bruno"
            numEliminados += 1
            if (numErros1 == 3): print(f"bruno perdeu feio")
            else: print(f"bruno saiu do jogo")
        # Caso Clara seja eliminada - André 0 -> Bruno 1
        elif ((quantClara <= 0 or numErros2 == 3)and not("clara" in nomesEliminados)):
            nomesEliminados += "clara"
            numEliminados += 1
            if (numErros2 == 3): print(f"clara perdeu feio")
            else: print(f"clara saiu do jogo")
        # ------------------------------

    # Verifica se apenas resta um jogador
    if (numEliminados == 2):
        stopJogo    = True  # Troca de execução do Jogo
        # Tratamento de valores negativos
        if (quantAndre <= 0): quantAndre = 0
        if (quantBruno <= 0): quantBruno = 0
        if (quantClara <= 0): quantClara = 0
        # -------------------------------
        # Condições de vitória
        if (not "andre" in nomesEliminados): print(f"andre ganhou")
        elif (not "bruno" in nomesEliminados): print(f"bruno ganhou")
        elif (not "clara" in nomesEliminados): print(f"clara ganhou")
        # --------------------
        # Output Final
        print(f"a quantidade final de bolas foi:\n"
                f"andre: {quantAndre}\n"
                f"bruno: {quantBruno}\n"
                f"clara: {quantClara}")
        # ------------
    # -----------------------------------