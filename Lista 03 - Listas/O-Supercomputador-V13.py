cps = []
qcps = []

np  = input() # nome do projeto
if (np == "Memória ROM Simples"): 
    cps = ["Redstone", "Repetidores", "Tochas de Redstone"]
    qcps = [256, 64, 128]
elif (np == "Calculadora de 4 bits"):
    cps = ["Redstone", "Repetidores",  "Blocos de Notas", "Observadores"]
    qcps = [1024, 256, 64, 128]
elif (np == "Sequenciador Musical"):
    cps = ["Redstone",  "Repetidores",  "Lâmpadas de Redstone", "Pistões Aderentes"]
    qcps = [4096, 1024, 2048, 512]
elif (np == "Processador de 8 Bits"):
    cps = [ "Redstone",  "Repetidores",  "Comparadores",  "Pistões"]
    qcps = [2048, 512, 256, 128]
elif (np == "Supercomputador V13"):
    cps = ["Redstone",  "Repetidores",  "Comparadores",  "Pistões Aderentes"]
    qcps = [8192, 2048, 1024, 1024]


ctr = False # construir?
cpj, ncpj, qcpj = [], [], [] # componentes do projeto | quantidades dos componentes do projeto
while (not ctr):
    cps = input()
    if (cps == "Construir!"): 
        cps = cps.split(" ") # componentes do projeto
        qcps, nmcps = int(cps[-1]), " ".join(cps[0:-1])
        ncpj.append(nmcps)
        ctr = True
        
        print()
    else:
        cps = cps.split(" ") # componentes do projeto
        qcps, nmcps = int(cps[-1]), " ".join(cps[0:-1])
        cpj.append(nmcps)
        qcpj.append(qcps)
        if ((not nmcps in cps[0])):
            print(f"Hmm, {nmcps} não parece ser útil para este projeto.")
        elif(nmcps == "Redstone"):
            print(f"Mais redstone! A energia que move o progresso! (+{qcps} Redstone)")
        elif(nmcps == "Repetidores"):
            print(f"Repetidores para garantir que o sinal chegue longe! Perfeito! (+{qcps} Repetidores)")
        elif(nmcps == "Tochas de Redstone"):
            print(f"Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{qcps} Tochas de Redstone)")
        elif(nmcps == "Lâmpadas de Redstone"):
            print(f"Lâmpadas para o display! O resultado vai ficar bem visível. (+{qcps} Lâmpadas de Redstone)")
        elif(nmcps == "Blocos de Notas"):
            print(f"Blocos de Notas! Quem sabe não rola uma musiquinha no final? (+{qcps} Blocos de Notas)")
        elif(nmcps == "Observadores"):
            print(f"Observadores a postos! Nenhuma atualização de bloco passará despercebida. (+{qcps} Observadores)")
        elif(nmcps == "Pistões"):
            print(f"Pistões para mover as coisas de lugar. Isso vai ser útil! (+{qcps} Pistões)")
        elif(nmcps == " Pistões Aderentes"):
            print(f"Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{qcps} Pistões Aderentes)")

if (qcpj == qcps):
    print(f"Viniccius13 conseguiu construir o {np}! Partiu programar!\n\n")