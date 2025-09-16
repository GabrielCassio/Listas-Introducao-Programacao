print(f"Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele\nQuantos dos amigos dele conseguirão ajudar dessa vez?")
# Número de pessoas que irão ao encontro 
quantidadePessoas   = int(input())

# Possíveis nomes para o encontro
nome1   = ""
nome2   = ""
nome3   = ""
nome4   = ""
nomes   = ""
# Possível lugar para encontro
lugar   = ""
frase   = ""

quantMediaCerva = 0
quantTotalCerva = 0

if (quantidadePessoas > 0):
    print(f"Hora da lista dos amigos da vez!")
    if (quantidadePessoas == 1):
        nome1   = input()
        if (nome1 == "Barney"): print(f"Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif (nome1 == "Robin"): print(f"Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif (nome1 == "Marshall"): print(f"O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif (nome1 == "Lily"): print(f"Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else: print(f"{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
        nomes   = nome1
    elif (quantidadePessoas == 2):
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
        # Verificando se duplas de amigos acompanhando
        if((nome1 == "Marshall" or nome1 == "Lily") and
           (nome2 == "Marshall" or nome2 == "Lily")):
            print(f"Nada melhor que um casal para dar conselhos de relacionamento.")
        if((nome1 == "Barney" or nome1 == "Marshall") and
           (nome2 == "Barney" or nome2 == "Marshall")):
            print(f"Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")
        nomes   = nome1 + nome2
    elif (quantidadePessoas == 3):
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
        nomes   = nome1 + nome2 + nome3
    else:
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
        nomes   =   nome1 + nome2 + nome3 + nome4
        if (("Marshall" in nomes) and ("Lily" in nomes) and ("Robin" in nomes) and ("Barney" in nomes)):
            print(f"O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”.")
    # Lugar do encontro
    lugar   = input()
elif (quantidadePessoas == 0):
    lugar   = "MacLaren's Pub"

# Outputs especiais relacionando nomes com lugar escolhido:
if (("Barney" in nomes) and (lugar == "Arena de Laser Tag")):
    print(f"Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.")
elif (("Robin" == nomes) and (lugar == "Carmichael’s")):
    print(f"Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")
elif (lugar == "MacLaren's Pub"):
    quantMediaCerva = int(input())
    # Cálculo das Cervas
    quantTotalCerva = quantMediaCerva * (quantidadePessoas + 1)
    if ((("Marshall" in nomes) or ("Lily" in nomes) or ("Robin" in nomes) or ("Barney" in nomes))):
        print(f"Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
    elif(not(("Marshall" in nomes) and ("Lily" in nomes) and ("Robin" in nomes) and ("Barney" in nomes))):
        print(f"Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.")

# Frases envolvendo a quantidade de pessoas:
if (quantidadePessoas == 1):
    frase   = "Saideira de um pra um. Nada melhor do que uma pessoa pra ouvir seus problemas."
elif (quantidadePessoas == 2):
    frase   = "Duas pessoas se compadeceram com a situação do pobre Ted."
elif (quantidadePessoas == 3):
    frase   = "Três pessoas! Ted conseguiu se divertir bastante."
elif((quantidadePessoas == 4) and
     (("Marshall" in nomes) and ("Lily" in nomes) and ("Robin" in nomes) and ("Barney" in nomes))):
    frase   = "O quinteto junto consegue resolver qualquer problema!"
else:
    frase   = "Saiu um quinteto um pouco diferente do que a gente tá acostumado, mas no fim conseguiram deixar Ted alegre."

# Relatório final:
if (quantidadePessoas > 0): 
    print(f"\nRelatório da situação de Ted:")
    if (quantidadePessoas == 1):
        print(f"- Ted foi consolado por: {nome1}.")
    elif (quantidadePessoas == 2):
        print(f"- Ted foi consolado por: {nome1} e {nome2}.")
    elif (quantidadePessoas == 3):
        print(f"- Ted foi consolado por: {nome1}, {nome2} e {nome3}.")
    elif (quantidadePessoas == 4):
        print(f"- Ted foi consolado por: {nome1}, {nome2}, {nome3} e {nome4}.")

    print(f"- O local de afogar as mágoas foi: {lugar}.\n"
        f"- {frase}.")
    if (lugar == "MacLaren's Pub"): print(f"- Quantidade de cervejas bebidas pelo grupo: {quantTotalCerva} cervejas.")
    print(f"Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?")

elif (quantidadePessoas == 0):
        print(f"\nRelatório da situação de Ted:\n"
            f"Ted foi para o MacLaren’s… Olhe em volta, Ted, você está sozinho.\n"
            f"- Quantidade de cervejas bebidas por Ted: {quantTotalCerva} cervejas.")
