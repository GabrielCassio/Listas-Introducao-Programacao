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

def SamAttack():
    # [name, damage, range]
    weapons = [["Espingarda", 25, 2], ["Rifle", [15, 5], 3], ["Metralhadora", 15, 4]]

def TpNeil():
    cordNeil = PosCharacter()
    # passar a referência das Listas para acesso rápido
    newCordNeil = DistChebyshev()
    # Limpar antiga posição de Neil

    # Substitui Neil na nova posição 
    board[newCordNeil[0]][newCordNeil[1]] = "N"
    for i in range(6):
        print(" ".join(board))

# Other functions
def PosCharacter() -> list:
    ...

def MovementSam(movLetter: str):
    cordSam = PosCharacter()
    if (movLetter == "W"):
        ...
    elif (movLetter == "A"):
        ...
    elif (movLetter == "S"):
        ...
    else:
        ...


def main():

    # Flames infos
    hitsFlames = 0
    # Sam também pode receber 5 de dano ao andar num espaço dominado por fogo.

    # Sam infos
    lifeSam = 100 
    posSam = []
    # Ao Sam tentar passar para um espaço instraponível ou para fora da matriz, ele deve permanecer no mesmo lugar.

    # Neil infos
    lifeNeil = 100 # Vida dos personagens
    damageNeil = 15
    totalDamNeil = 0
    # ele atirará com seu próprio rifle depois que Sam fizer 4 ações

    # Output inicial do código
    print(f"Sam: Mas que lugar é esse aqui?\nDollman: WASD... Num exclusivo de PS5? Ah, fala sério!\n")
    # -------------------------
    stopEvents = False
    while (not stopEvents):
        '''Type of Input
            - Movimento (W, A, S, D)
            - Troca de arma (Espingarda/Rifle/Metralhadora)
            - Atirar'''
        weapons, indexWeapon = ["Espingarda", "Rifle", "Metralhadora"], -1
        movements = ["W", "A", "S", "D"]

        sIn = input()
        # Verifica se a entrada é uma arma
        if (sIn in movements):
            MovementSam(sIn)
        elif (sIn in weapons): 
            print(f"Arma trocada para {sIn}")
            indexWeapon = weapons.index(sIn)
        else:
            SamAttack()

    
    if (lifeNeil == max(0, lifeNeil)):
        # Ao final da missão retornar com o cálculo
        likes = 1000 - (totalDamNeil * 8) - (hitsFlames * 10)
        print(f"\nMISSÃO COMPLETA! - Investigue a Anomalia\n========================================\nLikes recebidos: 👍 {likes}")
    else:
        print(f"\nMISSÃO FALHOU\n==============\nSam foi derrotado.\n[Sua alma vaga pela Emenda, buscando reencontrar seu corpo perdido...]")

# Main code
# Declaração para acesso Global
board = [input().split() for x in range(6)] # Tabuleiro Inicial

main()