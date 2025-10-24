entrada = '''
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
'''

possibleValues = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Criando rowatriz 9x9
tab = []
for i in range(9):
    tabLiine = input().split()
    tab.append(tabLiine)
# ----------------------------------------------------------------------------

# Busca
# Opções válidas
opValidInRow = [] # Para Linha
opValidInColumn = [] # Para Coluna
opValidInGrid3x3 = [] # Para subGrid
# Intersecção das opções
candidates = []
#Matrix de saída
finalMatrix = ""

# Mexendo com MapStack
mapStack = [
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
]
choiceStack = []

'''finishedRows = 0
if (not '.' in tab[row]):  finishedRows += 1'''
stopGame = False
while (not stopGame):
#for i in range(1):
    for row in range(9):
        if (not stopGame):
            for col in range(9):
                # Achando candidatos para CADA posição da matriz
                if (tab[row][col] == "."): # Pego cada posição bem definida na linha [row]
                    validValuesRow = possibleValues[:]   
                    # Opções válidas na Linha
                    for valInCol in tab[row]: # Percorre a linha coluna a coluna
                        if ((valInCol != '.' ) and (valInCol in validValuesRow)): validValuesRow.remove(valInCol)
                    opValidInRow = validValuesRow # Valores válidos para a posição tab[row][col] da rowatriz

                    # Opções válidas na Coluna
                    validValuesColumn = possibleValues[:]
                    for posRow in range(9): # Temos que percorrer a lista linha por linha e não elemento da coluna
                        valInRow = tab[posRow][col]
                        if ((valInRow != '.') and (valInRow in validValuesColumn)): validValuesColumn.remove(valInRow)
                    opValidInColumn = validValuesColumn

                    # Opções válidas no subGrid 3x3
                    # Em qual grid
                    subGrid = [] # [nLinhas, nColunas]
                    if ((row//3 < 1) and (col//3 < 1)): subGrid = [range(0,3), range(0, 3)]
                    elif ((row//3 < 1) and (col//3 < 2)): subGrid = [range(0, 3), range(3, 6)]
                    elif ((row//3 < 1) and (col//3 < 3)): subGrid = [range(0, 3), range(6, 9)]
                    elif ((row//3 < 2) and (col//3 < 1)): subGrid = [range(3, 6), range(0, 3)]
                    elif ((row//3 < 2) and (col//3 < 2)): subGrid = [range(3, 6), range(3, 6)]
                    elif ((row//3 < 2) and (col//3 < 3)): subGrid = [range(3, 6), range(6, 9)]
                    elif ((row//3 < 3) and (col//3 < 1)): subGrid = [range(6, 9), range(0, 3)]
                    elif ((row//3 < 3) and (col//3 < 2)): subGrid = [range(6, 9), range(3, 6)]
                    elif ((row//3 < 3) and (col//3 < 3)): subGrid = [range(6, 9), range(6, 9)]


                    validValues3x3 = possibleValues[:] 
                    for gridRow in subGrid[0]:
                        for gridCol in subGrid[1]:
                            valInGrid = tab[gridRow][gridCol]
                            if ((valInGrid != '.')): validValues3x3.remove(valInGrid)       
                    opValidInGrid3x3 = validValues3x3             
                
                    # Posso pegar qualquer lista para iterar e pegar a intersecção dos conjuntos
                    validating = []
                    for num in opValidInRow:
                        if ((num in opValidInColumn) and (num in opValidInGrid3x3)):
                            validating.append(num)
                    candidates = validating[:]
                    # --------------------------------------------------

                    # Validação de Escolha
                    # Armazenando casos válidos
                    if (len(candidates) > 0): 
                        mapStack[row][col] = candidates          
                        tab[row][col] = mapStack[row][col].pop(0)
                    elif (len(candidates) == 0):
                        print(f"Chegamos ao ponto de que a posição ({row},{col}) não possui casos possíveis para exchange")
                        stopGame = True
                
    # Vendo as possibilidades mapeadas
    print(f"----- mapStack -----")
    for i in range(9):
        print(f"{mapStack[i]}")
    print()

    # Verificando conclusão do Sudoku
    primeMatrix = ""
    for length in range(9):
        primeMatrix += " ".join(tab[length])+"\n"
    print(f"{primeMatrix}") # Retirar depois
    if (not '.' in primeMatrix): 
        stopGame, finalMatrix  = True, primeMatrix
    # -------------------------------

print(f"Caso encerrado! Mizael provou sua inocência lógica e o Sudoku foi resolvido!")
print(f"{finalMatrix}", end="")


# Validação dos candidatos - Caso Determinístico
# if (len(candidates) == 1): tab[row][col] = candidates[0]
# ------------------------------------