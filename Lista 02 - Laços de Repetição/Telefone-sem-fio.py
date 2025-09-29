# Variáveis de Inicialização
n, refPalavra, anteriorPalavra = int(input()), "", "" # Número de participantes, Palavra de referência, Palavra anterior
numPalavrasErradas, errou5  = 0, False # Número de vezes que falaram uma palavra errada, Estado de se errou 5
nomeErrou1, palavraErrou1, nomeErrou2 = "", "", ""
# --------------------------

# Outputs iniciais
print(f"Vai começar a brincadeira! Será que a palavra vai ficar igual até o fim?")
# ----------------

#  Variáveis de loop
for estudante in range(n):
    # Inputs para cada Estudante
    nomeParticipante    = input()
    palavraFalada       = input()
    # -------------------------

    if (estudante == 0): refPalavra    = palavraFalada # A primeira palavra é a de referência

    # Verifica se alguém falou uma palavra errada
    if (palavraFalada != anteriorPalavra and anteriorPalavra != ""):
        numPalavrasErradas += 1
        # Seleciona os 2 primeiros estuantes que erraram a palavra
        if (nomeErrou1 == ""):
            nomeErrou1      = nomeParticipante
            palavraErrou1   = palavraFalada
        elif (nomeErrou2 == ""):
            nomeErrou2      = nomeParticipante
        # --------------------------------------
        print(f"Parece que {nomeParticipante} não conseguiu ouvir muito bem e acabou passando pra frente uma palavra diferente da que escutou…")
    # ------------------------------------------

    anteriorPalavra = palavraFalada
    
    # Verifica se a palavra foi errada 5 vezes
    if (numPalavrasErradas == 5 and not errou5):
        errou5  = True
        print(f"Caramba, que confusão! A palavra {refPalavra} já tá toda embaralhada e virou {palavraFalada}!")
    # ------------------------------------------

# Verifica se a palavra de saída foi a mesma da entrada
if (refPalavra == anteriorPalavra and numPalavrasErradas == 0):
    print(f"Impressionante, todos os jogadores ouviram e falaram perfeitamente a palavra {refPalavra}! Talvez os telefones modernos comecem a perder espaço pra moda antiga.")
elif (refPalavra == anteriorPalavra and numPalavrasErradas != 0):
    print(f"Parece que ocorreram {numPalavrasErradas} trocas durante o processo, mas mesmo com essa pequena confusão, a palavra {refPalavra} conseguiu chegar no fim do telefone sem fio.")

# ------------------------------------------------------

# Verifica se saída não foi mesmo do que a entrada
if (refPalavra != anteriorPalavra and numPalavrasErradas == 1):
    print(f"Poxa, foi por pouco, só quem errou foi {nomeErrou1} que disse {palavraErrou1} ao invés de {refPalavra}…")
elif (refPalavra != anteriorPalavra and numPalavrasErradas == 2):
    print(f"Se não fosse pelos erros de {nomeErrou1} e {nomeErrou2} a palavra {refPalavra} poderia ter chegado até o fim, talvez eles devessem tentar de novo.")
elif (refPalavra != anteriorPalavra and numPalavrasErradas > 2):
    print(f"É, parece que os alunos se confundiram bastante durante a brincadeira e a palavra {refPalavra} acabou virando {anteriorPalavra}. No total, ocorreram {numPalavrasErradas} trocas.")
# ------------------------------------------------