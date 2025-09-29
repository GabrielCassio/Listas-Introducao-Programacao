predio1, predio2, predio3 = "CFCH", "CTG", "CIN"

# Nomes dos procuradores
nome1, pontuacao1   = input(), 0
nome2, pontuacao2   = input(), 0
nome3, pontuacao3   = input(), 0
# ----------------------

# Variáveis de Busca
fimBusca    = False
# ------------------

# Iniciando a Brincadeira
print(f"Vai começar o esconde-esconde UFPE 2025!")
# -----------------------

# Buscas de cada procurador
for procurador in range (3):
    # Saída inicial para cada procurador
    if (procurador == 0): print(f"\nProntos ou não, lá vai {nome1}.")
    elif (procurador == 1): print(f"\nProntos ou não, lá vai {nome2}.")
    else: print((f"\nProntos ou não, lá vai {nome3}."))
    # ---------------------------------

    # Busca em cada prédio
    for predio in range(3):
        # Saída inicial para cada prédio
        if (procurador == 0):
            if (predio == 0): print(f"Agora {nome1} procurará no {predio1}.")
            elif (predio == 1): print(f"Agora {nome1} procurará no {predio2}.")
            else: print(f"Agora {nome1} procurará no {predio3}.")
        elif (procurador == 1): 
            if (predio == 0): print(f"Agora {nome2} procurará no {predio1}.")
            elif (predio == 1): print(f"Agora {nome2} procurará no {predio2}.")
            else: print(f"Agora {nome2} procurará no {predio3}.")
        else:
            if (predio == 0): print(f"Agora {nome3} procurará no {predio1}.")
            elif (predio == 1): print(f"Agora {nome3} procurará no {predio2}.")
            else: print(f"Agora {nome3} procurará no {predio3}.")
        # ------------------------------
        while (not fimBusca):
            estadoBusca = input()

            if (estadoBusca == "Achou uma pessoa!"):
                if (procurador == 0): 
                    pontuacao1 += 1
                    print(f"{nome1} achou uma pessoa!")
                elif (procurador == 1):
                    pontuacao2 += 1
                    print(f"{nome2} achou uma pessoa!")
                else:
                    pontuacao3 += 1
                    print(f"{nome3} achou uma pessoa!")
            elif (estadoBusca == "Fim da busca nesse prédio."):
                fimBusca    = True

        fimBusca    = False
    # ---------------------
# -------------------------

maiorPontuador, nomeVencedor  = max(pontuacao1, pontuacao2, pontuacao3), ""
if (maiorPontuador !=  0):
    if (maiorPontuador == pontuacao1): nomeVencedor = nome1
    elif (maiorPontuador == pontuacao2): nomeVencedor   = nome2
    else: nomeVencedor  = nome3
    print(f"\n{nomeVencedor} é o(a) melhor no esconde-esconde da UFPE!")
else: print(f"\nNinguém foi encontrado, nenhum dos buscadores ganhou a disputa.")
