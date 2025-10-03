# Variáveis do Advinho
# Número de Vidas | Tentativa de Letra
numLifeSoothsayer, letterAttempt   = 6, ""
# Variáveis do Desafiante
# Palavra Secreta | Palavra fantasma
secretWord, ghostWord   = "", ""

# Número Rodadas | Rodada Atual
numRounds, currentRound   = int(input()), 0
# Condições de Parada


# Output inicial do jogo
print(f"Que comece o jogo! Adivinhe a palavra, mas cuidado para não cair na armadilha.")






while ((currentRound < numRounds) and (numLifeSoothsayer > 0)):
    numLifeSoothsayer  = 6
    # Início da rodada 
    currentRound += 1
    print(f"Rodada {currentRound}/{numRounds}:")

    # Parte do Desafiante --------------------
    secretWord, ghostWord, numLettersComun, newGhostWord, wordsInRules, repeatedLetters  = input().lower(), input().lower(), 0, False, False, ""
    lengthSecretWord, lengthGhostWord = len(secretWord), len(ghostWord)
    

    while (not wordsInRules):
        # Iníco da parte dos Desafiantes
        for ghostLetter in ghostWord:
            if ((ghostLetter in secretWord) and (not ghostLetter in repeatedLetters)):
                numLettersComun += 1
                repeatedLetters += ghostLetter
        if (numLettersComun >= 3 or ghostWord == secretWord):
            print(f"A palavra fantasma possui {numLettersComun} letras presentes na palavra secreta. Tente uma com menos de 3 letras iguais.")
            ghostWord, numLettersComun, repeatedLetters    = input().lower(), 0, ""
        else: wordsInRules, numLettersComun = True, 0
        # Fim da parte do Desafiante ------------

    # Formatação de Outputs
    outWord, outAttempts = "", ""
    for caractere in range(lengthSecretWord): 
        outWord += "_"
        if (not caractere + 1 == lengthSecretWord): outWord += " "
    print(f"Palavra: {outWord}")


    # Parte do Adivinho ---------------------
    lettersInRound, numAttempts, hitedAll  = "", 0, False

    while ((numLifeSoothsayer > 0) and not hitedAll):
        letterAttempt, posSecretLetter, newWord   = input().lower(), 0, ""

        # Verifica se a Letra é repetida
        if (letterAttempt in lettersInRound):
            # Caso repetida possui apenas a seguinte saída
            print(f"Você já tentou a letra '{letterAttempt}'. Tente outra.")
        # Fim da verificação -----------------------
        else:
            numAttempts     += 1
            lettersInRound  += letterAttempt
            hitedLetter     = False
            # Caso não seja repetida -----------
            if (letterAttempt in secretWord):
                # Adiciona a letra à saída
                for letra in secretWord:
                    posSecretLetter += 1
                    if (letterAttempt == letra):
                        indexSubstituir = 0
                        for caractere in outWord:
                            indexSubstituir += 1
                            if ((2 * posSecretLetter - 1)   == indexSubstituir):
                                newWord += f"{letterAttempt}"
                            else:
                                newWord += f"{caractere}"
                        outWord, newWord = newWord, ""
                # ------------------------------------
                print(f"Boa! A letra '{letterAttempt}' está na palavra.")
                # Verifica se acertou todas
                if (not "_" in outWord):
                    hitedAll = True
                    secretWord = secretWord.capitalize()
                    print(f"Parabéns, Adivinho! Você descobriu a palavra secreta: {secretWord}.\n"
                            f"Total de tentativas: {numAttempts}")
                # ------------------------------------
            
            elif ((not letterAttempt in secretWord) and (not letterAttempt in ghostWord)):
                numLifeSoothsayer   -= 1
                print(f"Naao! A letra '{letterAttempt}' não está na palavra. Você perdeu 1 vida.")
                if (numLifeSoothsayer == 0):
                    secretWord = secretWord.capitalize()
                    print(f"Fim de jogo! A forca está completa e o Adivinho perdeu. A palavra secreta era: {secretWord}.")
            elif ((not letterAttempt in secretWord) and (letterAttempt in ghostWord)):
                numLifeSoothsayer   -= 2
                print(f"CUIDADO! A letra '{letterAttempt}' é uma armadilha! Você perdeu 2 vidas.")
                if (numLifeSoothsayer == 0):
                    secretWord = secretWord.capitalize()
                    print(f"Fim de jogo! A forca está completa e o Adivinho perdeu. A palavra secreta era: {secretWord}.")
            # ------------------------------
            # Se ele erra, automaticamente hitedLetter é falso
            # Verifica se o usuário acertou a letra
            if (numLifeSoothsayer > 0):
                if (not letterAttempt in outAttempts):
                    if (outAttempts == ""): outAttempts += letterAttempt
                    else: outAttempts += f", {letterAttempt}"

                # Saída para quando não se acerta todas as letras ou zera a vida
                if ((not hitedAll)):
                    print(f"=====================\n"
                        f"Palavra: {outWord}\n"
                        f"Vidas restantes: {numLifeSoothsayer}\n"
                        f"Letras chutadas: {outAttempts}\n"
                        f"=====================")
    # Fim da parte do Adivinho --------------