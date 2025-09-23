# Número de artigos
numArtgSheldon  = int(input())
numArtgLeonard  = int(input())
numArtgRaj      = int(input())
numArtgHoward   = int(input())
# Número de experiências
numExpSheldon   = int(input())
numExpLeonard   = int(input())
numExpRaj       = int(input())
numExpHoward    = int(input())

# Cálculo da Pontuação
pointSheldon    = (numArtgSheldon * 2) + (numExpSheldon * 3)
pointLeonard    = (numArtgLeonard * 2) + (numExpLeonard * 3)
pointRaj        = (numArtgRaj * 2) + (numExpRaj * 3)
pointHoward     = (numArtgHoward * 2) + (numExpHoward * 3)

# Pontuação total da competição
print(f"Pontuação final:\nSheldon: {pointSheldon}\nLeonard: {pointLeonard}\nRaj: {pointRaj}\nHoward: {pointHoward}\n")

# Avaliação do vencedor -------------------------------------
'''
Para avaliar a pountação entre os 4 elementos, devo comparar a pontuação deles e distribuí-los em colocações 
para facilitar a lógica
'''
maiorPontuacao  =   max(pointSheldon, pointLeonard, pointRaj, pointHoward)

# Caso 1: Todos estão empatados, mas Sheldon está contido nesse conjunto
if (pointSheldon == maiorPontuacao):
    '''
    Esse caso engloba se Sheldon empata com uma pessoa ou mais e se ele tem a maior pontuação sozinho
    '''
    print(f"O cientista da semana é: Sheldon\nNão é atoa que ele ganhou o prêmio Nobel")
else :
    # Caso2.1: Em que Sheldon não é o maior pontuador
    # Verifica quem é o maior pontuador
    if (pointLeonard == maiorPontuacao):
        print(f"O cientista da semana é: Leonard\nA vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.")
    elif (pointRaj == maiorPontuacao):
        print(f"O cientista da semana é: Raj\nEle comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres.")
    else:
         print(f"O cientista da semana é: Howard\nUm pequeno passo para a ciência, um grande salto para alguém com mestrado.")
    
    '''
    # Caso 2.0 (Não otimizado): Se todos menos Sheldon estão empatados
    if (maiorPontuacao == pointLeonard == pointRaj == pointHoward):
        print(f"O cientista da semana é: Leonard\nA vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.")
    elif (maiorPontuacao == pointLeonard == pointRaj):
        print(f"O cientista da semana é: Leonard\nA vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.")
    elif (maiorPontuacao == pointLeonard == pointHoward):
        print(f"O cientista da semana é: Leonard\nA vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.")
    elif (maiorPontuacao == pointRaj == pointHoward):
        print(f"O cientista da semana é: Raj\nEle comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres.")
    else:
        # Caso 3: Ninguém está empatado
        if (maiorPontuacao == pointLeonard):
            print(f"O cientista da semana é: Leonard\nA vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.")
        elif (maiorPontuacao == pointRaj):
            print(f"O cientista da semana é: Raj\nEle comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres.")
        elif (maiorPontuacao == pointHoward):
            print(f"O cientista da semana é: Howard\nUm pequeno passo para a ciência, um grande salto para alguém com mestrado.")
    '''