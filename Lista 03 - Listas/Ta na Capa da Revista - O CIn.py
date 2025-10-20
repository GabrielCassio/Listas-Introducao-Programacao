# Output inicial
print(f"Senhoras e senhores, o desfile de gala do CIn vai começar!")
# --------------
# Informações base
nmMonitores = ["Adrieli Queiroz", "Arthur Jorge", "César Cavalcanti", "Elisson Oliveira", "Filipe Moreira", "Gabriela Alves", "Joab Henrique", "Maria Fernanda", "Miriam Gonzaga", "Sofia Remindes"]
modelos, intrusos = [], []
# -------------
nd = int(input())

# Tratamento de Patriocínio e Associados
nmPat, nmAss = input(), ""

if (nmPat == "Tha Beauty"): nmAss = "Thais Linares"
elif (nmPat == "DeGuê?"): nmAss = "Davi Brito"
elif (nmPat == "Diva Depressão"): nmAss = "Edu e Fih"
# ----------------------

events = [input() for x in range(nd)]

# Desfile
numInv = 0
mPos = 0
coreConditonal = False
for nm in events:
    mPos += 1
    # Regras de Controle
    if ((nm in nmMonitores) and (not nm in modelos)):
        print(f"Desfilante de n° {mPos}: {nm}!")
        modelos.append(nm)
    elif (nm == nmAss):
        print(f"Invasão tolerada por motivos de patrocínio!")
        print(f"Desfilante de n° {mPos}: {nm}!")
        modelos.append(nm)
        intrusos.append(nm)
    else:
        print(f"{nm} invadiu a passarela! Segurem ele(a), produção!")
        intrusos.append(nm)
        numInv += 1
        exg = False
        for monitor in nmMonitores:
            if (not exg):
                if ((not monitor in modelos) and ((not monitor in events[mPos-1:]))):
                    print(f"Desfilante de n° {mPos}: {monitor}!")
                    exg = True
                    modelos.append(monitor)
        if (not exg): 
            print(f"Desfilante de n° {mPos}: {nm}?! Pelo visto não havia como substituir...")
            modelos.append(nm)

    if (numInv == 3 and not coreConditonal):
        coreConditonal = True
        mPos += 1
        print(f"Muitas invasões estão deixando a galera irritada... Chama o Core pra acalmar os ânimos!")
        print(f"Desfilante de n° {mPos}: Core!")
        modelos.append("Core")

if ("Gretchen" in intrusos or "Tulla Luana" in intrusos or "Inês Brasil" in intrusos):
    print(f"Nas arquibancadas do CIn, sussurros indignados agitam a multidão...")

    for intruso in intrusos:
        if (intruso == "Gretchen"): print(f'\"Eles tem que respeitar os meus 37 anos de carreira! Eu hoje sou um ícone, se eu morrer hoje eu vou continuar sendo a Gretchen!\"')
        if (intruso == "Tulla Luana"): print(f'\"Ninguém ser humano está acima de mim! Mas eu estou acima de muitos... é assim que eu penso.\"')
        if (intruso == "Inês Brasil"): print(f'\"É aquele ditado... Vamo fazer o quê?\"')

# --------------------------
