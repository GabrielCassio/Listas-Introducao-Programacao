# André 0-> Bruno 1-> Clara 2 
quantAndre  = int(input())
quantBruno  = int(input())
quantClara  = int(input())

quantJogador0, quantJogador1, quantJogador2    = quantAndre, quantBruno, quantClara

stopJogo, numJogadores    = False, 3

while(not stopJogo):
    # Caso um jogador seja eliminado reduz 1 do range do loop de jogadores
    for jogador in range(numJogadores):
        resultadoLance = input()
        if (resultadoLance == "acertou"):
            if (jogador == 0):
                quantJogador0 += 1
                quantJogador2 -= 1
                quantJogador2 -= 1
            elif (jogador == 1):
                quantJogador0 -= 1
                quantJogador1 += 1
                quantJogador2 -= 1
            elif (jogador == 2):
                quantJogador0 -= 1
                quantJogador1 -= 1
                quantJogador2 += 1
        elif (resultadoLance == "errou"):
            if (jogador == 0):
                quantJogador0 -= 1
            elif (jogador == 1):
                quantJogador1 -= 1
            elif (jogador == 2):
                quantJogador2 -= 1
        
        # Caso André seja eliminado - Bruno 0 -> Clara 1
        if (quantJogador0 == 0):
            quantJogador0, quantJogador1  = quantJogador1, quantJogador2
            numJogadores    -= 1
        # Caso Bruno seja eleminado - André 0 -> Clara 1
        elif (quantJogador1 == 0):
            quantJogador1   = quantJogador2
            numJogadores    -= 1
        # Caso Clara seja eliminada - André 0 -> Bruno 1
        elif (quantJogador2 == 0):
            numJogadores    -= 1
        