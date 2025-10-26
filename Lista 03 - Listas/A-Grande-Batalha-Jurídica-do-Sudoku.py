'''
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
# Uso da ideia das pilhas, base da recursão

possibleValues = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Criando rowatriz 9x9
tab = []
for i in range(9):
    tabLiine = input().split()
    tab.append(tabLiine)
# ----------------------------------------------------

# Armazenando casas em branco | Casas Problema
emptyBoxes, posEmptyBoxes = [], 0
for row in range(9):
    for col in range(9):
        if (tab[row][col] == '.'): 
            emptyBoxes.append([row, col])
#print(f"{emptyBoxes}")
# ----------------------------------------------------

finalMatrix = ""
stopGame = False
while (not stopGame):
    # Não verificar todos de uma vez
    solvingBox = emptyBoxes[posEmptyBoxes] # Posição do caixa vazia '.'
    curRow, curCol = solvingBox[0], solvingBox[1]
    finded = False # Estado em que se encontra um candidato válido

    # Validação dos possíveis valores e teste
    # Precisamos fazer uma comparação dinâmica
    # para os próximos elementos da pilha
    curValueInBox = 0
    if tab[curRow][curCol] == '.': curValueInBox = 1
    else: curValueInBox = int(tab[curRow][curCol]) + 1

    for curValue in range(curValueInBox, 10):
        isValid = True # Condição de validação do valor
        if (not finded):
            curValue = str(curValue)
            for cols in range(9): # Compara com os demais Elementos da Linha
                if ((tab[curRow][cols] == curValue) and (cols != curCol)):
                    isValid = False
            for rows in range(9): # Compara com os demais
                if ((tab[rows][curCol] == curValue) and (rows != curRow)):
                    isValid = False

            startSubGridRow = curRow - curRow%3
            startSubGridCol = curCol - curCol%3
            for subRow in range(startSubGridRow, startSubGridRow + 3):
                for subCol in range(startSubGridCol, startSubGridCol + 3):
                    if ((tab[subRow][subCol] == curValue) and ((subRow != curRow) or (subCol != curCol))):
                        isValid = False

            if (isValid): 
                tab[curRow][curCol] = curValue
                posEmptyBoxes += 1 # Avança na lista/pilha
                finded = True

    # O valor é válido?
    if (finded):
        if posEmptyBoxes == len(emptyBoxes): stopGame = True
    else:
        tab[curRow][curCol] = '.'
        posEmptyBoxes -= 1  

print(f"Caso encerrado! Mizael provou sua inocência lógica e o Sudoku foi resolvido!")
for i in range(9):
    finalMatrix += " ".join(tab[i])+"\n"
print(f"{finalMatrix}", end="")