# Variapveis da partida
quantidadePartidas, numPartida = 0, 0
vitoriasArthur, vitoriasJoao, resistenciaArthur, resistenciaJoao = 0, 0, 0, 0
# ---------------------
# Outputs iniciais
print(f"Começa agora o treinamento para grande final mundial de cabo de guerra!")
# ----------------
# Verifica paridade da quantidade de partidas
quantidadePartidas  = int(input())
while (quantidadePartidas % 2 == 0):
    print(f"Não deverá haver empates! O número de partidas deverá ser ímpar.")
    quantidadePartidas  = int(input())
print(f"Eles batalharão em {quantidadePartidas} longas partidas.")
# ------------------------------------------
# Entrada de dados
forcaArthur, forcaJoao, resistencia = int(input()), int(input()), int(input())
# Condições de Rodada e de Partidas
resistenciaArthur, resistenciaJoao = resistencia, resistencia
#runPartida, runRodada   =   True, True
pararFlag   = False
for partida in range(quantidadePartidas):
    if (not pararFlag):
        # Variáveis de controle
        numPartida          += 1
        # Outputs de início de partida
        print(f"Começa a {numPartida}ª partida!\n"
            f"Placar geral: {vitoriasArthur} X {vitoriasJoao}")
        # ----------------------------
        #runRodada   = True
        while (not pararFlag):
            # Definindo vencedor
            numero  = int(input()) # Número que determina vencedor da rodada
            # Verifica se é primo
            isPrime =   True
            if (numero > 1):
                i   = 2
                while(i ** 2 <= numero):
                    if (numero % i == 0):
                        isPrime = False
                    i += 1
            else:
                isPrime = False
            # --------------
            if (numero % (numero ** 0.5) == 0 if (numero > 0) else 0):
                resistenciaArthur   += 1
                resistenciaJoao     -= 1
                print(f"O número é um quadrado perfeito! Arthur consegue puxar mais forte.")
            elif (isPrime):
                resistenciaJoao     += 1
                resistenciaArthur   -= 1
                print(f"O primo do primo é primo do primo? João puxa mais forte!")
            else:
                maiorForca = max(forcaArthur, forcaJoao)
                if (maiorForca == forcaArthur):
                    resistenciaArthur   += 1
                    resistenciaJoao     -= 1
                    print(f"Arthur é o mais forte! João não consegue segurar.")
                else:
                    resistenciaJoao     += 1
                    resistenciaArthur   -= 1
                    print(f"João é o mais forte! Arthur não consegue segurar.")
            # --------------------
            # ------------------------- 
            # Outputs de fim de partida
            if (resistenciaJoao == 0):
                vitoriasArthur += 1
                print(f"Arthur dá orgulho para Maceió e ganha a partida!")
                pararFlag   = True
                # runRodada, runPartida   = False, False
            elif (resistenciaArthur == 0):
                vitoriasJoao        += 1
                print(f"João usa seus talentos de mangueboy e leva essa para casa!")
                pararFlag   = True
                #runRodada, runPartida   = False, False
            # -----------------------
            if ((vitoriasJoao == ((quantidadePartidas//2) + 1) and vitoriasArthur == 0) or 
                (vitoriasJoao == 0  and vitoriasArthur == ((quantidadePartidas//2) + 1)) and 
                quantidadePartidas > 1):
                pararFlag   = True
                #runPartida  = False
    if (resistenciaArthur == 0 or resistenciaJoao == 0):
        resistenciaArthur, resistenciaJoao, pararFlag = resistencia, resistencia, False
        
# Output fim de todas as partidas
print(f"\nAgora eles estão prontos para o mundial!\n"
    f"Placar final: {vitoriasArthur} X {vitoriasJoao}")
# ------------------------------

# Verificando Vencedor
maiorPontuacao, menorPontuacao  = max(vitoriasArthur, vitoriasJoao), min(vitoriasArthur, vitoriasJoao)
vencedor    = "Arthur" if (maiorPontuacao == vitoriasArthur) else "João"
perdedor    = "Arthur" if (menorPontuacao == vitoriasArthur) else "João"
# --------------------

# Saída Final
if (menorPontuacao == 0): print(f"{perdedor} não teve chance! {vencedor} venceu todas as partidas.")
else: print(f"O ganhador foi {vencedor} com uma diferença de {maiorPontuacao - menorPontuacao} partidas.")
# -----------