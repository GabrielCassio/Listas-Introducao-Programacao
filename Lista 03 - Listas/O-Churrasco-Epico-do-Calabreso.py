numConvidados, nameConvidados, vet2Comidas  = int(input()), [], [   [], # Valor das Comidas
                                                                    []  # Nome das Comidas
                                                                ]
for convidado in range(numConvidados):
    name = input()
    nameDish = input()
    value = int(input())
    
    # Regra Para Expulsar Maicon kuster
    if ("Maicon Kuster" == name):
        print(f"você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!")
        numConvidados -= 1
    # Verifica se é um prato repetido
    elif (nameDish in vet2Comidas[1]):
        print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {name}")
        numConvidados -= 1
    else:
        nameConvidados.append(name)
        vet2Comidas[0].append(value)
        vet2Comidas[1].append(nameDish)

# Selection Sorting modficado
for i in range(len(vet2Comidas[0])):
    minValue = min(vet2Comidas[0][i:])
    idmin = vet2Comidas[0].index(minValue, i)
    if (vet2Comidas[0][idmin] < vet2Comidas[0][i]): 
        vet2Comidas[0][i], vet2Comidas[0][idmin] = vet2Comidas[0][idmin], vet2Comidas[0][i]
        vet2Comidas[1][i], vet2Comidas[1][idmin] = vet2Comidas[1][idmin], vet2Comidas[1][i]
        nameConvidados[i], nameConvidados[idmin] = nameConvidados[idmin], nameConvidados[i]

# Ordenamento lexográfico por selection sorting
# Melhora a eficiência se eu não usar o list comprehension do python
indexEquals = [index for index in range(numConvidados) if vet2Comidas[0].count(vet2Comidas[0][index]) > 1]
palavras    = [nameConvidados[index][0] for index in range(numConvidados) if vet2Comidas[0].count(vet2Comidas[0][index]) > 1]

for i in range(len(palavras)):
    minValue = min(palavras[i:])
    idmin = palavras.index(minValue, i)
    if (palavras[idmin] < palavras[i]):
        palavras[i], palavras[idmin] = palavras[idmin], palavras[i]
        vet2Comidas[1][indexEquals[i]], vet2Comidas[1][indexEquals[idmin]] = vet2Comidas[1][indexEquals[idmin]], vet2Comidas[1][indexEquals[i]]
        nameConvidados[indexEquals[i]], nameConvidados[indexEquals[idmin]] = nameConvidados[indexEquals[idmin]], nameConvidados[indexEquals[i]]

# Caso niguém vá para a festa do calabreso
printON = True
if (len(nameConvidados) == 0): 
    printON = False
    print(f"Nenhum convidado marcou presença na festa do calabreso!")
elif (len(nameConvidados) == 1): 
    print(f"Obrigado para o(a) {nameConvidados[0]} pelo(a) excelente {vet2Comidas[1][0]}")
else:
    # Saída da pessoa que trouxe a comida mais cara
    print(f"Obrigado para o(a) {nameConvidados[numConvidados-1]} pelo(a) excelente {vet2Comidas[1][numConvidados-1]}")
    # Saída da pessoa que trouxe a comida mais barata
    print(f"Rapaz, {nameConvidados[0]} trouxe o(a) {vet2Comidas[1][0]} que estava altamente mais ou menos!!!")


# Output final
if (printON):
    print(f"Lista de convidados do Calabreso")
    for i in range(numConvidados):
        print(f"{i + 1}- {nameConvidados[i]}")