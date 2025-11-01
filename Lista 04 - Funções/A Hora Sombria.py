# Informações Levels
curLevel = 0

'''
    Em cada andar, diferentes sombras surgirão para enfrentar a equipe, cada uma com seus próprios dados de ataque e vida.
    Ao término de cada andar explorado, Makoto recupera 50 pontos de vida e 15 pontos de mana, sem ultrapassar seus valores máximos.
    Se a vida do protagonista chegar a 0, a exploração termina.
'''

# Informações Sombras
'''
    Cada sombra possui vida inicial, pontos de ataque e golpes próprios.
    As sombras podem assumir diferentes estados:
        Ativo: pronta para atacar.
        Derrubado: vulnerável, mas pode se levantar durante seu turno.
        Derrotado: foi eliminada e não pode mais atacar durante o combate.
    Pode haver múltiplas sombras por andar.

    --------

    As sombras atacam automaticamente, causando dano com base em seu golpe e poder de ataque.
    Se uma sombra estiver derrubada, ela se levanta no início de seu turno e retorna ao estado Ativo, perdendo a vulnerabilidade.
    As sombras sempre atacam Makoto.
'''

# Informações Makoto

'''
    Makoto possui uma característica única: diferente de seus companheiros, que têm apenas uma Persona, ele consegue invocar diferentes Personas e alterná-las quando quiser.

    -> Contudo, nesta exploração, ele decidiu que só trocará de Persona a cada andar explorado.

    Ou seja, seu Persona será trocado a cada novo andar, alterando assim seus status no início de cada combate.

    Makoto possui 300 pontos máximos de vida e 70 pontos máximos de mana. Seus atributos ofensivos variam conforme o Persona utilizado. Ele começa o combate inicial com essa pontuação.

    Makoto pode realizar quatro tipos de ação:

    Persona: utiliza o golpe de sua Persona atual.
    Atacar: realiza um golpe com a espada.
    Yukari: solicita Yukari para curá-lo, restaurando 100 pontos de vida (sem ultrapassar o máximo). Pode ser chamada até 2 vezes por combate.
    Junpei: solicita Junpei para executar um golpe crítico, causando 100 pontos de dano e derrubando a sombra. Pode ser chamado apenas 1 vez por combate. Caso Junpei acerte o golpe concede uma ação extra (o efeito “Mais Um”) para Makoto.
    Makoto só poderá usar o golpe de sua Persona caso possua mana suficiente.
'''

# Informações de Golpes

'''
    Existem apenas três tipos de golpes possíveis, tanto para as Personas de Makoto quanto para as sombras:

    Mágico leve – poder base 3: Zio, Garu, Agi, Bufu
    Físico leve – poder base 4: Corte, Perfuração, Pancada
    Mágico médio – poder base 5: Zionga, Garula, Agilao, Bufula

    -----------------

    Utilize a seguinte fórmula para calcular o dano de cada golpe durante o combate:

    dano = int(((poder_base * 15) ** 0.5) * (atk_usuário / 2))
    atk_usuário: inteiro que representa a força do usuário.
    poder_base: inteiro que representa o poder base do golpe utilizado.
'''

# Informações turnos

'''
    Makoto → Sombra1 → Makoto → Sombra2 → Makoto → SombraN → Makoto → Sombra1 →

    As sombras agirão na ordem em que forem recebidas na entrada.

    Por exemplo, se a entrada contiver Sombra A e Sombra B, a sequência será:

    Makoto → Sombra A → Makoto → Sombra B → Makoto → Sombra A → ...

    Essa lógica se repete independentemente da quantidade de sombras.
'''

# Funções Obrigatórias
def combat():
    # Quantidade de movimentos que os amigos de Makoto podem ajudar
    movsSupFriends = [1, 1] # [yakari, junpei]

    indexShadow, isTime = 0, "Makoto"
    stopCombat = False
    while (not stopCombat):
        if (isTime == "Makoto"):
            if (statusShadows[indexShadow] == "Ativo"):
                turnMakoto(indexShadow, statusShadows, shadowsInBattleList[indexShadow], propsMakoto, propsPersona, movsSupFriends)
                isTime = "Shadow"
        elif (isTime == "Shadow"):
            if (statusShadows[indexShadow] != "Derrotado"):
                turnShadow(indexShadow, shadowsInBattleList[indexShadow], statusShadows, propsMakoto)
                isTime = "Makoto"
        
        # Verifica MAIS UM
        oneMore = propsMakoto[3]
        if (oneMore): isTime = "Makoto"
        
        # Região de indexamento de sombra
        if (indexShadow == len())

# Resultado dos Golpes de Persona
def resultAttack(list1: list) -> str:
    ascendSortExch, reverseSortExch = bubbleSort(list1) # Número de trocas

    if (ascendSortExch == 0 or reverseSortExch == 0): 
        # Deixa a sombra vulnerável
        return "Acerto em Fraqueza"
    else:
        finalValueExch = min(ascendSortExch, reverseSortExch)
        if (finalValueExch <= 5): return "Acerto Normal"
        else: return "Erro"

def bubbleSort(list1: list):
    # Recebe uma lista e verifica se ela está ordenada com base nas exchanges
    # Retorna as exchanges
    ctrSortedExch, ctrRevSortedExch   = 0, 0
    sortedList, reverseSortedList = list1, list1[:]

    listLength = len(list1)
    for i in range(listLength):
        for j in range(i+1, listLength):

            # Verifica o ordenamento direto
            if (sortedList[i] > sortedList[j]): 
                ctrSortedExch += 1
                sortedList[i], sortedList[j] = sortedList[j], sortedList[i]
                # Verifica o ordenamento reverso
            if (reverseSortedList[i] < reverseSortedList[j]):
                ctrRevSortedExch += 1
                reverseSortedList[i], reverseSortedList[j] = reverseSortedList[j], reverseSortedList[i]

    return ctrSortedExch, ctrRevSortedExch

# As funções de turno fazem modificações diretas com base em referência
def turnShadow(indexShadow: int, propsShadow: list, statusShadow: list, propsMakoto: list):
    # [nome - vida - ataque - golpe] - propsShadow
    if (statusShadow[indexShadow] == "Derrubado"): statusShadow[indexShadow] = "Ativo"
    elif (statusShadow[indexShadow] == "Ativo"):
        nameAtk, damageAtk = propsShadow[3], propsShadow[2]
        danoShadow = calcDamage(damageAtk, nameAtk)
        propsMakoto[0] -= danoShadow # Decrementa a vida de Makoto

def turnMakoto(indexShadow: int, statusShadow: list, propsShadow: list, propsMakoto: list, propsPersona: list, movsFriends: list):
    # [nome - vida - ataque - golpe] - propsShadow
    # Recebe a quantidade atual de mana do Makoto, as informações da persona do makoto, lista de moviemntos dos amigos de Makoto
    # Alterações na vida das Sombras é feita pela referência, assim como os movimentos de junpei e yukari

    # Lista de entradas possíveis 
    actionListMakoto = ["junpei", "yuraki", "persona", "atacar"]
    # Entrada de ação do turno de Makoto
    actionMakoto = input()
    # A ação de entrada tem que estar na lista de ações
    while(not (actionMakoto in actionListMakoto) or (actionMakoto == "junpei" and movsFriends[1]) or (actionMakoto == "yukari" and movsFriends[0]) or (actionMakoto == "persona" and propsMakoto[1] <= propsPersona[3])):
        actionListMakoto = input()
    
    if (actionMakoto == "persona"): # Caso seja Makoto e tenha mana
        # Decrementa a mana do Makoto
        custoPersona = propsPersona[3]
        propsMakoto[1] -= custoPersona
        # Ataque da Persona
        elementsList = [int(x) for x in input().split()]
        resAtk = resultAttack(elementsList)
        # Condicional de ataque do BubbleSort
        # Resultados possíveis: Acerto normal, Erro, Acerto em Fraqueza
        if (resAtk == "Acerto em Fraqueza"):
            atkPersona, nameAtk = propsPersona[1], propsPersona[2]
            danoPersona = calcDamage(atkPersona, nameAtk, resAtk)
            propsShadow[1] -= danoPersona
            statusShadow[indexShadow] = "Derrubado" # Derruba a sombra
            propsMakoto[3] = True   # Concede uma ação extra
        elif (resAtk == "Acerto Normal"):
            atkPersona, nameAtk = propsPersona[1], propsPersona[2]
            danoPersona = calcDamage(atkPersona, nameAtk)
            propsShadow[1] -= danoPersona

    elif (actionMakoto == "atacar"): # Poder base sempre igual a 2
        # A questão é cagada em explicar o dano causado pelo Makoto. Assumimos equivalente ao ataque da persona
        atkPersona = propsPersona[1]
        danoMakoto = calcDamage(atkPersona)
        # Decrementando a vida da Sombra
        propsShadow[1] -= danoMakoto
    elif (actionMakoto == "junpei"):
        # junpei causa 100 de dano
        propsShadow[1] -= 100
        # Decrementa o uso da ajuda de junpei
        movsFriends[1] -= 1
    elif (actionMakoto == "yukari"):
        # yukari restaura 100 pontos de vida do Makoto
        vidaMakoto = propsMakoto[0]
        propsMakoto[0] += min(300, vidaMakoto + 100)
        # Decrementa o uso da ajuda de yukari
        movsFriends[0] -= 1   

def calcDamage(attackDamage: int, nameAttack: str = "", resultAttack: str = "") -> int:
    if (resultAttack == "Acerto em Fraqueza"):
        return int((((calcBasePower(nameAttack) * 15)**0.5) * (attackDamage/2)) * 1.5)
    else: return int(((calcBasePower(nameAttack) * 15)**0.5) * (attackDamage/2))
    
def calcBasePower(nameAttack: str) -> int:
    powerAttack, listAttacks = 0, [["Zio", "Garu", "Agi", "Bufu"], ["Corte", "Perfuração", "Pancada"], ["Zionga", "Garula", "Agilao", "Bufula"]]
    for i in range(3):
        # Golpe do tipo Mágico Leve
        if (nameAttack in listAttacks[i][0]): powerAttack = 3
        # Golpe do tipo Físico Leve
        elif (nameAttack in listAttacks[i][1]): powerAttack = 4
        # Golpe do tipo Mágico Médio
        elif (nameAttack in listAttacks[i][2]): powerAttack = 5
        elif (nameAttack == ""): powerAttack = 2
    return powerAttack

def main():
    # Condição de subida para o próximo andar
    stopUpTower = False
    while (not stopUpTower):
        # A cada novo ANDAR/BATALHA, temos:
        # Entrada do Persona de Makoto
        propsPersona = [int(x) if x.isnumeric() else x for x in input().split(" - ")] 

        # Número de sombras no combate
        numShadows = int(input())
        for i in range(numShadows):
            # Entrada da Sombra
            shadowInput = [int(x) if x.isnumeric() else x for x in input().split(" - ")]
            shadowsInBattleList.append(shadowInput)

        combat()


# Main code ---------------
# Makoto
# [nome - atk - golpe - custo]
propsPersona    = [] 
propsMakoto     = [300, 70, False] # [vida, mana, MAIS UM]

# Shadows
# [nome - vida - ataque - golpe]
shadowsInBattleList = []
statusShadows       = [] # Pode conter []


main()