'''# Vetor base para o ordenamento decrescente
import random
vet2D = [
         [5, 6, 4, 7, 5, 1, 7, 2, 6],
         [y for y in ["cabeça", "morango", "morango", "ovelha", "morango", "morango", "cabeça", "morango", "morango"]]   
        ]
print(vet2D)

for i in range(len(vet2D[0])):
    minValue = min(vet2D[0][i:])
    idmin = vet2D[0].index(minValue, i)
    if (vet2D[0][idmin] < vet2D[0][i]):
        vet2D[0][i], vet2D[0][idmin] = vet2D[0][idmin], vet2D[0][i]
        vet2D[1][i], vet2D[1][idmin] = vet2D[1][idmin], vet2D[1][i]

print(vet2D)


# Ordenamento lexográfico pós sorting geral
lenVectWord, currentWord = (len(vet2D[1]) - 1), 0
while (currentWord < lenVectWord):
    if (vet2D[0][currentWord] == vet2D[0][currentWord + 1]): # Verifica condição de empate entre pontuação
        findLowest, length, letter = False, min(len(vet2D[1][currentWord]), len(vet2D[1][currentWord+1])), 0 # Condição crescente de lexografia
        while (letter < length and not findLowest): # Varre as palavras
            if vet2D[1][currentWord][letter] > vet2D[1][currentWord + 1][letter]:
                findLowest, vet2D[1][currentWord], vet2D[1][currentWord + 1] = True, vet2D[1][currentWord + 1], vet2D[1][currentWord]
            letter += 1
    currentWord += 1

print(vet2D)
'''
a = ['a', 'b', "c"]
print(min(a[1:]))