# Vida inicial de Madeline
lifeMadeline = 100

def attackBadeline(life) -> int:
    sIn = input()
    if (sIn == "Você não tem o que é necessário para escalar."):
        life -= 20
        print(f"Eu nunca vou conseguir chegar ao topo :(")
    elif (sIn == "NÓS NUNCA DEVERÍAMOS TER SAÍDO DE CASA! VAMOS MORRER NESSA MONTANHA!"):
        life -= 50
        print(f"NAAÃO EU NUNCA DEVERIA TER INVENTADO DE ESCALAR ESSA MONTANHA!")
    
    return life


def reactionMadeline(life) -> int:
    sIn = input()
    if (sIn == "Calma Badeline, nós vamos conseguir."):
        life += 25
    elif (sIn == "Eu sei que somos capazes! Vamos em frente!"):
        nResps = int(input())
        life += (10 * nResps)
    elif (sIn == "Madeline, nós estamos com você. Continue!"):
        life += 60
    
    return life

# Ordem dos Eventos: Ataque Badeline, Reação Madeline 
# Madeline Wins
stopRun, sideAction = False, True
while (not stopRun):

    if (sideAction): lifeMadeline = attackBadeline(lifeMadeline)
    else: lifeMadeline = reactionMadeline(lifeMadeline)
        
    sideAction = not sideAction

    # Condição de encerramento do programa
    if (not (0 <= lifeMadeline < 150)): stopRun = True

if (lifeMadeline >= 150):
    print(f"Madeline chegou ao topo! Ela se senta em um banco para descansar e apreciar a vista.")
elif (lifeMadeline <= 0):
    print(f"Madeline e Badeline não conseguiram se entender... parece que elas nunca vão ver a cidade de cima.")