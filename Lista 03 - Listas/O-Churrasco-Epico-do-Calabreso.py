'''
Maicon Kuster - Não à fofoca
Sem repetição de comidas - diversidade gastronômica
comida mais cara - reconhecimento especial
comida mais barata - feeback constrututivo
'''

numConvidados, nameConvidados, vet2Comidas  = int(input()), [], [ [], # Valor das Comidas
                                                                  []  # Nome das Comidas
                                                                ]

for convidado in range(numConvidados):
    name = input()
    nameDish = input()
    value = int(input())
    
    # Regra Para Expulsar Maicon kuster
    if ("Maicon Kuster" == name):
        print(f"você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!")
    # Verifica se é um prato repetido
    elif (nameDish in vet2Comidas[1]):
        print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {name}")
    else:
        nameConvidados.append(name)
        vet2Comidas[0].append(value)
        vet2Comidas[1].append(nameDish)

# Caso niguém vá para a festa do calabreso
if (len(nameConvidados) == 0): print(f"Nenhum convidado marcou presença na festa do calabreso!")
elif (len(nameConvidados) == 1): print(f"Obrigado para o(a) {nameConvidados[0]} pelo(a) excelente {vet2Comidas[0][0]}")
else:
    idGrastestValue, idLowestValue = vet2Comidas[0].index(max(vet2Comidas[0])), vet2Comidas[0].index(min(vet2Comidas[0]))
    # Sort dos valores
    # Saída da pessoa que trouxe a comida mais cara
    print(f"Obrigado para o(a) {nameConvidados[idGrastestValue]} pelo(a) excelente {vet2Comidas[1][idGrastestValue]}")
    # Saída da pessoa que trouxe a comida mais barata
    print(f"Rapaz, {nameConvidados[idLowestValue]} trouxe o(a) {vet2Comidas[1][idLowestValue]} que estava altamente mais ou menos!!!")


# Sorting

for i in range(len(vet2Comidas[0])):
    minValue = min(vet2Comidas[0][i:])
    idmin = vet2Comidas[0].index(minValue, i)
    if (vet2Comidas[0][idmin] < vet2Comidas[0][i]):
        vet2Comidas[0][i], vet2Comidas[0][idmin] = vet2Comidas[0][idmin], vet2Comidas[0][i]
        vet2Comidas[1][i], vet2Comidas[1][idmin] = vet2Comidas[1][idmin], vet2Comidas[1][i]
        nameConvidados[i], nameConvidados[idmin] = nameConvidados[idmin], nameConvidados[i]


# Ordenamento lexográfico pós sorting geral
lenVectWord, currentWord = (len(nameConvidados) - 1), 0
while (currentWord < lenVectWord):
    if (vet2Comidas[0][currentWord] == vet2Comidas[0][currentWord + 1]): # Verifica condição de empate entre pontuação
        findLowest, length, letter = False, min(len(nameConvidados[currentWord]), len(nameConvidados[currentWord+1])), 0 # Condição crescente de lexografia
        while (letter < length and not findLowest): # Varre as palavras
            if nameConvidados[currentWord][letter] > nameConvidados[currentWord + 1][letter]:
                findLowest, nameConvidados[currentWord], nameConvidados[currentWord + 1] = True, nameConvidados[currentWord + 1], nameConvidados[currentWord]
                vet2Comidas[1][currentWord], vet2Comidas[1][currentWord + 1] = vet2Comidas[1][currentWord + 1], vet2Comidas[1][currentWord]
            elif (nameConvidados[currentWord][letter] < nameConvidados[currentWord + 1][letter]):
                findLowest = True
            letter += 1
    currentWord += 1


# Output final
print(f"Lista de convidados do Calabreso")
for i in range(lenVectWord + 1):
    print(f"{i + 1}- {nameConvidados[i]}")
