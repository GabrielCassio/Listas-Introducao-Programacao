# Mensagem de início da competição
print(f"Bem-vindos ao Jimmy Jab!")

participante1   = input()
participante2   = input()
participante3   = input()
participante4   = input()

# Status do Evento 1 - Bocatona
vencedorBocatona    =  ""
perdedorBocatona    =  ""

# Status do Evento 2 - Corrida
maiorTempo     = 0
menorTempo     = 0
vencedorCorrida     = ""
perdedorCorrida     = ""

# Ganhador e 2º Lugar
ganhadorCompeticao  = ""
segundoLugar        = ""

# Verifica se o sargento ou capitão estão entre os participantes
if ((participante1 != "Terry" and participante1 != "Holt") and
    (participante2 != "Terry" and participante2 != "Holt") and 
    (participante3 != "Terry" and participante3 != "Holt") and 
    (participante4 != "Terry" and participante4 != "Holt")):
        # Evento 1 - Bocatona
        print(f"Nosso primeiro evento é...\nA Bocatona!")
        # Condicão de Vitória obrigatória caso participação dew Scully no Bocatona
        if (participante1 == "Scully" or
            participante2 == "Scully" or
            participante3 == "Scully" or
            participante4 == "Scully"):
                vencedorBocatona    = "Scully"
                perdedorBocatona    =  input()
                print(f"Scully leva a melhor, não tem como competir com ele.")
                print(f"{perdedorBocatona} não avançou para a próxima fase!")
        else:
                vencedorBocatona    = input()
                perdedorBocatona    = input()
                print(f"{vencedorBocatona} levou a melhor na Bocatona!")
                print(f"{perdedorBocatona} não avançou para a próxima fase!")
        
        # Reorganização dos participantes pós saída do perdedor do Bocatona
        if (participante1 == perdedorBocatona):
            participante1, participante2, participante3 = participante2, participante3, participante4
        elif (participante2 == perdedorBocatona):
            participante2, participante3 = participante3, participante4
        elif (participante3 == perdedorBocatona):
            participante3   = participante4
        
        # Evento 2 - Corrida
        print(f"O segundo evento é A corrida volumosa!")
        # Recebe Tempo
        tempoCorrida1   = int(input())
        tempoCorrida2   = int(input())
        tempoCorrida3   = int(input())

        # Maior e menor tempo
        maiorTempo = max(tempoCorrida1, tempoCorrida2, tempoCorrida3)
        menorTempo = min(tempoCorrida1, tempoCorrida2, tempoCorrida3)

        # Encontra o vencedor da corrida
        if (menorTempo == tempoCorrida1):
            vencedorCorrida = participante1
        elif (menorTempo == tempoCorrida2):
            vencedorCorrida = participante2
        else:
            vencedorCorrida = participante3

        # Encontra o perdedor da Corrida
        if (maiorTempo == tempoCorrida1):
            perdedorCorrida = participante1
        elif (maiorTempo == tempoCorrida2):
            perdedorCorrida = participante2
        elif (maiorTempo == tempoCorrida3):
            perdedorCorrida = participante3
        
        # Mostrando o vencedor e perdedor da Corrida
        print(f"{vencedorCorrida} levou a melhor na Corrida Volumosa!")
        print(f"{perdedorCorrida} não avançou para a próxima fase!")

        # Reorganização dos participantes pós saída do perdedor da Corrida
        if (participante1 == perdedorCorrida):
            participante1, participante2 = participante2, participante3
        elif (participante2 == perdedorCorrida):
            participante2   = participante3
        
        if ((participante1 == "Amy" or participante1 == "Jake") and
            (participante2 == "Amy" or participante2 == "Jake")):
            print(f"Jake ficou com o 2º lugar!\nAmy VENCEU O JIMMY JABS!")
        else:
            ganhadorCompeticao = input()
            segundoLugar = participante2 if (ganhadorCompeticao == participante1) else participante1
            print(f"{segundoLugar} ficou com o 2º lugar!\n{ganhadorCompeticao} VENCEU O JIMMY JABS!")
else:
     print(f"Jimmy Jab CANCELADO!")