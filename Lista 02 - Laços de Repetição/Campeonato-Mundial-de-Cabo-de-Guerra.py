# Variapveis da partida
quantidadePartidas, numPartida, quantidadeRodadas, = 0, 0, 0
pontosArthur, pontosJoao, venceuArthur, venceuJoao = 0, 0, False, False
# ---------------------
# Outputs iniciais
print(f"Começa agora o treinamento para grande final mundial de cabo de guerra!")
# ----------------
# Verifica paridade da quantidade de partidas
while (quantidadePartidas % 2 == 0):
    print(f"Não deverá haver empates! O número de partidas deverá ser ímpar.")
    quantidadePartidas  = int(input())
print(f"Eles batalharão em {quantidadePartidas} longas partidas.")
# ------------------------------------------
# Entrada de dados
forcaArthur, forcaJoao, resistencia  = int(input()), int(input), int(input())

while (quantidadePartidas > 0):
    # Variáveis de controle
    quantidadePartidas  -= 1
    numPartida          += 1

    # Outputs de início de partida
    print(f"Começa a {numPartida}ªpartida!\n"
        f"Placar geral: {pontosArthur} X {pontosJoao}")
    # ----------------------------

    numero  = int(input()) # Número que determina vencedor da rodada
    if (type(numero ** 0.5) is int):
        pontosArthur += 1
        venceuArthur = True
        print(f"O número é um quadrado perfeito! Arthur consegue puxar mais forte.")
    elif ():
        print(f"O primo do primo é primo do primo? João puxa mais forte!")
    else:
        maiorForca = max(forcaArthur, forcaJoao)
        if (maiorForca == forcaArthur):
            pontosArthur += 1
            venceuArthur = True
            print(f"Arthur é o mais forte! João não consegue segurar.")
        else:
            pontosJoao += 1
            venceuJoao = True
            print(f"João é o mais forte! Arthur não consegue segurar.")
    # ---------------------------- 
    # Outputs de fim de partida
    if (venceuArthur): print(f"Arthur dá orgulho para Maceió e ganha a partida!")
    elif (venceuJoao): print(f"João usa seus talentos de mangueboy e leva essa para casa!")

print(f"Agora eles estão prontos para o mundial!\n"
    f"Placar final: {pontosArthur} X {pontosJoao}")

print(f"{nome_perdedor} não teve chance! {nome_ganhador} venceu todas as partidas.")

print(f"O ganhador foi {nome_ganhador} com uma diferença de {diff_vitorias} partidas.")