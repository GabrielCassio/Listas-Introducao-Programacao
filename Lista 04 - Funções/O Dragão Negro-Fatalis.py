def isNotLifeOk(dragonLife, statsHunters) -> bool:
    if (dragonLife <= 0): return True
    elif (statsHunters[0][0] <= 0 and statsHunters[1][0] <= 0 and statsHunters[2][0] <= 0): return True
    else: return False

# Weapons
def greatSword(enemyLife: int) -> int:
    typeAttack = input()
    if (typeAttack == "Golpe Carregado"):
        enemyLife -= 165
    elif (typeAttack == "Corte Largo"):
        enemyLife -= 120
    elif (typeAttack == "Divisor de Mundos"):
        enemyLife -= 200
    return enemyLife

def fuziArco(enemyLife: int) -> int:
    typeAttack = input()
    if (typeAttack == "Tiro Carregado"):
        enemyLife -= 90
    elif (typeAttack == "Bala de Penetração"):
        enemyLife -= 120
    elif (typeAttack == "Tiro Devastador"):
        enemyLife -= 150    
    return enemyLife

def glaiveInseto(enemyLife: int, lifeHunter: int):
    typeAttack = input()
    if (typeAttack == "Corte Aéreo"):
        enemyLife -= 100
    elif (typeAttack == "Descida Carregada"):
        enemyLife -= 120
    elif (typeAttack == "Kinseto"):
        color = input()
        if (color == "Vermelho"): enemyLife -= 40
        elif (color == "Amarelo"): enemyLife -= 15
        elif (color == "Verde"): lifeHunter += 40
    return enemyLife, lifeHunter

# Dragon Attack
def dragonAttack(statsHunters: list) -> list:
    typeAttack = input()
    if (typeAttack == "Ataque com Cauda"): 
        for i in range(3):
            statsHunters[i][0] -= 55
    elif (typeAttack == "Bola de Fogo"):
        for i in range(3):
            statsHunters[i][0] -= 65
    elif (typeAttack == "Mar de Chamas Negras"):
        for i in range(3):
            if (statsHunters[i][0]>0): 
                statsHunters[i][1] = input()
                # Caçador eleminado (Vida)
                if (statsHunters[i][1] == "Desprotegido"): 
                    statsHunters[i][0] = 0
    return statsHunters

# Output inicial
print(f"Hora de Lutar contra a Historia!\n")

# Initial Life of Fatalis, the Dragon
lifeFatalis = 1800
statsHunters = [[200, "Desprotegido", greatSword], [200, "Desprotegido", glaiveInseto], [200, "Desprotegido", fuziArco]]

# Combate com 4 turnos
nTurns, cTurn, stopBattle = 4, 0, False

while((cTurn < nTurns) and not stopBattle):
    cTurn += 1

    # Vez de cada caçador - OK
    for time in range(len(statsHunters)):
        # Regra da Vida
        stopBattle = isNotLifeOk(lifeFatalis, statsHunters) 
        if (not stopBattle):

            if (statsHunters[time][0] > 0):
                if (time == 1):
                    lifeFatalis, statsHunters[1][0] = statsHunters[1][2](lifeFatalis, statsHunters[1][0])
                else:
                    lifeFatalis = statsHunters[time][2](lifeFatalis)
    # --------------------
    
    stopBattle = isNotLifeOk(lifeFatalis, statsHunters)
    if (not stopBattle): statsHunters = dragonAttack(statsHunters)

if (lifeFatalis > 0): print(f"O Fatalis conseguiu sobreviver ao combate...\nO mundo corre perigo!")
else: print(f"Eu não acredito, vocês conseguiram!\nObrigado caçadores! O mundo está salvo.")