# Output Inicial - Saída obrigatória
print(f"Finalmente Jamal chega no CInbebeda, pronto pra causar, quando de repente…\nJamal - \"Que danado é isso?\"")
# --------------------

nmMonitors = ["Júnior", "Henrique", "Miguel", "Guilherme"]
entry = input().split(", ")
nomes, notas = entry[0:8:2], [int(i) for i in entry[1:8:2]]
#print(notas)

# Verifica se todos os monitores desejados
while ((not "Júnior" in nomes) or (not "Henrique" in nomes) or  (not "Miguel" in nomes) or (not "Guilherme" in nomes)):
    #print(f"O nome {nomes[i]} não é de um monitor.")
    entry = input().split(", ")
    print(f"Insira nomes válidos.") # Saída obrigatória
    nomes, notas = entry[0:-1:2], [int(i) for i in entry[1:8:2]]

#print(f"Todos os nomes são de monitores 👍")
# --------------------------------------

nmPior = nomes[notas.index(min(notas))]

for j in range(4):
    if (notas[j] == 10): print(f"O monitor {nomes[j]} é diferenciado! Teve a aprovação do próprio Jamal.")

# Retorna o Nome do Monitor com menor Nota
print(f"Jamal avaliou a situação dos monitores e viu que {nmPior} é o mais necessitado.")
# ------------------------------------

# Recebe a string com os movimentos do monitor
movPes = input().split(", ")

# Treinamento do Jamal
presetJamal = ["D12", "D33", "E12", "E31", "D12", "E31", "D12"]

# Calculando erros de movimento
qErrors = 0
for k in range(7): 
    if (movPes[k] != presetJamal[k]): qErrors+=1
# ----------------------------  

movOutJamal = f"\nJamal - Movimentação 0:\n" + f". . .\n"+f". . .\n"+f"E . D\n"+f"\nJamal - Movimentação 1:\n"+f". 1 .\n"+f". . .\n"+f"E . .\n"+f"\nJamal - Movimentação 2:\n"+f". . .\n"+f". . .\n"+f"E . 2\n"+f"\nJamal - Movimentação 3:\n"+f". 3 .\n"+f". . .\n"+f". . D\n"+f"\nJamal - Movimentação 4:\n"+f". . .\n"+f". . .\n"+f"4 . D\n"+f"\nJamal - Movimentação 5:\n"+f". 5 .\n"+f". . .\n"+f"E . .\n"+f"\nJamal - Movimentação 6:\n"+f". D .\n"+f". . .\n"+f"6 . .\n"+f"\nJamal - Movimentação 7:\n"+f". 7 .\n"+f". . .\n"+f"E . .\n"
# Saídas obrigatórias do Jamal
print(f"Jamal - \"Vou ensinar apenas uma vez, então preste atenção.\"")
print(f"{movOutJamal}")
# --------------------------

# Verificação de Validade dos movimentos
j = 0
while(j < 7):
    if (("E" != movPes[j][0] and "D" != movPes[j][0]) or 
        (3 < int(movPes[j][1]) or int(movPes[j][1]) < 1) or (3 < int(movPes[j][2]) or int(movPes[j][2])< 1) or
        (len(movPes) != 7)):
        j = 0
        print(f"Movimento inválido! Por favor, insira outro.\n")
        movPes = input().split(", ")
    else: j += 1
# ------------------------------------  

# Saídas do monitor
movOutMonitor = [[".", ".", "."], [".", ".", "."], ["E", ".", "D"]]

print(f"{nmPior} - Movimentação 0:\n"+f". . .\n"+f". . .\n"+f"E . D\n")
xE, yE, xD, yD = 2, 0, 2, 2
for i in range(7):
    # Verificando qual pé está se movendo
    if (movPes[i][0] == "E"): # Pé esquerdo se move
        movOutMonitor[xD][yD] = "D"
        movOutMonitor[xE][yE] = "." # Retira a letra da Matriz
        # Carrega posição do Pé em movimento
        xE,yE = int(movPes[i][1])-1, int(movPes[i][2])-1
        # Substituindo o conteúdo da matriz pelo número do passo
        movOutMonitor[xE][yE] = str(i+1)
    else: 
        movOutMonitor[xE][yE] = "E"
        movOutMonitor[xD][yD] = "."
        xD,yD = int(movPes[i][1])-1, int(movPes[i][2])-1
        # Substituindo o conteúdo da matriz pelo número do passo
        movOutMonitor[xD][yD] = str(i+1)
    
    print(f"{nmPior} - Movimentação {i+1}:")
    for m in range(3):
        print(" ".join(movOutMonitor[m]))
    print()
# --------------------------------

# Verificação de sequência do passinho do Jamal
learned = False 
if (movPes == presetJamal):
    learned = True
    if (nmPior == "Júnior"): print(f"Uma máquina! Depois de horas vendo o passinho no Instagram ele conseguiu pegar mais rápido.")
    elif (nmPior == "Henrique"): print(f"O maldito talento ataca novamente! Tinha que ser o desenrolado.")
    elif (nmPior == "Miguel"): print(f"O cara veio do interior pra mostrar como que se faz!")
    # Guilherme
    else: print(f"Ninguém nunca tinha visto ele dançar! Sabíamos que ele estava escondendo um dom.")
else:
    # Caso tenha apenas 1 erro, recebe UMA nova entrada com movimento válidos
    if (qErrors == 1): 
        # Saída obrigatória
        print(f"Foi quase! O monitor merece uma nova chance!")
        movPes = input().split(", ")
        print()
        if (movPes == presetJamal):
            print(f"{movOutJamal}")
            # Saídas do monitor
            movOutMonitor = [[".", ".", "."], [".", ".", "."], ["E", ".", "D"]]
            print(f"{nmPior} - Movimentação 0:\n"+f". . .\n"+f". . .\n"+f"E . D\n")
            xE, yE, xD, yD = 2, 0, 2, 2
            for i in range(7):
                # Verificando qual pé está se movendo
                if (movPes[i][0] == "E"): # Pé esquerdo se move
                    movOutMonitor[xD][yD] = "D"
                    movOutMonitor[xE][yE] = "." # Retira a letra da Matriz
                    # Carrega posição do Pé em movimento
                    xE,yE = int(movPes[i][1])-1, int(movPes[i][2])-1
                    # Substituindo o conteúdo da matriz pelo número do passo
                    movOutMonitor[xE][yE] = str(i+1)
                else: 
                    movOutMonitor[xE][yE] = "E"
                    movOutMonitor[xD][yD] = "."
                    xD,yD = int(movPes[i][1])-1, int(movPes[i][2])-1
                    # Substituindo o conteúdo da matriz pelo número do passo
                    movOutMonitor[xD][yD] = str(i+1)
                
                print(f"{nmPior} - Movimentação {i+1}:")
                for m in range(3):
                    print(" ".join(movOutMonitor[m]))
                print()
            # --------------------------------
            learned = True
            print(f"Era isso! {nmPior} só estava precisando de um empurrãozinho.")
        else: print(f"Nem com outra tentativa {nmPior} conseguiu ajeitar isso.")
    elif (qErrors == 2):
        print(f"Melhor o monitor {nmPior} deixar esse negócio de dança pra lá.")
    elif (qErrors == 3):
        print(f"Isso tá horrível!")
    else: print(f"O monitor {nmPior} foi expulso da festa por não saber dançar.")
# ------------------------------------------

# Convite do Jamal caso todos tenham passado
if (learned):
    print(f"Jamal - \"Vocês aprendem rápido! Quero que vocês dancem no meu próximo show!\"")
    invite = input()
    if (invite == "Sim"): print(f"Óbvio que o monitor {nmPior} não perderia essa oportunidade por nada!")
    elif (invite == "Não"): print(f"Infelizmente o monitor {nmPior} jogou essa oportunidade fora. Todos sabem que lá na frente ele vai se arrepender disso.")
else:
    print(f"Jamal desistiu de ensinar pra quem não aprende. Ele saiu em grande estilo, mandando o passinho e andando.")
# ----------------------------------------