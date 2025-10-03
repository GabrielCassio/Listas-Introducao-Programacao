## Variáveis da brincadeira
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
    # Mostra o resultado de cada criança
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
    # -----------------------------
# Verifica o vencedor
if (numVencedores == 1):
    print(f"O vencedor é {nomesVencedores}!")
elif (numVencedores >= 2):
    # Define os vencedores
    vencedor1, vencedor2, vencedor3, vencedor4 = "", "", "", ""
    # Define a ordem dos vencedores
    # Ana
    if ("Ana" in nomesVencedores): vencedor1 = "Ana"
    # Adrieli
    if ("Adrieli" in nomesVencedores and
        not "Ana" in nomesVencedores): vencedor1 = "Adrieli"
    else: vencedor2 = "Adrieli"
    # Joab
    if ("Joab" in nomesVencedores and
        not "Ana" in nomesVencedores and
        not "Adrieli" in nomesVencedores): vencedor1 = "Joab"
    elif ("Joab" in nomesVencedores and
        not "Ana" in nomesVencedores): vencedor2 = "Joab"
    else: vencedor3 = "Joab"
    # Duda
    if ("Duda" in nomesVencedores and 
        not "Ana" in nomesVencedores and
        not "Adrieli" in nomesVencedores and 
        not "Joab" in nomesVencedores): vencedor1 = "Duda"
    elif ("Duda" in nomesVencedores and 
        not "Ana" in nomesVencedores and
        not "Adrieli" in nomesVencedores): vencedor2 = "Duda" 
    elif ("Duda" in nomesVencedores and
        not "Ana" in nomesVencedores): vencedor3 = "Duda"
    else: vencedor4 = "Duda"
    # ------------------------------
    # Mostra os vencedores
    if (numVencedores == 2):
        print(f"Houve empate entre: {vencedor1}, {vencedor2}")
    elif (numVencedores == 3):
        print(f"Houve empate entre: {vencedor1}, {vencedor2}, {vencedor3}")
    elif (numVencedores == 4):
        print(f"Houve empate entre: {vencedor1}, {vencedor2}, {vencedor3}, {vencedor4}")
    # -------------------