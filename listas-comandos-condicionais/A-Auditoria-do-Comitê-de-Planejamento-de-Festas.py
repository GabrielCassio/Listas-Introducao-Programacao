# O programa recebe 1 item e suas propriedades
nomeItem            = input().lower()
valorItem           = float(input())
valorItem           = 0 if (valorItem < 0) else valorItem
responsavelCompra   = input().lower()
tipoEvento          = input().lower()

# Verifica se esse item vale mais do que 100.0 conto
# Regras 1 - angela -----

if (valorItem > 100.0):
    # Só Aprova a compra se quem fez ela foi angela
    if (responsavelCompra == "angela"):
        print(f"Compra Aprovada!\nApenas eu tenho discernimento para gastos desta magnitude.")
    else:
        print(f"Compra Reprovada!\nGasto excessivo e irresponsável! Onde está a disciplina fiscal?!")
elif ((valorItem <= 100.0) and
      (responsavelCompra == "angela")):
    print(f"Compra Aprovada!\nCompra feita por mim, obviamente dentro dos padrões de excelência.")
# ------------------------
# Regras 2 - michael
elif ((responsavelCompra == "michael") and
      (nomeItem == "mágica" or nomeItem == "fantasia")):
    print(f"Compra Reprovada!\nO Comitê não financia frivolidades e palhaçadas, Michael.")
elif ((responsavelCompra == "michael") and
      (valorItem > 60.0)):
    print(f"Compra Aprovada com ressalvas!")
    if (tipoEvento == "natal"):
        print(f"O espírito natalino de Michael é... excessivo. A nota será conferida.")
    elif (tipoEvento == "aniversario"):
        print(f"Michael nunca gasta tanto nos aniversários dos funcionários, deve ser o dele!")
elif ((responsavelCompra == "michael") and
      (valorItem <= 60.0)):
    print(f"Compra Aprovada!\nUma compra surpreendentemente sensata vinda do Michael. Suspeito.")
# -----------------------
# Regras 3 - Halloween ----
elif (tipoEvento == "halloween"):
    if ((nomeItem == "abóbora") and
        (valorItem <= 30.0)):
        print(f"Compra Aprovada!\nUma abóbora de tamanho e custo razoáveis. Eficiente.")
    elif ((nomeItem == "abóbora") and
          (valorItem > 30.0)):
        print(f"Compra Aprovada com ressalvas!\nPor que uma abóbora precisa ser tão cara? Extravagância.")
    else:
        print(f"Compra Aprovada com ressalvas!\nDecoração de Halloween... Tenho certeza que Phyllis exagerou de novo.")
# -----------------------
# Regras 4 - Aniversário ----
elif (tipoEvento == "aniversario"):
    if((nomeItem == "bolo") and
       (valorItem <= 40.0)):
        print(f"Compra Aprovada!\nUm bolo modesto para celebrar mais um ano de produtividade, parabéns!")
    elif ((nomeItem == "sorvete de menta com chocolate")):
        print(f"Compra Reprovada!\nEste sabor de sorvete é uma abominação e não entrará em meu evento.")
    elif ((valorItem <= 100.0) or
          (nomeItem == "bolo" and (40 < valorItem <= 100))):
        print(f"Compra Aprovada!\nItens de aniversário devem ser práticos, não uma distração do trabalho.")
# ----------------------
# Regras 5 - Exceções ----
else:
    if ((valorItem > 50.0)):
        print(f"Compra Aprovada com ressalvas!\nEstá dentro do orçamento, mas não quer dizer que não vou verificar!")
    else:
        print(f"Compra Aprovada!\nEsta compra não viola nenhum regulamento... por enquanto.")


'''
elif ((tipoEvento == "halloween") and
      (nomeItem == "abóbora") and
      (valorItem <= 30.0)):
    print(f"Compra Aprovada!\nUma abóbora de tamanho e custo razoáveis. Eficiente.")
elif ((tipoEvento == "halloween") and
      (nomeItem == "abóbora") and
      (valorItem > 30.0)):
    print(f"Compra Aprovada com ressalvas!\nPor que uma abóbora precisa ser tão cara? Extravagância.")
elif ((tipoEvento == "halloween") and
      (nomeItem != "abóbora")):
    print(f"Compra Aprovada com ressalvas!\nDecoração de Halloween... Tenho certeza que Phyllis exagerou de novo.")

elif ((tipoEvento == "aniversario") and
      (nomeItem == "bolo") and
      (valorItem <= 40.0)):
    print(f"Compra Aprovada!\nUm bolo modesto para celebrar mais um ano de produtividade, parabéns!")
elif ((tipoEvento == "aniversario") and
      (nomeItem == "sorvete de menta com chocolate")):
    print(f"Compra Reprovada!\nEste sabor de sorvete é uma abominação e não entrará em meu evento.")
elif ((tipoEvento == "aniversario") and
    (valorItem <= 100.0) and
    (nomeItem != "bolo")):
    print(f"Compra Aprovada!\nItens de aniversário devem ser práticos, não uma distração do trabalho.")
'''