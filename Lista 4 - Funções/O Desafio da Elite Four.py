def DefineTeam() -> list:
    team = []
    for i in range(4):
        sIn = [int(x) if (x.isnumeric()) else x for x in input().split(" - ")]
        team.append(sIn)
    return team

def ChoiceOp() -> str:
    elit4Names = ["lorelei", "bruno", "agatha", "lance"]
    nmOponent = input().lower()
    if (nmOponent in elit4Names): return nmOponent

def OponentTeam(nameOp: str) -> list:
    pokemonTeam = []
    if (nameOp == "lorelei"): # Lorelei Team
        pokemonTeam = [  
            ["Lapras", "agua", 220, 50, "Raio de Gelo", 60, "agua", 60],
            ["Blastoise", "agua", 180, 55, "Hidro Bomba", 65, "agua", 78],
            ["Victreebel", "grama", 160, 40, "Folha Navalha", 55, "grama", 70],
            ["Ninetales", "fogo", 170, 45, "Lança-chamas", 60, "fogo", 100]]
    elif (nameOp == "bruno"): # Bruno Team
        pokemonTeam = [   
            ["Charizard", "fogo", 190, 40, "Presa de Fogo", 70, "fogo", 100],
            ["Arcanine", "fogo", 180, 50, "Velocidade Extrema", 60, "fogo", 95],
            ["Kingler", "agua", 170, 60, "Caranguejo Martelo", 65, "agua", 75],
            ["Jolteon", "eletrico", 150, 35, "Choque do Trovão", 55, "eletrico", 130]]
    elif (nameOp == "agatha"): # Agatha Team
        pokemonTeam = [   
            ["Venusaur", "grama", 180, 50, "Raio Solar", 70, "grama", 80],
            ["Vileplume", "grama", 160, 45, "Pó do Sono", 50, "grama", 50],
            ["Raichu", "eletrico", 160, 40, "Investida Trovão", 65, "eletrico", 110],
            ["Poliwrath", "agua", 190, 55, "Soco Dinâmico", 60, "agua", 70]]
    elif (nameOp == "lance"): # Lance Team
        pokemonTeam = [   
            ["Electabuzz", "eletrico", 180, 45, "Soco de Trovão", 75, "eletrico", 105],
            ["Jolteon", "eletrico", 170, 35, "Onda de Trovão", 60, "eletrico", 130],
            ["Exeggutor", "grama", 160, 40, "Bomba de Semente", 65, "grama", 55],
            ["Magmar", "fogo", 175, 40, "Giro de Fogo", 55, "fogo", 93]]
    
    return pokemonTeam

def IsPokElissonMF(velPokElisson: int, velPokOponente: int) -> bool:
    if (velPokElisson >= velPokOponente): return True
    else: return False

# Verifica se o Ataque é Efetivo
def IsTypeEffective(typeAttack: str, typePokDef: str) -> float:
    if (typeAttack == "normal"): return 1.0
    superEffecComb = [["fogo", "grama"], ["agua", "fogo"], ["grama", "agua"], ["eletrico", "agua"]]
    lowEffecComb = [["grama", "fogo"], ["fogo", "agua"], ["agua", "grama"], ["agua", "eletrico"]]
    if ([typeAttack, typePokDef] in superEffecComb): return 2.0
    elif ([typeAttack, typePokDef] in lowEffecComb): return 0.5
    else: return 1.0

def ExecuteAttack(elissonPok: list, oponentPok: list, maxLifeEliPok: int, maxLifeOpPok: int):
    # Quem começará o TURNO baseado na VELOCIDADE dos Pokemons
    if (IsPokElissonMF(elissonPok[7], oponentPok[7])):
        print(f"\n{elissonPok[0]} usa {elissonPok[4]}!") # Output de ataque
        mult1 = IsTypeEffective(elissonPok[6], oponentPok[1])
        damage = PokemonDamage(elissonPok[5], oponentPok[3], mult1)
        oponentPok[2] -= damage
        oponentPok[2] = max(0, oponentPok[2])

        if (mult1 == 2.0): print(f"{elissonPok[4]} é super efetivo!")
        elif (mult1 == 0.5): print(f"{elissonPok[4]} não é muito efetivo...")

        print(f"Causou {damage} de dano. HP de {oponentPok[0]} agora é {oponentPok[2]}/{maxLifeOpPok}.")

        if (oponentPok[2] > 0):
            print(f"\n{oponentPok[0]} do oponente usa {oponentPok[4]}!")
            mult1 = IsTypeEffective(oponentPok[6], elissonPok[1])
            damage = PokemonDamage(oponentPok[5], elissonPok[3], mult1)
            elissonPok[2] -= damage
            elissonPok[2] = max(0, elissonPok[2])

            if (mult1 == 2.0): print(f"{oponentPok[4]} é super efetivo!")
            elif (mult1 == 0.5): print(f"{oponentPok[4]} não é muito efetivo...")

            print(f"Causou {damage} de dano. HP de {elissonPok[0]} agora é {elissonPok[2]}/{maxLifeEliPok}.")
    else:
        print(f"\n{oponentPok[0]} do oponente usa {oponentPok[4]}!")
        mult1 = IsTypeEffective(oponentPok[6], elissonPok[1])
        damage = PokemonDamage(oponentPok[5], elissonPok[3], mult1)
        elissonPok[2] -= damage
        elissonPok[2] = max(0, elissonPok[2])

        if (mult1 == 2.0): print(f"{oponentPok[4]} é super efetivo!")
        elif (mult1 == 0.5): print(f"{oponentPok[4]} não é muito efetivo...")

        print(f"Causou {damage} de dano. HP de {elissonPok[0]} agora é {elissonPok[2]}/{maxLifeEliPok}.")

        if (elissonPok[2] > 0):
            print(f"\n{elissonPok[0]} usa {elissonPok[4]}!") # Output de ataque
            mult1 = IsTypeEffective(elissonPok[6], oponentPok[1])
            damage = PokemonDamage(elissonPok[5], oponentPok[3], mult1)
            oponentPok[2] -= damage
            oponentPok[2] = max(0, oponentPok[2])

            if (mult1 == 2.0): print(f"{elissonPok[4]} é super efetivo!")
            elif (mult1 == 0.5): print(f"{elissonPok[4]} não é muito efetivo...")

            print(f"Causou {damage} de dano. HP de {oponentPok[0]} agora é {oponentPok[2]}/{maxLifeOpPok}.")

#Nome - 0 | Tipo Pokemon - 1 | Vida - 2 | Defesa - 3 | Nome Ataque - 4 | Poder - 5 | Tipo Ataque - 6 | Velocidade - 7

# Funções Obrigatórias
def PokemonDamage(attackPokemon, defensePokemon, mult):
    # Recebe o Poder de Ataque do Pokemon e a Defesa do pokemon Oponente
    finalDam = max(1, int((attackPokemon - (defensePokemon/2)) * mult))
    return finalDam

def TurnsBattle(elissonPok: list, oponentPok: list, maxLifesPlayers: list):
    # Vida dos Pokemons que estão na rodada
    lifeMaxPokEli, lifeMaxPokOp = maxLifesPlayers[0], maxLifesPlayers[1]
    cTurn = 0 # Número de Turnos da Rodada
    while ((elissonPok[2] > 0 and oponentPok[2] > 0)): # Enquanto AMBOS Pokemons tiverem 
        cTurn += 1 # Incrementa Rodada

        # Início do turno do Pokemon
        print(f"\n-- Turno {cTurn} --")
        ExecuteAttack(elissonPok, oponentPok, lifeMaxPokEli, lifeMaxPokOp)

def Main(elissonTeam, oponentTeam): # Função que controla toda a batalha
    nPokElisson, nPokOponente = 4, 4 # Quantidade de Pokemons em Batalha
    elissonIdPok, oponentIdPok = 0, 0 # Id dos Pokemons no 1v1

    cRound = 0 # Número do Round
    while (nPokElisson > 0 and nPokOponente > 0):
        cRound += 1

        maxLifePlayers = [maxLifes[0][elissonIdPok], maxLifes[1][oponentIdPok]]

        # Início de Rodada
        print(f"\n--- Rodada {cRound} ---\n"
        f"{elissonTeam[elissonIdPok][0]}, eu escolho você!\n"
        f"{oponentTeam[oponentIdPok][0]}, vai!\n"
        f"--------------------")
        
        # Vida dos Pokemons no 1v1
        elissonPok, oponentPok = elissonTeam[elissonIdPok], oponentTeam[oponentIdPok]
        TurnsBattle(elissonPok, oponentPok, maxLifePlayers)
        if (elissonPok[2] == 0): 
            print(f"\n{elissonPok[0]} foi derrotado!")
            nPokElisson -= 1
            elissonIdPok += 1
        else:
            print(f"\n{oponentPok[0]} do oponente foi derrotado!")
            nPokOponente -= 1
            oponentIdPok += 1

        # End Round
        print(f"\n--------------------\n\nPlacar: {oponentIdPok} X {elissonIdPok}")
    
    # End Battle
    if (nPokElisson == 0):
        print(f"\n========================================\nQue pena! Você foi derrotado.\n========================================")
    else: 
        print(f"\n========================================\nParabéns! Você venceu a batalha Pokémon!\n========================================")    

# -----------------------------------------------
# Warmup phase
# 1. Choice your team
print(f"Hora de montar seu time Pokémon!\n")
elissonTeam = DefineTeam()

# 2. Oponent choices
print(f"Qual membro da Elite Four você deseja enfrentar?\n")
oponent = ChoiceOp()
oponentTeam = OponentTeam(oponent)

maxLifes =[[x[2] for x in elissonTeam], [x[2] for x in oponentTeam]]
# ----------------------

# Battle phase
print(f"====================\n"
    f"A BATALHA VAI COMEÇAR!\n"
    f"====================")

Main(elissonTeam, oponentTeam)