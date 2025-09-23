# Parte 1 - Outputs Iniciais
print(f"Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele…")
print(f"Quantos dos amigos dele conseguirão ajudar dessa vez?")
# --------------------------
# Variáveis de caso
quantidadePessoas                               = int(input())
nomes, nome1, nome2, nome3, nome4, lugar, frase = "", "", "", "", "", "", ""
quantMediaCerva, quantTotalCerva                = 0, 0
sozinhoTed  = False
# -----------------

# Caso em que Ted está sozinho
if (quantidadePessoas == 0):
    sozinhoTed      = True
    lugar           = "MacLaren’s Pub"
# -----------------------------
elif (quantidadePessoas == 1):
    # Nomes dos Amigos
    print(f"Hora da lista dos amigos da vez!")
    nome1   = input()
    if (nome1 == "Barney"): print(f"Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif (nome1 == "Robin"): print(f"Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif (nome1 == "Marshall"): print(f"O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif (nome1 == "Lily"): print(f"Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else: print(f"{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    lugar   = input()
elif (quantidadePessoas == 2):
    # Nomes dos Amigos
    print(f"Hora da lista dos amigos da vez!")
    nome1   = input()
    if (nome1 == "Barney"): print(f"Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif (nome1 == "Robin"): print(f"Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif (nome1 == "Marshall"): print(f"O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif (nome1 == "Lily"): print(f"Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else: print(f"{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    nome2   = input()
    if (nome2 == "Barney"): print(f"Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif (nome2 == "Robin"): print(f"Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif (nome2 == "Marshall"): print(f"O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif (nome2 == "Lily"): print(f"Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else: print(f"{nome2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    lugar   = input()
elif (quantidadePessoas == 3):
    # Nomes dos Amigos
    print(f"Hora da lista dos amigos da vez!")
    nome1   = input()
    if (nome1 == "Barney"): print(f"Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif (nome1 == "Robin"): print(f"Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif (nome1 == "Marshall"): print(f"O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif (nome1 == "Lily"): print(f"Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else: print(f"{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    nome2   = input()
    if (nome2 == "Barney"): print(f"Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif (nome2 == "Robin"): print(f"Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif (nome2 == "Marshall"): print(f"O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif (nome2 == "Lily"): print(f"Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else: print(f"{nome2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    nome3   = input()
    if (nome3 == "Barney"): print(f"Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif (nome3 == "Robin"): print(f"Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif (nome3 == "Marshall"): print(f"O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif (nome3 == "Lily"): print(f"Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else: print(f"{nome3} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    lugar   = input()
elif (quantidadePessoas == 4):
    # Nomes dos Amigos
    print(f"Hora da lista dos amigos da vez!")
    nome1   = input()
    if (nome1 == "Barney"): print(f"Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif (nome1 == "Robin"): print(f"Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif (nome1 == "Marshall"): print(f"O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif (nome1 == "Lily"): print(f"Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else: print(f"{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    nome2   = input()
    if (nome2 == "Barney"): print(f"Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif (nome2 == "Robin"): print(f"Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif (nome2 == "Marshall"): print(f"O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif (nome2 == "Lily"): print(f"Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else: print(f"{nome2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    nome3   = input()
    if (nome3 == "Barney"): print(f"Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif (nome3 == "Robin"): print(f"Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif (nome3 == "Marshall"): print(f"O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif (nome3 == "Lily"): print(f"Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else: print(f"{nome3} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    nome4   = input()
    if (nome4 == "Barney"): print(f"Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif (nome4 == "Robin"): print(f"Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif (nome4 == "Marshall"): print(f"O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif (nome4 == "Lily"): print(f"Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else: print(f"{nome4} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    lugar   = input()

if (lugar == "MacLaren’s Pub"): 
    quantMediaCerva = int(input())
    quantTotalCerva = quantMediaCerva * (quantidadePessoas + 1)

if (not(sozinhoTed)):
    # Após receber todos os nomes:
    nomes = nome1 + nome2 + nome3 + nome4
    if (("Marshall" in (nomes) and "Lily" in (nomes)) and
        (quantidadePessoas == 2)):
        print(f"Nada melhor que um casal para dar conselhos de relacionamento.")
    elif (("Barney" in (nomes) and "Marshall" in (nomes)) and
        (quantidadePessoas == 2)):
        print(f"Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")
    elif ("Barney" in (nomes) and "Robin" in (nomes) and "Marshall" in (nomes) and "Lily" in (nomes)):
        print(f"O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”.")
    # --------------------------

    # Verfica se o lugar da saidera já foi preenchida pelo caso (quantidadePessoas == 0)
    if ("Barney" in nomes and lugar == "Arena de Laser Tag"):
        print(f"Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.")
    elif ((quantidadePessoas == 1) and (nome1 == "Robin") and (lugar == "Carmichael’s")):
        print(f"Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")
    elif (("Barney" in nomes or "Robin" in nomes or "Marshall" in nomes or "Lily" in nomes) and
        (lugar == "MacLaren’s Pub")):
        print(f"Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
    elif (lugar == "MacLaren’s Pub" and not("Barney" in (nomes)) and not("Robin" in (nomes)) and not("Marshall" in (nomes)) and not("Lily" in (nomes))):
        print(f"Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.")

# Output por quantidade de pessoas
if (quantidadePessoas == 1):
    frase   = "Saideira de um pra um. Nada melhor do que uma pessoa pra ouvir seus problemas."
elif (quantidadePessoas == 2):
    frase   = "Duas pessoas se compadeceram com a situação do pobre Ted."
elif (quantidadePessoas == 3):
    frase   = "Três pessoas! Ted conseguiu se divertir bastante."
elif (quantidadePessoas == 4):
    if ("Barney" in (nomes) and "Robin" in (nomes) and "Marshall" in (nomes) and "Lily" in (nomes)):
        frase   = "O quinteto junto consegue resolver qualquer problema!"
    else:
        frase   = "Saiu um quinteto um pouco diferente do que a gente tá acostumado, mas no fim conseguiram deixar Ted alegre."

# Relatório Final
if (quantidadePessoas == 0):
    print()
    print(f"Relatório da situação de Ted:")
    print(f"Ted foi para o MacLaren’s… Olhe em volta, Ted, você está sozinho.")
    print(f"- Quantidade de cervejas bebidas por Ted: {quantTotalCerva} cervejas.")
elif (1 <= quantidadePessoas <= 4):
    print()
    print(f"Relatório da situação de Ted:")
    if (quantidadePessoas == 1):
        print(f"- Ted foi consolado por: {nome1}.")
    elif (quantidadePessoas == 2):
        print(f"- Ted foi consolado por: {nome1} e {nome2}.")
    elif (quantidadePessoas == 3):
        print(f"- Ted foi consolado por: {nome1}, {nome2} e {nome3}.")
    elif (quantidadePessoas == 4):
        print(f"- Ted foi consolado por: {nome1}, {nome2}, {nome3} e {nome4}.")

    print(f"- O local de afogar as mágoas foi: {lugar}.")
    print(f"- {frase}")

    if (lugar == "MacLaren’s Pub"): print(f"- Quantidade de cervejas bebidas pelo grupo: {quantTotalCerva} cervejas.")
    print(f"Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?")