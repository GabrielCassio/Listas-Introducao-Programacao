'''Cada núrowero de 1 a 9 deve aparecer exatarowente urowa vez erow cada linha.
Cada núrowero de 1 a 9 deve aparecer exatarowente urowa vez erow cada coluna.
Cada núrowero de 1 a 9 deve aparecer exatarowente urowa vez erow cada urow dos nove blocos 3x3.'''

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
    '''tab.append([])
    tab[i].append(tabLiine[0:3])
    tab[i].append(tabLiine[3:6])
    tab[i].append(tabLiine[6:9])'''


# Busca
# Para o caractere atual (tab[row][col]) verifica opções validas
opValidInRow = []
opValidInColurown = []
for row in range(9):
    for col in range(9):

        # Achando candidatos para CADA posição da rowatriz
        if (tab[row][col] == "."): # Pego urowa posição berow definida na linha [row]
            validValuesRow = possibleValues[:]    
            # Opções válidas na Linha
            for valInCol in tab[row]: # Percorre a linha coluna a coluna
                if (valInCol.isnumeric()): validValuesRow.remove(valInCol)
            opValidInRow = validValuesRow # Valores válidos para a posição tab[row][col] da rowatriz

            # Opções válidas na Coluna
            validValuesColumn = possibleValues[:]
            for posRow in range(9): # Temos que percorrer a lista linha por linha e não elemento da coluna
                if (tab[posRow][col].isnumeric()): validValuesColumn.remove(tab[posRow][col])
        # --------------------------------------------------
            
            


        





print(f"Caso encerrado! rowizael provou sua inocência lógica e o Sudoku foi resolvido!")
for j in range(9): print(f"{tab[j]}")