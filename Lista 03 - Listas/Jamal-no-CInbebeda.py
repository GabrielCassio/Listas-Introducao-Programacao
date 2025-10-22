# Output Inicial - Saída obrigatória
print(f"Finalmente Jamal chega no CInbebeda, pronto pra causar, quando de repente…\nJamal - \"Que danado é isso?\"")
# --------------------

nmMonitors = ["Júnior", "Henrique", "Miguel", "Guilherme"]
entry = input().split(", ")
nomes, notas = entry[0:-1:2], [int(i) for i in entry[1:8:2]]
#print(notas)

# Verifica se todos os monitores desejados
while ((not "Júnior" in nomes) or (not "Henrique" in nomes) or  (not "Miguel" in nomes) or (not "Guilherme" in nomes)):
    #print(f"O nome {nomes[i]} não é de um monitor.")
    print(f"Insira nomes válidos.") # Saída obrigatória
    entry = input().split(", ")
    nomes, notas = entry[0:-1:2], [int(i) for i in entry[1:8:2]]

#print(f"Todos os nomes são de monitores 👍")
# --------------------------------------
allPassed = True if (notas == [10, 10, 10, 10]) else False
nmPior = nomes[notas.index(min(notas))]

for j in range(4):
    if (notas[j] == 10): print(f"O monitor {nomes[j]} é diferenciado! Teve a aprovação do próprio Jamal.")
if (not allPassed):
    # Retorna o Nome do Monitor com menor Nota
    print(f"Jamal avaliou a situação dos monitores e viu que {nmPior} é o mais necessitado.")
# ------------------------------------

# Validação do movimento dos pés
movPes = input().split(", ")
newAttempt, qErrors= False, 0

# Verificação dos Movimentos (E ou D) | Tem 7 movimentos
if (len(movPes) != 7):
    qErrors += 1
    newAttempt = True
    print("Quatidade de movimentos diferente de 7!")
# Percorre toda a lista de movimentos e verifica se existe apenas (E ou D) e (1 < m ou n < 4)
#print(f"{movPes}")
for i in range(7):
    if (("E" != movPes[i][0] and "D" != movPes[i][0]) or 
        (3 < int(movPes[i][1]) < 1) or (3 < int(movPes[i][2]) < 1)):
        newAttempt = True
        qErrors += 1
        '''print(f"Letra errada: {movPes[i][0]} | Posição na entrada: {i}")
        qErrors += 1
        print(f"Index da matriz errado!: {movPes[i][1:3]} | Posição na entrada: {i} | Num erros: {qErrors}")'''
if (newAttempt): print(f"Movimento inválido! Por favor, insira outro.")
# ----------------------------------------

# Treinamento do Jamal
presetJamal = ["D12", "D33", "E12", "E31", "D12", "E31", "D12"]
movOutJamal = f"\nJamal - Movimentação 0:\n" + f". . .\n"+f". . .\n"+f"E . D\n"+f"\nJamal - Movimentação 1:\n"+f". 1 .\n"+f". . .\n"+f"E . .\n"+f"\nJamal - Movimentação 2:\n"+f". . .\n"+f". . .\n"+f"E . 2\n"+f"\nJamal - Movimentação 3:\n"+f". 3 .\n"+f". . .\n"+f". . D\n"+f"\nJamal - Movimentação 4:\n"+f". . .\n"+f". . .\n"+f"4 . D\n"+f"\nJamal - Movimentação 5:\n"+f". 5 .\n"+f". . .\n"+f"E . .\n"+f"\nJamal - Movimentação 6:\n"+f". D .\n"+f". . .\n"+f"6 . .\n"+f"\nJamal - Movimentação 7:\n"+f". 7 .\n"+f". . .\n"+f"E . .\n"
# Saídas obrigatórias do Jamal
print(f"Jamal - \"Vou ensinar apenas uma vez, então preste atenção.\"")
print(f"{movOutJamal}")
# --------------------------

# Saídas do monitor
movOutMonitor = f"{nmPior} - Movimentação 0:\n" + f". . .\n"+f". . .\n"+f"E . D\n"+f"\n{nmPior} - Movimentação 1:\n"+f". 1 .\n"+f". . .\n"+f"E . .\n"+f"\n{nmPior} - Movimentação 2:\n"+f". . .\n"+f". . .\n"+f"E . 2\n"+f"\n{nmPior} - Movimentação 3:\n"+f". 3 .\n"+f". . .\n"+f". . D\n"+f"\n{nmPior} - Movimentação 4:\n"+f". . .\n"+f". . .\n"+f"4 . D\n"+f"\n{nmPior} - Movimentação 5:\n"+f". 5 .\n"+f". . .\n"+f"E . .\n"+f"\n{nmPior} - Movimentação 6:\n"+f". D .\n"+f". . .\n"+f"6 . .\n"+f"\n{nmPior} - Movimentação 7:\n"+f". 7 .\n"+f". . .\n"+f"E . .\n"
print(f"{movOutMonitor}")

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
        print(f"{movOutJamal}")
        if (movPes == presetJamal): 
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