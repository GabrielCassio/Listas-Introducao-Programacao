# Other functions
def CordsCharacter(searchLetter: str) -> list:
    for i in range(6):
        for j in range(6):
            if (board[i][j] == searchLetter):
                return  [i, j] # Coordenadas do personagem em questã
            
board = [input().split() for x in range(6)] # Tabuleiro Inicial

print(CordsCharacter("S"))