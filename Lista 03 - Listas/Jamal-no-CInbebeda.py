print(f"Finalmente Jamal chega no CInbebeda, pronto pra causar, quando de repente…\n"
    f"Jamal - \"Que danado é isso?\"")

entrada = input().split(", ") # Nomes e Notas monitores
nomes = entrada[0: 8: 2]

while (not "Júnior" in nomes or not "Henrique" in nomes or not "Guilherme" in nomes or not "Miguel" in nomes):
    print(f"Insira nomes válidos.")
    entrada = input().split(", ")
    nomes = entrada[0: 8: 2]

# Caso todos os nomes válidos, então calculamos notas:
notas = [int(x) for x in entrada[1: 8: 2]]

# Para qualquer um com nota 10
for i in range(4):
    if (notas[i] == 10): print(f"O monitor {nomes[i]} é diferenciado! Teve a aprovação do próprio Jamal.")

# Qual aquele com pior nota
nomePiorNota = nomes[notas.index(min(notas))]
print(f"Jamal avaliou a situação dos monitores e viu que {nomePiorNota} é o mais necessitado.")

# Output do Jamal
movOutJamal = f"Jamal - Movimentação 0:\n" + f". . .\n"+f". . .\n"+f"E . D\n"+f"\nJamal - Movimentação 1:\n"+f". 1 .\n"+f". . .\n"+f"E . .\n"+f"\nJamal - Movimentação 2:\n"+f". . .\n"+f". . .\n"+f"E . 2\n"+f"\nJamal - Movimentação 3:\n"+f". 3 .\n"+f". . .\n"+f". . D\n"+f"\nJamal - Movimentação 4:\n"+f". . .\n"+f". . .\n"+f"4 . D\n"+f"\nJamal - Movimentação 5:\n"+f". 5 .\n"+f". . .\n"+f"E . .\n"+f"\nJamal - Movimentação 6:\n"+f". D .\n"+f". . .\n"+f"6 . .\n"+f"\nJamal - Movimentação 7:\n"+f". 7 .\n"+f". . .\n"+f"E . .\n"
print(f"Jamal - \"Vou ensinar apenas uma vez, então preste atenção.\"")
print(f"\n{movOutJamal}")

# Movimentos pré-setados do Jamal
presetJamal = ["D12", "D33", "E12", "E31", "D12", "E31", "D12"]
# Entrada do conjunto de movimentos do monitor com pior nota
movMonitor = input().split(", ")
# Verificação de validade do conjunto
movSetValid, nInvalids = False, 0
while(not movSetValid):
    newCall = False
    if (len(movMonitor) != 7): newCall = True
    else:
        for j in range(7):
            if ("E" != movMonitor[j][0] and "D" != movMonitor[j][0]) or (int(movMonitor[j][1]) > 3 or int(movMonitor[j][1]) < 1) or (int(movMonitor[j][2]) > 3 or int(movMonitor[j][2])< 1): newCall = True
    if (newCall):
        nInvalids += 1
        print(f"Movimento inválido! Por favor, insira outro.")
        movMonitor = input().split(", ")
    else: movSetValid = True
if (nInvalids > 0): print()

# Comparação de movimentos monitor e Jamal
qErros = 0
for k in range(7): 
    # Comparação 1 a 1 do passinho do monitor com o preset do Jamal
    if (movMonitor[k] != presetJamal[k]): qErros+=1

# Output Monitor
# Desenhar a saída das matrizes
movOutMonitor = [[".", ".", "."], [".", ".", "."], ["E", ".", "D"]]

print(f"{nomePiorNota} - Movimentação 0:\n"+f". . .\n"+f". . .\n"+f"E . D\n")
xE, yE, xD, yD = 2, 0, 2, 2
for i in range(7):
    # Verificando qual pé está se movendo
    if (movMonitor[i][0] == "E"): # Pé esquerdo se move
        movOutMonitor[xD][yD] = "D"
        movOutMonitor[xE][yE] = "." # Retira a letra da Matriz
        # Carrega posição do Pé em movimento
        xE,yE = int(movMonitor[i][1])-1, int(movMonitor[i][2])-1
        # Substituindo o conteúdo da matriz pelo número do passo
        movOutMonitor[xE][yE] = str(i+1)
    else: 
        movOutMonitor[xE][yE] = "E"
        movOutMonitor[xD][yD] = "."
        # Carrega posição do Pé em movimento
        xD,yD = int(movMonitor[i][1])-1, int(movMonitor[i][2])-1
        # Substituindo o conteúdo da matriz pelo número do passo
        movOutMonitor[xD][yD] = str(i+1)
    
    print(f"{nomePiorNota} - Movimentação {i+1}:")
    for m in range(3): print(" ".join(movOutMonitor[m]))
    print()

# Condições de verificação de segunda chance e se foram convidades para show
secondTime, invited = False, False
# Toma como base o número de erros
if (qErros == 0):
    invited = True
    if (nomePiorNota == "Júnior"): print(f"Uma máquina! Depois de horas vendo o passinho no Instagram ele conseguiu pegar mais rápido.")
    elif (nomePiorNota == "Henrique"): print(f"O maldito talento ataca novamente! Tinha que ser o desenrolado.")
    elif (nomePiorNota == "Miguel"): print(f"O cara veio do interior pra mostrar como que se faz!")
    elif (nomePiorNota == "Guilherme"): print(f"Ninguém nunca tinha visto ele dançar! Sabíamos que ele estava escondendo um dom.")
elif (qErros == 1):
    secondTime = True
    print(f"Foi quase! O monitor merece uma nova chance!")
elif (qErros == 2): print(f"Melhor o monitor {nomePiorNota} deixar esse negócio de dança pra lá.")
elif (qErros == 3): print(f"Isso tá horrível!")
else: print(f"O monitor {nomePiorNota} foi expulso da festa por não saber dançar.")

if (secondTime):
    movMonitor = input().split(", ") # Nova entrada de movimentos
    # Novo conjunto de movimentos
    movOutMonitor = [[".", ".", "."], [".", ".", "."], ["E", ".", "D"]] # Reset do conjunto de saída
    print(f"\n{nomePiorNota} - Movimentação 0:\n"+f". . .\n"+f". . .\n"+f"E . D\n")
    xE, yE, xD, yD = 2, 0, 2, 2
    for i in range(7):
        # Verificando qual pé está se movendo
        if (movMonitor[i][0] == "E"): # Pé esquerdo se move
            movOutMonitor[xD][yD] = "D"
            movOutMonitor[xE][yE] = "." # Retira a letra da Matriz
            # Carrega posição do Pé em movimento
            xE,yE = int(movMonitor[i][1])-1, int(movMonitor[i][2])-1
            # Substituindo o conteúdo da matriz pelo número do passo
            movOutMonitor[xE][yE] = str(i+1)
        else: 
            movOutMonitor[xE][yE] = "E"
            movOutMonitor[xD][yD] = "."
            xD,yD = int(movMonitor[i][1])-1, int(movMonitor[i][2])-1
            # Substituindo o conteúdo da matriz pelo número do passo
            movOutMonitor[xD][yD] = str(i+1)
        
        print(f"{nomePiorNota} - Movimentação {i+1}:")
        for m in range(3): print(" ".join(movOutMonitor[m]))
        print()
    
    if (movMonitor == presetJamal):
        invited = True
        print(f"Era isso! {nomePiorNota} só estava precisando de um empurrãozinho.")
    else: print(f"Nem com outra tentativa {nomePiorNota} conseguiu ajeitar isso.")

if (invited):
    print(f"Jamal - \"Vocês aprendem rápido! Quero que vocês dancem no meu próximo show!\"")
    response = input()
    if (response == "Sim"): print(f"Óbvio que o monitor {nomePiorNota} não perderia essa oportunidade por nada!")
    elif (response == "Não"): print(f"Infelizmente o monitor {nomePiorNota} jogou essa oportunidade fora. Todos sabem que lá na frente ele vai se arrepender disso.")
else: print(f"Jamal desistiu de ensinar pra quem não aprende. Ele saiu em grande estilo, mandando o passinho e andando.")