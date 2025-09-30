# Ordem da Amarelinha 1 -> 2 -> 3 -> 4 -> 5 |  Ana, Adrieli, Joab e Duda | podem errar ao tentar pular para a próxima casa (perder o equilíbrio ou pisar fora da linha)
# Variáveis da brincadeira
n   = int(input()) # Número de tentativas registrado por jogador
n1, n2, n3, n4 = 0, 0, 0, 0 # Última casa alcançada na última tentiva
nomesVencedores, numVencedores  = "", 0
# -----------------------

# Verifica a rodada de cada criança
for crianca in range(4):
    # Tentativas
    for tentativas in range(n):
        numCasas  = int(input())    # Número de cassa alcançadas a cada tentativa
        # Recebe a última casa alcançada a cada tentiva de cada criança
        if (tentativas + 1 == n and crianca == 0): n1 = numCasas
        elif (tentativas + 1 == n and crianca == 1): n2 = numCasas
        elif (tentativas + 1 == n and crianca == 2): n3 = numCasas
        elif (tentativas + 1 == n and crianca == 3): n4 = numCasas 
        # -------------------------------------------------------------

    if (crianca == 0): 
        print(f"Ana tentou {n} vezes e completou a última casa {n1}")
        if (n1 == 5): 
            nomesVencedores += "Ana"
            numVencedores   += 1
            print(f"Ana completou a amarelinha!")
        else: print(f"Ana não conseguiu completar a amarelinha!")
    elif (crianca == 1): 
        print(f"Adrieli tentou {n} vezes e completou a última casa {n2}")
        if (n2 == 5): 
            nomesVencedores += "Adrieli"
            numVencedores   += 1
            print(f"Adrieli completou a amarelinha!")
        else: print(f"Adrieli não conseguiu completar a amarelinha!")
    elif (crianca == 2): 
        print(f"Joab tentou {n} vezes e completou a última casa {n3}")
        if (n3 == 5): 
            nomesVencedores += "Joab"
            numVencedores   += 1
            print(f"Joab completou a amarelinha!")
        else: print(f"Joab não conseguiu completar a amarelinha!")
    elif (crianca == 3): 
        print(f"Duda tentou {n} vezes e completou a última casa {n4}")
        if (n4 == 5):
            nomesVencedores += "Duda"
            numVencedores   += 1
            print(f"Duda completou a amarelinha!")
        else: print(f"Duda não conseguiu completar a amarelinha!")

if (numVencedores == 1):
    print(f"O vencedor é {nomesVencedores}!")
elif (numVencedores >= 2):
    
    if ("Ana" in nomesVencedores): 
    if ("Adrieli" in nomesVencedores): 
    if ("Joab" in nomesVencedores): 
    if ("Duda" in nomesVencedores):

    if (numVencedores == 2):
        vencedor1, vencedor2    = "", ""
        print(f"")
    elif (numVencedores == 3):
        print(f"")
    elif (numVencedores == 4):
        print(f"")
    