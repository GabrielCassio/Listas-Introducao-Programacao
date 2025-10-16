# Output incial
print(f"Iniciando investigação... Zé Felipe está focado.")

pts = 0 # pontos de suspeita

q, i = int(input()), 0 # quantidade de eventos | variável de iteração
ens = 0 # número de encontros suspeitos
nac = 0 # número de álibes
lsev = [] # lista de eventos
stp = False # condição de parada da investigação

while (i < q):
    
    infev = input().split(" - ") # Recendo evento
    # Aplicação da regra 0
    if (infev[0] == "VJM"): stp, pts = True, 100

    # Adicionando informações
    lsev.append([])
    lsev[i].append(infev[0]) # Adicionando sigla
    lsev[i].append(infev[1]) # Adicionando evento
    lsev[i].append(int(infev[2][:2])) # Adicionando hora-inicio
    lsev[i].append(int(infev[3][:2])) # Adicionando hora-fim

    i += 1 # Atulizando a variável de iteração

if (not stp):
    # Ordenamento com BBsort
    llsev = len(lsev)
    for i in range(llsev):
        for j in range(llsev - 1):
            if ((lsev[j][2] > lsev[j+1][2])): 
                lsev[j], lsev[j+1] = lsev[j+1], lsev[j]
            elif ((lsev[j][2] == lsev[j+1][2])):  #and (lsev[j][2][2] > lsev[j+1][2][2])):
                if (lsev[j][3] > lsev[j+1][3]):
                    lsev[j], lsev[j+1] = lsev[j+1], lsev[j]

    for i in range(llsev):
        for j in range(i + 1, llsev):
            sgs = [lsev[i][0], lsev[j][0]]
            if ((lsev[i][2] < lsev[j][3]) and (lsev[j][2] < lsev[i][3]) and
                (lsev[i][1] == lsev[j][1])):
                if ("V" in sgs and "JM" in sgs):
                    ens += 1
                    pts += 35
                elif ("V" in sgs and "ZF" in sgs):
                    nac += 1
                    pts -= 20
                    if (pts < 0): pts = 0

    print(f"\n--- Linha do Tempo dos Eventos ---")
    for i in range(llsev):
        nm = lsev[i][0]
        if (nm == "V"): nm = "Virgínia"
        elif (nm == "JM"): nm = "Jogador Misterioso"
        elif (nm == "ZF"): nm = "Zé Felipe"
        elif (nm == "VJM"): nm = "Virginia e Jogador Misterioso"
        print(f"{lsev[i][2]}:00-{lsev[i][3]}:00: {nm} - {lsev[i][1]}")

    print(f"\n--- Resumo da Análise ---")
    print(f"Encontros Suspeitos: {ens}\n"
        f"Álibis Confirmados: {nac}")

if (pts >= 100):
    print(f"\nTRAIÇÃO CONFIRMADA! Zé Felipe vai fazer uma música sobre isso.")
elif (70 <= pts <= 99):
    print(f"\nNível de Suspeita: {pts} - MUITO SUSPEITO! Zé Felipe vai ter uma conversa séria com a Virgínia.")
elif (30 <= pts <= 69):
    print(f"\nNível de Suspeita: {pts} - Hmmm, algo de estranho não está certo. Zé Felipe vai ficar de olho.")
elif (pts < 30):
    print(f"\nNível de Suspeita: {pts} - Não há motivo para preocupação. Zé Felipe pode respirar aliviado e voltar a brincar com a Maria Flor.")