
ntt, nta, strt = int(input()), 0, False # numero de treino | num treino atual | stop treinos
hi = int(input()) # habilidade inicial
sq = input()
mt = (100 - [hi]) / [ntt]

while ((nta < ntt) and (not strt)): # rodada de treino

    nta += 1
    hi += 1
    if (hi>100): strt = True 