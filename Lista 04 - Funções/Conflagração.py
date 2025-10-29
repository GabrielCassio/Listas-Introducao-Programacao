# Funções Obrigatórias
# Mudar essa função só para receber a posição do Sam
def DistChebyshev (position1: list, position2: list) -> list:
    result = 0
    indexChebyshev = [0] * 2
    matrixLength = len(position2)
    for i in range(matrixLength):   
        d1 = abs(position1[0] - position2[i][0])
        d2 = abs(position1[1] - position2[i][1])
        curDist = max(d1, d2)
        if (curDist >= result):
            result = curDist
            indexChebyshev = position2[i]
    return indexChebyshev

# Function Attack Sam
def SamAttack():
    # [name, damage, range]
    weapons = [["Espingarda", 25, 2], ["Rifle", [15, 5], 3], ["Metralhadora", 15, 4]]

# Teleport Function
def TpNeil():
    cordNeil = CordsCharacter("N")
    cordSam = CordsCharacter("S")
    # passar a referência das Listas para acesso rápido
    newCordNeil = DistChebyshev(cordSam, board)
    # Limpar antiga posição de Neil
    board[cordNeil[0]][cordNeil[1]] = "P"
    # Substitui Neil na nova posição 
    board[newCordNeil[0]][newCordNeil[1]] = "N"
    for i in range(6):
        print(" ".join(board))

# Other functions
def CordsCharacter(searchLetter: str) -> list:
    for i in range(6):
        for j in range(6):
            if (board[i][j] == searchLetter):
                return  [i, j] # Coordenadas do personagem em questão
            

def MovementSam(movLetter: str):
    cordSam = CordsCharacter("S")
    # Ao Sam tentar passar para um espaço instraponível ou para fora da matriz, ele deve permanecer no mesmo lugar.
    if (movLetter == "W"):
        if (cordSam[1]-1 > 0):
            if (board[cordSam[0]][cordSam[1]-1] != "I"):
                if (board[cordSam[0]][cordSam[1]-1] == "F"):
                    flames[1] += 1
                    flames[0] = True
                else: flames[0] = False
                board[cordSam[0]][cordSam[1]] = initialBoard[cordSam[0]][cordSam[1]]
                board[cordSam[0]][cordSam[1]-1] = "S"

    elif (movLetter == "A"):
        if (cordSam[0]-1 > 0):
            if (board[cordSam[0]-1][cordSam[1]] != "I"):
                if (board[cordSam[0]-1][cordSam[1]] == "F"):
                    flames[1] += 1
                    flames[0] = True
                else: flames[0] = False
                board[cordSam[0]][cordSam[1]] = initialBoard[cordSam[0]][cordSam[1]]
                board[cordSam[0]-1][cordSam[1]] = "S"
    elif (movLetter == "S"):
        if (cordSam[1]+1 > 5):
            if (board[cordSam[0]][cordSam[1]+1] != "I"):
                if (board[cordSam[0]][cordSam[1]+1] == "F"):
                    flames[1] += 1
                    flames[0] = True
                else: flames[0] = False
                board[cordSam[0]][cordSam[1]] = initialBoard[cordSam[0]][cordSam[1]]
                board[cordSam[0]][cordSam[1]+1] = "S"
    else:
        if (cordSam[0]+1 > 5):
            if (board[cordSam[0]+1][cordSam[1]] != "I"):
                if (board[cordSam[0]+1][cordSam[1]] == "F"):
                    flames[1] += 1
                    flames[0] = True
                else: flames[0] = False
                board[cordSam[0]][cordSam[1]] = initialBoard[cordSam[0]][cordSam[1]]
                board[cordSam[0]+1][cordSam[1]] = "S"


def main():
    # Output inicial do código
    print(f"Sam: Mas que lugar é esse aqui?\nDollman: WASD... Num exclusivo de PS5? Ah, fala sério!\n")
    # -------------------------
    totalDamNeil = 0
    numActions = 0
    stopEvents = False
    while (not stopEvents):
        weapons, indexWeapon = ["Espingarda", "Rifle", "Metralhadora"], -1
        movements = ["W", "A", "S", "D"]
        indexWeapon = -1

        sIn = input()
        # Verifica se a entrada é uma arma
        if (sIn in movements):
            MovementSam(sIn)
        elif (sIn in weapons): 
            print(f"Arma trocada para {sIn}")
            indexWeapon = weapons.index(sIn)
        else:
            SamAttack(indexWeapon)
        numActions += 1 # Incrementa a quantidade de ações realizadas

        if (flames[0]): lifes[0] -= 5

        if (numActions == 4):
            print(f">>> Você recebe um disparo de Neil! <<<")
            # Ataque de Neil
            lifes[0] -= 15
            totalDamNeil += 15
        
        if (lifes[0] <= 40 and not lifes[2]):
            lifes[2] = True
            print(f"Dollman: A Fragile comeu todos os criptobiontes da DHV Magalhães... Se curar não é uma opção. Tome cuidado, Sam.")

    
    if (lifes[1] == max(0, lifes[1])):
        # Ao final da missão retornar com o cálculo
        likes = 1000 - (totalDamNeil * 8) - (flames[1] * 10)
        print(f"\nMISSÃO COMPLETA! - Investigue a Anomalia\n========================================\nLikes recebidos: 👍 {likes}")
    else:
        print(f"\nMISSÃO FALHOU\n==============\nSam foi derrotado.\n[Sua alma vaga pela Emenda, buscando reencontrar seu corpo perdido...]")

# Main code ---------------------------------------------------------
# Declaração para acesso Global
board = [input().split() for x in range(6)] # Tabuleiro Inicial
initialBoard = board[:]
# Flames Properties
flames = [False, 0] # [stay on flames, quantity of hits in flames]
# Life List
lifes = [100, 100, False] # [LifeSam, LifeNeil, lifeSamLT40]

main()
