# Functions
def isModifiedSrc(hrModificacao, hrMorte) -> bool:
    if (hrModificacao[0] > hrMorte[0]): return True
    elif (hrModificacao[0] == hrMorte[0] and hrModificacao[1] > hrMorte[1]): return True
    else: return False

def isElissonOnList(list) -> bool:
    if ("Elisson" in list): return True
    else: return False

def isJoaoOnList(list) -> bool:
    if ("João Guilherme" in list): return True
    else: return False

# Output inicial
print(f"TRIBUNAL EM SESSÃO\nJuiz: Que comece o julgamento do caso em pauta.\n")
print(f"Promotor Edgeworth: A promotoria está pronta, Meritíssimo.\nPhoenix Wright: (Lá vamos nós... A reputação do escritório está em jogo.) A defesa está pronta.\n")
print(f"--- SALA DE VISITAS DO TRIBUNAL ---\nJoão Guilherme: Sr. Wright, eu juro, eu não o matei! Eu estive lá, mas... é só isso!\nPhoenix Wright: (Eu sinto que ele está escondendo algo... Devo pressioná-lo por mais detalhes ou confiar no que ele me disse?)\n")
# ----------------------

# Escolha da decisão inicial
initialChoice = input()

print(f"--- DE VOLTA AO TRIBUNAL ---\nJuiz: Promotoria, apresente as evidências.\nPromotor Edgeworth: A promotoria acusa este homem pelo crime de assassinato...\nPromotor Edgeworth: ...João Guilherme!\nPromotor Edgeworth: Comecemos com a evidência virtual chave, o registro da última modificação no computador da vítima.")

# Input da hora da modificação
hrmod = input()
hrmod = [int(hrmod[:2]), int(hrmod[2:])]

print(f"Promotor Edgeworth: E, de acordo com o legista, a hora exata da morte.")

# Input da hora da morte
hrdie = input()
hrdie = [int(hrdie[:2]), int(hrdie[2:])]

print(f"Promotor Edgeworth: Finalmente, a prova irrefutável. O relatório de digitais da arma do crime, o troféu.")

# Input do número de digitais
nDigitais = int(input())

print(f"Promotor Edgeworth: Que o escrivão leia os nomes encontrados na arma...\n")

# Inputs dos nomes na lista
lsDigitais = []
for i in range(nDigitais): lsDigitais.append(input())

print(f"ARGUMENTOS FINAIS\n")

# Veredito do Juiz
veredito, elissonConf = "", False

# Bifurcações
if (initialChoice == "pressionar"):
    # a. A cena do flashback com a confissão de João é impressa:
    print(f"--- FLASHBACK: SALA DE VISITAS ---\nPhoenix Wright: HOLD IT! João, não é só isso! Eu não posso te defender se você não me contar tudo. O que realmente aconteceu naquela noite?\nJoão Guilherme: (soluço)... Certo... Eu vou contar. Não era sobre a rixa... era sobre o 'Ticket Fantasma'.\nJoão Guilherme: Um bug impossível no sistema da faculdade. Eu criei um código que o resolvia. Era a minha chance de conseguir o estágio dos sonhos.\nJoão Guilherme: Eu... eu confiei em Arthur. Mostrei o código a ele para uma revisão. E ele... ele o roubou. Apresentou como se fosse dele, levou todo o crédito.\nJoão Guilherme: E o pior, Sr. Wright... eu cometi o erro de comentar sobre meu progresso com o Elisson, o 'monitor do povo'. Ele era o único, além de mim e de Arthur, que sabia da história toda. Ele observava nossa agilidade com os tickets com um sentimento sombrio! Se houver dedo dele nisso, ele certamente tentará depôr para contar do roubo do meu código por Arthur para me incriminar!\n--- FIM DO FLASHBACK ---\n")

    # b. O argumento inicial da promotoria e a objeção da defesa são impressos:
    print(f"Promotor Edgeworth: A lógica é simples. O acusado tinha o motivo, suas digitais estão na arma, e a perícia mostra que o arquivo do 'Ticket Fantasma' foi modificado após a morte, provando que ele permaneceu na cena do crime!\nPhoenix Wright: OBJEÇÃO!\n")

    # c. Sub-bifurcação baseada nas evidências:
    if (isModifiedSrc(hrmod, hrdie)):
        veredito = "INOCENTE"
        print(f"Phoenix Wright: A sua lógica tem uma falha fatal, promotor! É impossível que meu cliente tenha modificado aquele arquivo!\nPhoenix Wright: Pois a defesa pode provar que, no exato momento da modificação, João Guilherme estava a quilômetros de distância, comprando um café na 'Cafeteria Byte'! Temos o registro da transação e uma testemunha ocular!\nPhoenix Wright: A contradição temporal, combinada com este álibi, prova apenas uma coisa: a existência de uma terceira pessoa na cena do crime!")
        if (isElissonOnList(lsDigitais)):
            print(f"Phoenix Wright: Se meu cliente tem um álibi, quem poderia ser? Quem alteraria o arquivo do 'Ticket Fantasma' para incriminar João Guilherme?\nPhoenix Wright: Só poderia ser alguém que conhecia a história... alguém que meu cliente confessou ter contado!\nPhoenix Wright: A defesa descobriu que apenas UMA outra pessoa sabia da história do código... uma pessoa cujas digitais, convenientemente, também estão na arma do crime!\nPhoenix Wright: A pessoa que matou Arthur Sean para eliminar um rival e incriminar o outro foi você...\nPhoenix Wright: ELISSON!!!\n\nElisson: N-NÃÃÃÃÃOOOOO! COMO... ELE TE CONTOU?! MEU PLANO ERA PERFEITO!\n")
            elissonConf = True
        else: print()
    elif (not isJoaoOnList(lsDigitais)):
        print(f"Phoenix Wright: A promotoria não pode sequer provar que meu cliente tocou na arma do crime! Não há digitais dele!\n")
        veredito = "INOCENTE"
    else:
        print(f"Phoenix Wright: (Droga... As digitais estão na arma e a linha do tempo da promotoria é sólida... Não tenho objeções...)\n")
        veredito = "CULPADO"
elif (initialChoice == "confiar"):
    # a. A reflexão de Phoenix é impressa:
    print(f"(Voz da Consciência de Phoenix: Eu confiei em João... mas agora, essa 'hora da modificação' não faz sentido para mim. Não tenho como usar essa evidência!)\n")
    # b. O argumento inicial da promotoria e a objeção da defesa são impressos:
    print(f"Promotor Edgeworth: A lógica é simples. O acusado tinha o motivo, e suas digitais estão na arma. O caso está encerrado.\nPhoenix Wright: OBJEÇÃO!\n")

    # c. Sub-bifurcação baseada nas evidências:
    if (not isJoaoOnList(lsDigitais)):
        print(f"Phoenix Wright: A promotoria não pode provar que meu cliente tocou na arma do crime! Não há digitais dele!\n")
        veredito = "INOCENTE"
    else:
        print(f"Phoenix Wright: (Droga... As digitais estão na arma e a linha do tempo da promotoria é sólida... Estou sem argumentos!)\n")
        veredito = "CULPADO"
    
print(f"Juiz: ...Compreendo. Após analisar todas as evidências e os argumentos...\nJuiz: O veredito para o caso de João Guilherme é: {veredito}!\n")

# Elisson se confessou
if (elissonConf):
    print(f"Juiz: Que esta corte jamais esqueça o dia em que a verdade foi revelada contra todas as probabilidades.")

if (veredito == "INOCENTE"):
    print(f"A reputação do escritório Fey & Co. continua impecável.")
elif (veredito == "CULPADO"):
    print(f"Edgeworth... Você ainda não venceu o debate final.")