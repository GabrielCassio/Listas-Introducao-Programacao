'''
Maicon Kuster - Não à fofoca
Sem repetição de comidas - diversidade gastronômica
comida mais cara - reconhecimento especial
comida mais barata - feeback constrututivo
'''

numConvidados, nameConvidados, vet2Comidas  = int(input()), [], [ [], # Nome das Comidas
                                                                  []  # Valor das Comidas
                                                                ]

for convidado in range(numConvidados):
    name = input()
    nameDish = input()
    value = int(input())
    
    # Regra Para Expulsar Maicon kuster
    if ("Maicon Kuster" == name):
        print(f"você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!")
    # Verifica se é um prato repetido
    elif (nameDish in vet2Comidas[0]):
        print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {name}")
    else:
        nameConvidados.append(name)
        vet2Comidas[0].append(nameDish)
        vet2Comidas[1].append(value)


# Caso niguém vá para a festa do calabreso
if (len(nameConvidados) == 0): print(f"Nenhum convidado marcou presença na festa do calabreso!")
elif (len(nameConvidados) == 1): print(f"Obrigado para o(a) {nameConvidados[0]} pelo(a) excelente {vet2Comidas[0][0]}")
else:
    idGrastestValue, idLowestValue = vet2Comidas[1].index(max(vet2Comidas[1])), vet2Comidas[1].index(min(vet2Comidas[1]))
    # Sort dos valores
    # Saída da pessoa que trouxe a comida mais cara
    print(f"Obrigado para o(a) {nameConvidados[idGrastestValue]} pelo(a) excelente {vet2Comidas[0][idGrastestValue]}")
    # Saída da pessoa que trouxe a comida mais barata
    print(f"Rapaz, {nameConvidados[idLowestValue]} trouxe o(a) {vet2Comidas[0][idLowestValue]} que estava altamente mais ou menos!!!")