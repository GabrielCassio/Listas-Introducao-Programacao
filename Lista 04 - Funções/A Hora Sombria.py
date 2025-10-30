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
    movsSupFriends = [2, 1] # [yakari, jumpei]


def turnShadow(statusShadow: str):
    if (statusShadow == "Derrubado"):
        statusShadow = "Ativo"
    ...

def turnMakoto(movsFriends: list):
    # Recebe a quantidade atual de mana do Makoto, as informações da persona do makoto, lista de moviemntos dos amigos de Makoto

    # Lista de entradas possíveis 
    actionListMakoto = ["jumpei", "yuraki", "persona", "atacar"]
    # Entrada de ação do turno de Makoto
    actionMakoto = input()
    # A ação de entrada tem que estar na lista de ações
    while(not (actionMakoto in actionListMakoto) or (actionMakoto == "jumpei" and movsFriends[1]) or (actionMakoto == "yukari" and movsFriends[0]) or (actionMakoto == "persona" and propsMakoto[1] <= personaMakoto[3])):
        actionListMakoto = input()
    
    if (actionMakoto == "jumpei"):
        # Jumpei causa 100 de dano

        # Decrementa o uso da ajuda de jumpei
        movsFriends[1] -= 1
    elif (actionMakoto == "yukari"):
        # yukari restaura 100 pontos de vida do Makoto
        vidaMakoto = propsMakoto[0]
        propsMakoto[0] += min(300, vidaMakoto + 100)
        # Decrementa o uso da ajuda de yukari
        movsFriends[0] -= 1
    elif (actionMakoto == "persona"):
        elementsList = input().split()
    elif (actionMakoto == "atacar"):
        ...

    

def calcDamage():
    ...

def bubbleSort(list: list) -> list:
    # Recebe uma lista não ordenada e devolve uma lista ordenada
    listLength = len(list)
    for i in range(listLength):
        for j in range(i+1, listLength):
            if (list[i] > list[j]): list[i], list[j] = list[j], list[i]
    return list

def main():
    # Condição de subida para o próximo andar
    stopUpTower = False
    while (not stopUpTower):
        # A cada novo ANDAR/BATALHA, temos:
        # Entrada do Persona de Makoto
        personaMakoto = [int(x) if x.isnumeric() else x for x in input().split(" - ")] 

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
personaMakoto   = [] 
propsMakoto     = [300, 70] # [vida, mana]

# Shadows
# [nome - vida - ataque - golpe]
shadowsInBattleList = []
statusShadows       = [] # Pode conter []


main()