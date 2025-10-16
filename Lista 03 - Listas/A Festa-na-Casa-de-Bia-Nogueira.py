# Retornando com as variáveis mnemônicas
influencerBaseList = ["Sofia Santino", "Doarda", "Ciclopin", "Bruna Pinheiro"]
cantorBaseList = ["Thiaguinho", "Little Thiago", "Neiff", "Diferenciado", "Veigh", "Mc Loma"]
guestlist, bolhalist  = [], []

stopInputs, tutorasOn, pautasOn = False, False, False
while (not stopInputs):
    entry = input()

    if (not (entry == "WhatsApp: 0 mensagens.")):
        if (entry == "CABOSSE! Bora simbora organizar essa festa."): 
            stopInputs = True
        else:
            nameGuest = " ".join(entry.split(" ")[:-3])    
            guestlist.append(nameGuest)
            if (nameGuest in influencerBaseList):
                bolhalist.append("influencer")
            elif (nameGuest in cantorBaseList):
                bolhalist.append("cantor")
            if (nameGuest == "Mc Loma"):
                guestlist.append("Mirella Santos")
                guestlist.append("Mariely Santos")

    else:
        stopInputs,tutorasOn = True, True


lenGuestList = len(guestlist)
if (lenGuestList == 0):
    print(f"I hate to tell you this BUT\nBia tava achando que ia fazer um mousse. O mousse virou uma piada, parceira")
    
if (tutorasOn):
    print(f"\nComo a vida não precisa ser only fechos, a gente vai finalizar minha franja hoje:\nEssa chapinha eu dei literalmente tipo 50 reais nela. Não é a mais potente, não é a mais mais... mas ela é algo. Às vezes a gente só precisa ser algo, não precisa ser tudo.\nE o protetor térmico? Vei, a chapinha sabe que eu tô fazendo de coração, ela nunca queimaria meu cabelo.\nEspera esfriar e você vai barbarizar quando tiver pronto\nÉ isso, tchau meus amores")

if (lenGuestList == bolhalist.count("influencer")):
    print(f'<TARDE DE FOFOCAS>\nConvidados:{", ".join(guestlist)}.')
    pautasOn = True
elif (lenGuestList == bolhalist.count("cantor")):
    print(f'<PLANOS PARA FESTA>\nConvidados:{", ".join(guestlist)}.')
    print(f"Tipo de comemoração: Paredão - Show na minha casa!!")
else:
    print(f"Cachaçaria na minha casa hoje, 21h.\nTodo mundo lá em casa! Tem que ser uma festa que dure muito, tipo 27 anos e 3 meses!!")

if (pautasOn == True):
    pautas = []
    for i in range(lenGuestList):
        entryPauta = input()
        pautas.append(entryPauta)
    for pauta in pautas:
        if (pauta == "Medo de ficar musculosa demais por causa da academia"):
            print(f"AMIGA, ouça: tem nem o P do PERIGO de você ficar grandona sem querer. Não se preocupe!")
        elif (pauta == "O cara que eu gosto não me quer, mas eu continuo insistindo. Acha que eu consigo algo?"):
            print(f"Claro que consegue, amiga! Consegue virar uma palhaça, consegue perder a autoestima... Consegue várias coisas :)")
        elif (pauta == "Meu chefe só me dá um dia de folga, mas eu precisava de dois."):
            print(f"Tem que ter pelo menos dois dias de descanso. Se seu chefe tem uma empresa que não pode passar dois dias fechada porque vai quebrar, ele deveria fechar! Isso não é nem uma empresa, é um quiosque!")
        elif(pauta == "Pessoas que adoram se fazer de coitadinhas"):
            print(f"Eu detesto quem gosta de ficar pagando de coitadinho(a). Se for chorar… Na verdade, não chora não, que eu não quero nem ouvir.")
        elif(pauta == "Essa história de que homem sofre calado"):
            print(f"Vocês ficam dizendo que homem sofre, que homem sofre calado… E por que eu ainda estou ouvindo? Por que eu ainda ouço???")

    numPeopleAgree = int(input())
    if (numPeopleAgree == 0):
        print(f"Apois me interne, me prenda, me jogue fora que eu tô maluca!")
    elif (numPeopleAgree >= 1):
        print(f"É isso, eu vejo tanta coisa errada nesse mundo… Mas é como dizem, né?! Life snake, a vida cobra em inglês.")