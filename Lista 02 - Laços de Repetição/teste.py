# Setup de variáveis
vidaAdvinho             = 6
qtdRodadas, atualRodada = int(input()), 0
# Condição de Próxima Etapa
fimJogo, vidaIgualZero    = False, False

# Output inicial do jogo
print(f"Que comece o jogo! Adivinhe a palavra, mas cuidado para não cair na armadilha.")

# Loop de Rodadas
while((not vidaIgualZero) and (not fimJogo)):
    # Início da rodada 
    atualRodada += 1
    print(f"Rodada {atualRodada}/{qtdRodadas}:")
    if (atualRodada == qtdRodadas): fimJogo = True
    # Socilicita as palavras do jogo
    palavraSecreta, palavraFantasma, letrasRepitidas, palavraEmRegra = input().lower(), input().lower(), "", False
    tamSecreta, tamFantasma = len(palavraSecreta), len(palavraFantasma)

    descobriuPalavra = False
    # --------------------------------------------------------------
    while (not palavraEmRegra):
        qtdLetrasComuns = 0
        for letraFantasma in palavraFantasma:
            if ((letraFantasma in palavraSecreta) and (not letraFantasma in letrasRepitidas)):
                qtdLetrasComuns += 1
                letrasRepitidas += letraFantasma
        if (qtdLetrasComuns >= 3):
            print(f"A palavra fantasma possui {qtdLetrasComuns} letras presentes na palavra secreta. Tente uma com menos de 3 letras iguais.")
            palavraFantasma, qtdLetrasComuns, letrasRepitidas    = input().lower(), 0, ""
        else: palavraEmRegra, qtdLetrasComuns = True, 0
    # Fim da parte do Desafiante ------------
    
    # Formatação de Outputs
    palavraSaida = ""
    for caractere in range(tamSecreta): 
        palavraSaida += "_"
        if (not caractere + 1 == tamSecreta): palavraSaida += " "
    print(f"Palavra: {palavraSaida}")
    # ------------------------------------------------

    # Variáveis para cada advinhação
    descobriuPalavra = False
    numTentativas, letrasUsadas, acertouLetra    = 0, "", False
    tentativasSaida    = ""
    # Loop de Advinhação Letra por Letra
    while((not vidaIgualZero) and (not descobriuPalavra)):
        letraIn = input().lower()

        # Verifica se a Letra é repetida
        if (letraIn in letrasUsadas):
            # Caso repetida possui apenas a seguinte saída
            print(f"Você já tentou a letra '{letraIn}'. Tente outra.")
        # Fim da verificação -----------------------
        else:
            numTentativas   += 1
            letrasUsadas    += letraIn
            # Caso não seja repetida -----------
            if (letraIn in palavraSecreta):
                acertouLetra     = True
                print(f"Boa! A letra '{letraIn}' está na palavra.")
            elif ((not letraIn in palavraSecreta) and (not letraIn in palavraFantasma)):
                vidaAdvinho   -= 1
                print(f"Naao! A letra '{letraIn}' não está na palavra. Você perdeu 1 vida.")
            elif ((not letraIn in palavraSecreta) and (letraIn in palavraFantasma)):
                vidaAdvinho   -= 2
                print(f"CUIDADO! A letra '{letraIn}' é uma armadilha! Você perdeu 2 vidas.")
            # ------------------------------

        if (vidaAdvinho <= 0): 
            vidaIgualZero = True
        elif (acertouLetra):
            acertouLetra, posLetraSecreta, novaPalavra = False, 0, ""
            for letra in palavraSecreta:
                posLetraSecreta += 1
                if (letraIn == letra):
                    indexSubstituir = 0
                    for caractere in palavraSaida:
                        indexSubstituir += 1
                        if ((2 * posLetraSecreta - 1)   == indexSubstituir):
                            novaPalavra += f"{letraIn}"
                        else:
                            novaPalavra += f"{caractere}"
                    palavraSaida, novaPalavra = novaPalavra, ""
            
            # Verifica se acertou tudo
            if (not "_" in palavraSaida): descobriuPalavra = True

        # Processa informações para a saída -------
        # Letras chutadas
        if (not letraIn in tentativasSaida):
            if (tentativasSaida == ""): tentativasSaida += letraIn
            else: tentativasSaida += f", {letraIn}"
        # Fim do processamento --------------------

        # Saída para quando não se acerta todas as letras ou zera a vida
        if ((not descobriuPalavra) and (not vidaIgualZero)):
            print(f"=====================\n"
                f"Palavra: {palavraSaida}\n"
                f"Vidas restantes: {vidaAdvinho}\n"
                f"Letras chutadas: {tentativasSaida}\n"
                f"=====================")
        
        if (descobriuPalavra):
            palavraSecreta = palavraSecreta.capitalize()
            vidaAdvinho  = 6
            print(f"Parabéns, Adivinho! Você descobriu a palavra secreta: {palavraSecreta}.\n"
                    f"Total de tentativas: {numTentativas}")
        elif (vidaIgualZero):
            palavraSecreta = palavraSecreta.capitalize()
            print(f"Fim de jogo! A forca está completa e o Adivinho perdeu. A palavra secreta era: {palavraSecreta}.")