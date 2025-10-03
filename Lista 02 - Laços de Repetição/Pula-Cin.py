# Output inicial
print(f"INICIANDO SIMULAÇÃO...")

# Tratamento do nome dos jogadores
namePLayer1, namePlayer2, pointArthur, pointSamuel = input(), "", 0, 0  
while (namePLayer1 != "Arthur" and namePLayer1 != "Samuel"):            # Validação do nome do jogador 1
    print(f"Jogador inválido! Essa competição é apenas entre Arthur e Samuel!")
    namePLayer1 = input()
print(f"{namePLayer1} começa na corda!")    # Caso o nome seja válido
if (namePLayer1 == "Arthur"): namePlayer2 = "Samuel"
else: namePlayer2 = "Arthur"
# -------------------------------- 

numRounds, currentRound = int(input()), 0   # Número de rounds a serem jogados

while (currentRound < numRounds):   # Loop para cada round
    currentRound += 1               # Atualiza índice da rodada
    oneTimeOutput, ritmo, totalBet  = False, int(input()), int(input())
    # Outputs Iniciais de uma nova rodada
    print(f"Começa a {currentRound}ª rodada!")
    if (currentRound == numRounds): print(f"Última rodada! Valendo 2 pontos!")

    # Variáveis de Aposta | Variáveis de Tropeço | Giros
    currentBet, diffBet, lastDiff, numStumble, onStumble, stopGiros  = 0, 0, 0, 0, False, False 
    # Output Inicial para cada vez em que o jogador mudar
    print(f"{namePlayer2} aposta que {namePLayer1} não chega a {totalBet} pulos! Vamos ver se é verdade! O ritmo de {namePLayer1} será {ritmo}!")
    
    # Loop para giradas de corda
    while (not stopGiros): 
        # Pulos Restantes | Soma dos Algarismos
        diffBet, sumAlgarismos  = totalBet - currentBet, 0 
        for algarismo in str(diffBet): sumAlgarismos += int(algarismo) # Realiza Soma

        # Estado de Pertinência de Fibonacci | Número de Fibonacci
        isQuadratic, num = False, 0
        for case in range(2):
            if (case == 0): num = 5 * (sumAlgarismos ** 2) + 4
            elif (case == 1): num = 5 * (sumAlgarismos ** 2) - 4
            start, end = 0, num
            while (start <= end and not isQuadratic):
                middle = (start + end) // 2
                square = middle * middle
                if square == num: isQuadratic = True
                elif square < num: start = middle + 1
                else: end = middle - 1

        # Veriificação de Tropeço
        if (isQuadratic): 
            numStumble += 1 # Incrementa tropeço do Jogador
            print(f"O número da soma é {sumAlgarismos}, que faz parte da sequência de Fibonacci!! {namePLayer1} tropeça!")
        # Caso não tropeçe
        else:
            if (diffBet < totalBet/4 and not oneTimeOutput):
                oneTimeOutput = True
                print(f"{namePLayer1} está quase chegando ao apostado! Falta pouco!")
            else:
                print(f"{namePLayer1} pula com maestria! Faltam {diffBet} pulos!")

        # Conidções de para os Giros
        currentBet += ritmo  # Incrementa os pulos do jogador
        # Condição de 3 Tropeçar 3 vezes
        if (numStumble == 3):
            stopGiros, onStumble = True, True  # Jogador tropeça
            print(f"E agora não tem jeito, {namePLayer1} cai de cara no chão!")
        elif (currentBet >= totalBet):
            # Condição de alcançar a Aposta
            stopGiros = True
    # Fim Loop Giros ---------------------------------------------------

    # Condição de pontuação
    # Caso ele não tenha tropeçado
    if (not onStumble):
        diffBet = abs(totalBet - currentBet)
        if (currentRound == numRounds):  # Última rodada vale 2 pontos
            if (namePLayer1 == "Arthur"): pointArthur += 2
            else: pointSamuel += 2
        # Rodada normal vale 1 ponto
        else:
            if (namePLayer1 == "Arthur"): pointArthur += 1
            else: pointSamuel += 1
    # -------------------------------

    # Mensagens finais para cada resultado
    if (currentBet < totalBet//2): print(f"Nossa!! Parece que {namePLayer1} não chegou nem na metade do apostado! Ainda bem que não foi competir pra valer no Round 6!")
    elif (totalBet//2 <= currentBet < int(0.75*totalBet)): print(f"Nem muito perto, nem muito longe do apostado. Talvez {namePLayer1} teve apenas azar!")
    elif (int(0.75*totalBet) <= currentBet < totalBet):
        print(f"Quase lá! por pouco {namePLayer1} não alcançou o apostado!")

    if (not onStumble):
        if (currentBet == totalBet): print(f"{namePLayer1} cumpriu o prometido e alcançou {totalBet} pulos! Ponto merecidíssimo!")
        elif (currentBet > totalBet): print(f"{namePLayer1} vai além, e supera a aposta em {diffBet} Ponto(s)! Deixou o {namePlayer2} no chinelo!")
    # -------------------------------

    # Realizando a troca dos jogadores
    namePLayer1, namePlayer2 = namePlayer2, namePLayer1
# Fim loop rodadas
print(f"COMPUTANDO PREVISÃO FINAL...")

if (pointArthur > pointSamuel): print(f"Arthur venceu a competição com {pointArthur} ponto(s)! Trouxe orgulho para Maceió!")
elif (pointSamuel > pointArthur): print(f"Samuel venceu a competição com {pointSamuel} ponto(s)! O Messi careca em sua foto de perfil ficaria impressionado se soubesse!")
elif (pointSamuel == pointArthur and pointArthur > 0): print(f"Houve um empate técnico! Ambos fizeram {pointArthur} ponto(s)! Óbvio que os dois monitores mais rápidos iriam empatar!")
elif (pointArthur == pointSamuel == 0): print(f"Ninguém pontuou! Que competição sem graça! Acho que os monitores se garantem mais nas dúvidas de IP mesmo...")