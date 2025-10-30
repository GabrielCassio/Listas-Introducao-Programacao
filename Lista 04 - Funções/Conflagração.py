# Funções Obrigatórias
# Mudar essa função só para receber a posição do Sam
def DistChebyshev (posSam: list, posNeil: list = [], typeFunction = True) -> list:
    '''
    typeFunction == True -> Casa mais distante de Sam
    typeFunction == False -> Distância entre Sam e Neil
    '''

    result = 0
    if (typeFunction):
        indexChebyshev = []
        boardPos = [[i, j] for i in range(6) for j in range(6)]
        matrixLength = len(boardPos)
        for i in range(matrixLength):   
            x, y = boardPos[i][0], boardPos[i][1]
            curDist = max(abs(posSam[0] - boardPos[i][0]), abs(posSam[1] - boardPos[i][1])) # Maior distância entre a casa atual em comparação e a posição de Sam
            if (curDist >= result and board[x][y] != "I" and board[x][y] != "N" and board[x][y] != "S"): result, indexChebyshev = curDist, boardPos[i]
        return indexChebyshev
    else:
        return max(abs(posSam[0] - posNeil[0]), abs(posSam[1] - posNeil[1]))

# Function Attack Sam
def SamAttack(sWeapon: str) -> int:
    cordSam = CordsCharacter("S")
    cordNeil = CordsCharacter("N")
    distBtwChac = DistChebyshev(cordSam, cordNeil, False)

    # Tipo da arma
    if (sWeapon == "Espingarda"):
        if (distBtwChac <= 2): 
            return 25
        else: return 0
    elif(sWeapon == "Rifle"):
        if (distBtwChac == 3): return 15
        else: return 5
    elif (sWeapon == "Metralhadora"):
        if (distBtwChac >= 4): return 15
        else: return 0

# Teleport Function
def TpNeil():
    cordNeil = CordsCharacter("N")
    x, y = cordNeil[0], cordNeil[1]
    cordSam = CordsCharacter("S")
    # Limpar antiga posição de Neil
    board[x][y] = "P"

    # passar a referência das Listas para acesso rápido
    newCordNeil = DistChebyshev(cordSam)
    x, y = newCordNeil[0], newCordNeil[1]
    # Substitui Neil na nova posição 
    board[x][y] = "N"

    for i in range(6):
        print(" ".join(board[i]))

# Other functions
def CordsCharacter(searchLetter: str) -> list:
    for i in range(6):
        for j in range(6):
            if (board[i][j] == searchLetter):
                return  [i, j] # Coordenadas do personagem em questão

# Movement Function
def MovementSam(movLetter: str, beforeState: str) -> str:
    cordSam = CordsCharacter("S")
    x, y = cordSam[0], cordSam[1]
    hdesloc, vdesloc = 0, 0 # Sentido de deslocamento
    if (movLetter == "W"): vdesloc = -1
    elif (movLetter == "A"): hdesloc = -1
    elif (movLetter == "S"): vdesloc = 1
    elif (movLetter == "D"): hdesloc = 1

    newX, newY = x + vdesloc, y + hdesloc
    # Ao Sam tentar passar para um espaço instraponível ou para fora da matriz, ele deve permanecer no mesmo lugar.
    if ((0 <= newX <= 5 and 0 <= newY <= 5) and (board[newX][newY] != "I")):
        newStateSam = board[newX][newY] # Guarda o estado da casa do próximo movimento
        if (newStateSam == "F"): flames[0] = True
        else: flames[0] = False
        # Exchange entre os estados das casas em que o Sam se movimenta
        board[x][y] = beforeState
        board[newX][newY] = "S"
        return newStateSam
    else: 
        return beforeState

def main():
    # Output inicial do código
    print(f"Sam: Mas que lugar é esse aqui?\nDollman: WASD... Num exclusivo de PS5? Ah, fala sério!\n")
    
    # Input lists of weapons and movements
    weapons, indexWeapon = ["Espingarda", "Rifle", "Metralhadora"], 1
    movements = ["W", "A", "S", "D"]
    beforeStateSam = "P"

    # Total de dano causado por Neil e as Instâncias de Dano Sofridas
    totalDamNeil = 0
    instDamNeil = 0

    numSamActions = 0
    stopGame = False
    while ((lifes[0] > 0 and lifes[1] > 0) and (not stopGame)):
        # Dano causado por Sam
        damageSam = 0

        # Entrada geral
        sIn = input()
        # Verifica se a entrada é um movimento
        if (sIn in movements): beforeStateSam = MovementSam(sIn, beforeStateSam)
        # Verifica se a entrada é uma arma
        elif (sIn in weapons): 
            print(f"Arma trocada para {sIn}.")
            indexWeapon = weapons.index(sIn)
        # Verifica se a entrada é a execução de um ataque
        else:
            # Cálculo do dano causado por Sam
            damageSam = SamAttack(weapons[indexWeapon]) 
        
        numSamActions += 1 # Incrementa a quantidade de ações realizadas

        if (damageSam > 0):
            # Decrementa a vida de Neil
            lifes[1] -= damageSam
            # Incrementa de instância sobre 
            instDamNeil += 1
            # Caso Neil perca, então o jogo terminará
            if (lifes[1] <= 0): stopGame = True
            
        if (not stopGame):
            if (numSamActions == 4):
                numSamActions = 0
                print(f">>> Você recebe um disparo de Neil! <<<")
                # Ataque de Neil
                lifes[0] -= 15
                totalDamNeil += 15
                if (lifes[0] <= 0): stopGame = True

            if (instDamNeil == 3): 
                instDamNeil = 0
                TpNeil() # Neil teleporta

            if (flames[0]):
                flames[1] += 1
                lifes[0] -= 5
                if (lifes[0] <= 0): stopGame = True

        if (not stopGame and lifes[0] <= 40 and not lifes[2]):
            lifes[2] = True
            print(f"Dollman: A Fragile comeu todos os criptobiontes da DHV Magalhães... Se curar não é uma opção. Tome cuidado, Sam.")
    
    if (lifes[1] <= 0):
        # Ao final da missão retornar com o cálculo
        likes = 1000 - (totalDamNeil * 8) - (flames[1] * 10)
        print(f"\nMISSÃO COMPLETA! - Investigue a Anomalia\n========================================\nLikes recebidos: 👍 {likes}")
    else:
        print(f"\nMISSÃO FALHOU\n==============\nSam foi derrotado.\n[Sua alma vaga pela Emenda, buscando reencontrar seu corpo perdido...]")

# Main code ---------------------------------------------------------
# Declaração para acesso Global
board = [input().split() for x in range(6)] # Tabuleiro Inicial
# Flames Properties
flames = [False, 0] # [stay on flames, quantity of hits in flames]
# Lifes List
lifes = [100, 100, False] # [LifeSam, LifeNeil, lifeSamLT40]

main()