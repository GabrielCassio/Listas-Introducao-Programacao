# Este não código não possui minemonicidade
print(f"RECEBA! É hoje que eu me torno o melhor dos melhores.")
gke = ["Rokenedy", "IShowSpeed", "Sérgio Soares", "Neymar Jr", "Gabriel Vasconcelos"] # goleiros especiais
ntt, nta, strt = int(input()), 0, False # numero de treino | num treino atual | stop treinos
hi = int(input()) # habilidade inicial
if (0 <= hi <= 5): print(f"A gente tem que começar de algum lugar, né? RECEBA!")
elif (6 <= hi <= 15): print(f"Não tem jeito, vou ser o melhor do mundo!")
elif (hi >= 16): print(f"O Pai tá estourado! RECEBA!")

mt = (100 - hi) / ntt # meta de evolução por treino
print(f"Meta por Partida: {mt}")
sq = input().split("-")

while ((nta < ntt) and (not strt)): # rodada de treino
    
    pt = 0 # pontos da sessão
    vec, x, y, gol = [], 0, 0, False # vecay de batida | Coordenadas de batida | gol

    tb, gka, hgk = sq[2*nta], sq[2*nta+1], 0 # tipo de batida atual | goleiro atual
    print(f"TIPO DE PARTIDA: {tb}\n"
        f"Nome do Goleiro: {gka}")
    
    if (not gka in gke): hgk = int(input()) # habilidade do goleiro não especial
    if (tb == "Batida de Falta"):
        vec = eval(input()) # vetor 3x3
        x, y = int(input()), int(input())
    elif (tb == "Batida de Pênalti"):
        vec = eval(input()) # vetor 2x2
        x, y = int(input()), int(input())
    elif (tb == "Batida de Ataque"):
        vec = eval(input()) # vetor 5x5
        x, y = int(input()), int(input())
    
    gol = False
    if (vec[x][y] == 1): # Verifica se acertou a batida
        if (gka == "Rokenedy"):
            print(f"Aí não dá, impossível de fazer gol no maior do mundo.")
        elif (gka == "IShowSpeed"):
            gol = True
            pt += 1.5*mt
            print(f"REBECA? Is that you?\n"
                f"Ispidi mai friand, recieve!")
        elif (gka == "Sérgio Soares"):
            print(f"DALE DALE, PROFESSOR! Quero ver se esse tal de Python é bom mesmo…")
            if (tb == "Batida de Pênalti"):
                gol = True
                pt = mt
        elif (gka == "Neymar Jr"):
            gol = True
            print(f"Ele nem sabe agarrar! A arma dele é a sua fragilidade…")
            pt += mt/2
        elif (gka == "Gabriel Vasconcelos"):
            gol = True
            print(f"HAHAHA! Eu pedi um desafio, não uma barra sem goleiro…")
            pt += 2*mt
        else:
            gol = True
            if (hi > hgk): 
                pt += (hi - hgk)

    if (gol): print(f"RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
    else: print(f"A jornada ainda não acabou!")
    nta += 1
    hi += pt
    
    if (hi > 100): strt = True
    else:
        if (pt >= mt): 
            print(f"VAMO! PARTIDA {nta} DE {ntt}!")
        else: 
            print(f"Dá pra recuperar depois! Vamo seguindo!")

if (hi>100): 
    print(f"NÃO TEM JEITO! EU SEMPRE SOUBE QUE IA SER O MELHOR DO MUNDO! RECEBA!")
elif (hi == 100):
    print(f"O trono do futebol hoje tem dois reis. Eu e Pelé! Não podia estar com alguém melhor!")
else:
    print(f"Ano que vem tem InterCIn de novo! É só eu treinar mais…")