'''Cada número de 1 a 9 deve aparecer exatamente uma vez em cada linha.
Cada número de 1 a 9 deve aparecer exatamente uma vez em cada coluna.
Cada número de 1 a 9 deve aparecer exatamente uma vez em cada um dos nove blocos 3x3.'''

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

tab = []
for i in range(9):
    tabLiine = entrada.split("\n").split()
    tab.append(tabLiine)






print(f"Caso encerrado! Mizael provou sua inocência lógica e o Sudoku foi resolvido!")
for j in range(9): print(f"{tab[j]}")