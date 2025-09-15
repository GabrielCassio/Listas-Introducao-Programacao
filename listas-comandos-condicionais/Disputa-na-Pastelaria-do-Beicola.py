# Players da competição
nomeCompetidor1     = input()
pasteisCompetidor1  = int(input())
nomeCompetidor2     = input()
pasteisCompetidor2  = int(input())
nomeCompetidor3     = input()
pasteisCompetidor3  = int(input())

# Definindo o maior número de pastéis consumidos
numPasteisMax   = max(pasteisCompetidor1, pasteisCompetidor2, pasteisCompetidor3)

# Definindo o vencedor
playerVencedor    = ''
if (numPasteisMax == pasteisCompetidor1):
    playerVencedor  = nomeCompetidor1
elif (numPasteisMax == pasteisCompetidor2):
    playerVencedor = nomeCompetidor2
else:
    playerVencedor  = nomeCompetidor3

florinaoIn = ("Floriano" == nomeCompetidor1 or "Floriano" == nomeCompetidor2 or "Floriano" == nomeCompetidor3)
# Outputs condicionadas
if ("Lineu" == nomeCompetidor1 or "Lineu" == nomeCompetidor2 or "Lineu" == nomeCompetidor3):
    print(f"Lineu comeu um pastel com gosto estranho e usou sua autoridade na vigilancia sanitaria para acabar com a competição, Beiçola tá desolado!")
else:
    print(f"A(O) campeã(o) é {playerVencedor}, com {numPasteisMax} pastéis consumidos!")
    if (florinaoIn and (playerVencedor != "Floriano")):
        print(f"Anos comendo pastel e perdeu justo para {playerVencedor}, lastimável, Sr. Flor!")
    if (playerVencedor == "Agostinho"):
        if (numPasteisMax > 100):
            print(f"Acho que o Agostinho deve ter escondido alguns pastéis na calça, pilantra!")
        elif ((50 < numPasteisMax < 100)):
            print(f"Agostinho madrugou no taxi e veio cheio de fome para a competição!")

'''
numPasteisMax    = pasteisCompetidor1
if (pasteisCompetidor2 > numPasteisMax):
    numPasteisMax   = pasteisCompetidor2
if (pasteisCompetidor3 > numPasteisMax):
    numPasteisMax   = pasteisCompetidor3
'''