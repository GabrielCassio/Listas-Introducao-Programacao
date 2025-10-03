# Número de Vidas | Tentativa de Letra
numLifeSoothsayer = 6

# Palavra Secreta | Palavra fantasma
secretWord, ghostWord = "", ""

# Número Rodadas | Rodada Atual
numRounds, currentRound = int(input()), 0

# Output inicial do jogo
print(f"Que comece o jogo! Adivinhe a palavra, mas cuidado para não cair na armadilha.")

while ((currentRound < numRounds)):
    # Início da rodada -----------------------
    # Reset da Vida
    numLifeSoothsayer   = 6
    # Incrementa a ordinalidade da rodada atual
    currentRound        += 1
    # Imprime a relação da rodada atual
    print(f"Rodada {currentRound}/{numRounds}:")

    # Reset Palavra Secreta | Reset Palavra Fantasma |  Quantidade de Letras Comuns | Letras Repitidas
    secretWord, ghostWord, numLettersComun, repeatedLetters = input().lower(), input().lower(), 0, ""
    # Tamanho da Palavra Secreta | Tamanho da Palavra Fantasma 
    lengthSecretWord, lengthGhostWord = len(secretWord), len(ghostWord)

    # A nova palavra fantasma está dentro das regras
    wordsInRules    = False
    while (not wordsInRules):
        # Iníco da parte dos Desafiantes
        for ghostLetter in ghostWord:
            if ((ghostLetter in secretWord) and (not ghostLetter in repeatedLetters)):
                numLettersComun += 1
                repeatedLetters += ghostLetter
        if (numLettersComun >= 3):
            print(f"A palavra fantasma possui {numLettersComun} letras presentes na palavra secreta. Tente uma com menos de 3 letras iguais.")
            ghostWord, numLettersComun, repeatedLetters    = input().lower(), 0, ""
        else: wordsInRules, numLettersComun = True, 0

    # Formatação de Outputs
    outWord, outAttempts = "", ""
    for index in range(lengthSecretWord): 
        outWord += "_"
        if (not (index + 1) == lengthSecretWord): outWord += " "
    # Imprime o tamanho ad Palavra em formato de forca
    print(f"Palavra: {outWord}")

    # Letras Usadas | Número de tentativas | Condição de Acertou Todas
    lettersInRound, numAttempts, hitedAll  = "", 0, False

    while ((numLifeSoothsayer > 0) and not hitedAll):
        # Letra Utilizada
        letterAttempt = input().lower()

        # Verifica se a Letra é repetida
        if (letterAttempt in lettersInRound):
            # Caso repetida possui apenas a seguinte saída
            print(f"Você já tentou a letra '{letterAttempt}'. Tente outra.")
        # Fim da verificação -----------------------
        else:
             # Caso não seja repetida -----------
            numAttempts     += 1
            lettersInRound  += letterAttempt

            if (letterAttempt in secretWord):
                # Posição de cada Letra na Palavra Secreta | Nova Palavra de saída
                posSecretLetter, newWord = 0, ""
                if (letterAttempt in secretWord):
                    for letra in secretWord: # Adiciona a letra à saída
                        posSecretLetter += 1
                        if (letterAttempt == letra):
                            indexSubstituir = 0
                            for caractere in outWord:
                                indexSubstituir += 1
                                if ((2 * posSecretLetter - 1) == indexSubstituir): newWord += f"{letterAttempt}"
                                else: newWord += f"{caractere}"
                            # Armazenando Nova palavra na saída global | resetando variável newWord
                            outWord, newWord = newWord, ""

                    # Imprime a saída de acerto para nova palavra
                    print(f"Boa! A letra '{letterAttempt}' está na palavra.")

                    # Verifica se acertou todas
                    if (not "_" in outWord):
                        # Ativa flag de acertou de todas
                        hitedAll = True
                        secretWord = secretWord.capitalize()
                        print(f"Parabéns, Adivinho! Você descobriu a palavra secreta: {secretWord}.\n"
                                f"Total de tentativas: {numAttempts}")

            elif ((not letterAttempt in secretWord) and (not letterAttempt in ghostWord)):
                numLifeSoothsayer   -= 1
                print(f"Naao! A letra '{letterAttempt}' não está na palavra. Você perdeu 1 vida.")
                if (numLifeSoothsayer <= 0):
                    secretWord = secretWord.capitalize()
                    print(f"Fim de jogo! A forca está completa e o Adivinho perdeu. A palavra secreta era: {secretWord}.")
            elif ((not letterAttempt in secretWord) and (letterAttempt in ghostWord)):
                numLifeSoothsayer   -= 2
                print(f"CUIDADO! A letra '{letterAttempt}' é uma armadilha! Você perdeu 2 vidas.")
                if (numLifeSoothsayer <= 0):
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