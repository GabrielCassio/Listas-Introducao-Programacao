componentes, quantCompsProj = [], []

nameProject  = input() # nome do projeto
if (nameProject == "Memória ROM Simples"): 
    componentes = ["Redstone", "Repetidores", "Tochas de Redstone"]
    quantCompsProj = [256, 64, 128]
elif (nameProject == "Calculadora de 4 bits"):
    componentes = ["Redstone", "Repetidores",  "Tochas de Redstone", "Lâmpadas de Redstone"]
    quantCompsProj = [512, 128, 64, 256]
elif (nameProject == "Sequenciador Musical"):
    componentes = ["Redstone",  "Repetidores",  "Blocos de Notas", "Observadores"]
    quantCompsProj = [1024, 256, 64, 128]
elif (nameProject == "Processador de 8 Bits"):
    componentes = [ "Redstone",  "Repetidores",  "Lâmpadas de Redstone",  "Pistões Aderentes"]
    quantCompsProj = [4096, 1024, 2048, 512]
elif(nameProject == "Display de Vídeo 8x8"):
    componentes = ["Redstone", "Repetidores", "Comparadores", "Pistões"]
    quantCompsProj = [2048, 512, 256, 128]
elif (nameProject == "Supercomputador V13"):
    componentes = ["Redstone",  "Repetidores",  "Comparadores",  "Pistões Aderentes"]
    quantCompsProj = [8192, 2048, 1024, 1024]

numComProj = len(componentes) # Tamanho da lista de componentes do projeto
constrStop, computingStop = False, False #  Condicionais de Parada

nomeCompNotIn, quantCompNotIn = [], [] # Componentes não úteis
nomeCompIn, quantCompIn = [], [] # Componentes úteis

while (not computingStop):
    if (not constrStop):
        compIn = input() # Recebe a entrada dos componentes
        if (compIn == "Construir!"): 
            constrStop = True
            print()
        else:
            compIn = compIn.split()  # Separa em Nome do Componente | Quantidade do Componente
            quant, nome = int(compIn[-1]), " ".join(compIn[0:-1])
            
            if ((not nome in componentes)):
                # Caso o componente seja inútil
                # Adiciona à lista de inúteis por ordem de entrada
                print(f"Hmm, {nome} não parece ser útil para este projeto.")
                if (nome in nomeCompNotIn):
                    idCompNot = nomeCompNotIn.index(nome)
                    quantCompNotIn[idCompNot] += quant
                else:
                    nomeCompNotIn.append(nome)
                    quantCompNotIn.append(quant)
            else:
                # Caso esse componente já exista, então incrementa a quantidade
                if(nome in nomeCompIn):
                    # Caso o componente seja útil
                    idComp = nomeCompIn.index(nome)
                    quantCompIn[idComp] += quant
                # Caso não exista
                else:                
                    # O componente será inserido por ordem de entrada na lista de componentes úteis
                    nomeCompIn.append(nome)
                    quantCompIn.append(quant)

                if(nome == "Redstone"):
                    print(f"Mais redstone! A energia que move o progresso! (+{quant} Redstone)")
                elif(nome == "Repetidores"):
                    print(f"Repetidores para garantir que o sinal chegue longe! Perfeito! (+{quant} Repetidores)")
                elif(nome == "Tochas de Redstone"):
                    print(f"Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{quant} Tochas de Redstone)")
                elif(nome == "Lâmpadas de Redstone"):
                    print(f"Lâmpadas para o display! O resultado vai ficar bem visível. (+{quant} Lâmpadas de Redstone)")
                elif(nome == "Blocos de Notas"):
                    print(f"Blocos de Notas! Quem sabe não rola uma musiquinha no final? (+{quant} Blocos de Notas)")
                elif(nome == "Observadores"):
                    print(f"Observadores a postos! Nenhuma atualização de bloco passará despercebida. (+{quant} Observadores)")
                elif(nome == "Comparadores"):
                    print(f"Comparadores para a lógica! A precisão é a alma do negócio. (+{quant} Comparadores)")
                elif(nome == "Pistões"):
                    print(f"Pistões para mover as coisas de lugar. Isso vai ser útil! (+{quant} Pistões)")
                elif(nome == "Pistões Aderentes"):
                    print(f"Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{quant} Pistões Aderentes)")
    else:
        # Lista ordenada com as informações de entrada
        quantCompOrder = [0] * numComProj
        # Atribui as informações de maneira ordenada
        for i in range(len(nomeCompIn)):
            nome, quant  = nomeCompIn[i], quantCompIn[i]
            idProj = componentes.index(nome)
            quantCompOrder[idProj] = quant
        #
        reqs = True
        for j in range(numComProj):
            if (quantCompOrder[j] < quantCompsProj[j]):
                reqs = False

        # Caso o termo "Construir!" seja enviado"
        if (reqs):
            # Verifica se atende as quantidades de componentes do projeto
            # Caso seja, ativa a condição de parada do código
            computingStop = True
            print(f"Viniccius13 conseguiu construir o {nameProject}! Partiu programar!\n")
            print(f"Para construirmos a(o) {nameProject}, utilizamos:\n")
            
            for i in range(len(quantCompIn)): # Imprimi os componentes que temos
                print(f"{nomeCompIn[i]} : {quantCompIn[i]}")

            if (nomeCompNotIn != []):
                print(f"\nMas, em nossa jornada, também coletamos:\n")
                for i in range(len(nomeCompNotIn)):
                    print(f"{nomeCompNotIn[i]} : {quantCompNotIn[i]}")
        else:
            constrStop = False
            print(f"Ainda não é possível construir o {nameProject}! Faltam:\n")
            for k in range(numComProj):
                quantNecess = quantCompsProj[k]
                quantColected = quantCompOrder[k] # Usa a lista que criamos

                if (quantColected < quantNecess):
                    nomeFal = componentes[k] # Pega o nome na ORDEM DO PROJETO
                    faltando = quantNecess - quantColected
                    qpacks = max(1, faltando // 64)
                    print(f"{qpacks} pack(s) de {nomeFal}")
            print()