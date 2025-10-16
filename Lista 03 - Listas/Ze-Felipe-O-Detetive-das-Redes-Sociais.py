# Output incial
print(f"Iniciando investigação... Zé Felipe está focado.")

pts = 0 # pontos de suspeita

q, i = int(input()), 0 # quantidade de eventos | variável de iteração
ens = 0 # número de encontros suspeitos
nac = 0 # número de álibes
lsev = [] # lista de eventos
stp = False # condição de parada da investigação

while ((not stp) and (i < q)):
    
    infev = input().split(" - ") # Recendo evento

    # Adicionando informações
    lsev.append([])
    lsev[i].append(infev[0]) # Adicionando sigla
    lsev[i].append(infev[1]) # Adicionando evento
    lsev[i].append(infev[2]) # Adicionando hora-inicio
    lsev[i].append(infev[3]) # Adicionando hora-fim

    lsev[i][2], lsev[i][3] = lsev[i][2].split(":"), lsev[i][3].split(":")
    lsev[i][2][0], lsev[i][2][1], lsev[i][3][0], lsev[i][3][1] = int(lsev[i][2][0]), int(lsev[i][2][1]), int(lsev[i][3][0]), int(lsev[i][3][1])
    print(f"{lsev}")
    # Ordenamento com BBsort
    llsev = len(lsev)
    if (llsev > 1): # caso exista mais que um elemento ordene o horário
        for i in range(llsev):
            for j in range(llsev - 1):
                if ((lsev[j][2][0] > lsev[j+1][2][0])): lsev[j], lsev[j+1] = lsev[j+1], lsev[j]
                elif ((lsev[j][2][0] == lsev[j+1][2][0]) and (lsev[j][2][1] > lsev[j+1][2][1])):
                    lsev[j], lsev[j+1] = lsev[j+1], lsev[j]
                elif (lsev[j][2][0] == lsev[j+1][2][0]): # caso o horário de início seja igual tanto em horas quanto em minutos verifuqe o horário de fim
                    if (lsev[j][3][0] > lsev[j+1][3][0]): lsev[j], lsev[j+1] = lsev[j+1], lsev[j]
                    elif ((lsev[j][3][0] == lsev[j+1][3][0]) and (lsev[j][3][1] > lsev[j+1][3][1])):
                        lsev[j], lsev[j+1] = lsev[j+1], lsev[j]

    # regra 0
    if (lsev[i][0] == "VJM"): stp, pts = True, 100
    i += 1 # Atulizando a variável de iteração

if (not stp):
    for i in range(len(lsev)):
        if ("V" == lsev[i][0]):
            ev = lsev[i][1]
            for j in range(len(lsev)):
                if("JM" == lsev[j][0] and (lsev[j][1] == ev) and ((60*lsev[i][2][0] < 60*lsev[j][3][0]) and (60*lsev[j][2][0] < 60*lsev[i][3][0]))):
                    ens += 1
                    pts += 35
                elif ("ZF" == lsev[j][0] and (lsev[j][1] == ev) and ((60*lsev[i][2][0] < 60*lsev[j][3][0]) and (60*lsev[j][2][0] < 60*lsev[i][3][0]))):
                    nac += 1
                    pts -= 20

    if pts < 0: pts = 0

    print(f"\n--- Linha do Tempo dos Eventos ---")
    for i in range(len(lsev)):
        nm = lsev[i][0]
        if (nm == "V"): nm = "Virgínia"
        elif (nm == "JM"): nm = "Jogador Misterioso"
        elif (nm == "ZF"): nm = "Zé Felipe"
        elif (nm == "VJM"): nm = "Virginia e Jogador Misterioso"
        print(f"{lsev[i][2][0]}:{lsev[i][2][1]:<02}-{lsev[i][3][0]}:{lsev[i][3][1]:<02}: {nm} - {lsev[i][1]}")

    print(f"\n--- Resumo da Análise ---")
    print(f"Encontros Suspeitos: {ens}\n"
        f"Álibis Confirmados: {nac}\n")

if (pts >= 100):
    print(f"TRAIÇÃO CONFIRMADA! Zé Felipe vai fazer uma música sobre isso.")
elif (70 <= pts <= 99):
    print(f"Nível de Suspeita: {pts} - MUITO SUSPEITO! Zé Felipe vai ter uma conversa séria com a Virgínia.")
elif (30 <= pts <= 69):
    print(f"Nível de Suspeita: {pts} - Hmmm, algo de estranho não está certo. Zé Felipe vai ficar de olho.")
elif (pts < 30):
    print(f"Nível de Suspeita: {pts} - Não há motivo para preocupação. Zé Felipe pode respirar aliviado e voltar a brincar com a Maria Flor.")