# Output Inicial
print(f"Serão 12 desenvolvedores defendendo a honra de seus lados do código! Que vença a melhor stack!")
# Variáveis de Setup da Brincadeira | typePlayer: "campo" ou "morto"
teamInAttack, stopGame, typePlayer, numPlayersFront, numPlayersBack, deathZoneFront, deathZoneBack = input(), False, "campo", 6, 6, 0, 0
while(teamInAttack != "Front-End" and teamInAttack != "Back-End"):
    print(f"Entrada inválida!") 
    teamInAttack = input()

while (not stopGame):
    # Caso seja uma jogada de Jogador em Campo
    if (typePlayer  == "campo"):
        if (teamInAttack == "Front-End"):
            # Entrada
            resultAttack = input()
            while(resultAttack != "acertou" and resultAttack != "errou"): 
                print(f"Entrada inválida!")
                resultAttack = input()
            # --------------------------------
            if (resultAttack == "acertou"):
                numPlayersBack  -= 1
                deathZoneBack   += 1
                print(f"{teamInAttack} acertou um jogador!")
                print(f"Back-End: {numPlayersBack} dev(s) em campo. | Front-End: {numPlayersFront} dev(s) em campo.")
                teamInAttack, typePlayer    = "Back-End", "morto"
            elif (resultAttack == "errou"):
                if (deathZoneFront == 0): teamInAttack    = "Back-End"
                else:
                    # Entrada
                    resultDefense = input()
                    while(resultDefense != "deixou" and resultDefense != "pegou"): 
                        print(f"Entrada inválida!")
                        resultDefense = input()
                    # --------------------------
                    if (resultDefense == "pegou"): teamInAttack = "Back-End"
                    elif (resultDefense == "deixou"): typePlayer = "morto"

        elif (teamInAttack == "Back-End"):
            # Entrada
            resultAttack = input()
            while (resultAttack != "acertou" and resultAttack != "errou"): 
                print(f"Entrada inválida!")
                resultAttack = input()
            # --------------------------------
            if (resultAttack == "acertou"):
                numPlayersFront  -= 1
                deathZoneFront   += 1
                print(f"{teamInAttack} acertou um jogador!")
                print(f"Back-End: {numPlayersBack} dev(s) em campo. | Front-End: {numPlayersFront} dev(s) em campo.")
                teamInAttack, typePlayer    = "Front-End", "morto"
            elif (resultAttack == "errou"):
                if (deathZoneBack == 0): teamInAttack    = "Front-End"
                else:
                    # Entrada
                    resultDefense = input()
                    while(resultDefense != "deixou" and resultDefense != "pegou"): 
                        print(f"Entrada inválida!")
                        resultDefense = input()
                    # --------------------------
                    if (resultDefense == "pegou"): teamInAttack = "Front-End"
                    elif (resultDefense == "deixou"): typePlayer = "morto"
    # --------------------------------
    # Caso seja uma jogada de Jogador Morto
    elif (typePlayer == "morto"):
        if (teamInAttack == "Front-End"):
            # Entrada
            resultAttack = input()
            while (resultAttack != "acertou" and resultAttack != "errou"):
                print(f"Entrada inválida!")
                resultAttack = input()
            # -----------------------------
            if (resultAttack == "acertou"):
                print(f"O morto do {teamInAttack} acertou um jogador!")
                numPlayersBack  -= 1
                deathZoneBack   += 1
                numPlayersFront += 1
                deathZoneFront  -= 1
                teamInAttack    = "Back-End"
                print(f"Back-End: {numPlayersBack} dev(s) em campo. | Front-End: {numPlayersFront} dev(s) em campo.")
            elif (resultAttack == "errou"):
                # Entrada
                resultDefense = input()
                while(resultDefense != "deixou" and resultDefense != "pegou"): 
                    print(f"Entrada inválida!")
                    resultDefense = input()
                # --------------------------
                if (resultDefense == "pegou"): teamInAttack, typePlayer = "Back-End", "campo"
                elif (resultDefense == "deixou"): typePlayer = "campo"
        elif (teamInAttack == "Back-End"):
            # Entrada
            resultAttack = input()
            while (resultAttack != "acertou" and resultAttack != "errou"): 
                print(f"Entrada inválida!")
                resultAttack = input()
            # -----------------------------
            if (resultAttack == "acertou"):
                print(f"O morto do {teamInAttack} acertou um jogador!")
                numPlayersBack  += 1
                deathZoneBack   -= 1
                numPlayersFront -= 1
                deathZoneFront  += 1
                teamInAttack    = "Front-End"
                print(f"Back-End: {numPlayersBack} dev(s) em campo. | Front-End: {numPlayersFront} dev(s) em campo.")
            elif (resultAttack == "errou"):
                # Entrada
                resultDefense = input()
                while(resultDefense != "deixou" and resultDefense != "pegou"): 
                    print(f"Entrada inválida!")
                    resultDefense = input()
                # --------------------------
                if (resultDefense == "pegou"): teamInAttack, typePlayer = "Front-End", "campo"
                elif (resultDefense == "deixou"): typePlayer = "campo"
    # Verifica fim de Jogo
    if (numPlayersBack == 0 or numPlayersFront == 0): stopGame = True

if (numPlayersFront == 0): print(f"Vitória do Back-End! Restaram {numPlayersBack} devs ainda mantendo o servidor de pé!")
elif (numPlayersBack == 0): print(f"Vitória do Front-End! Restaram {numPlayersFront} devs ainda segurando o layout!")