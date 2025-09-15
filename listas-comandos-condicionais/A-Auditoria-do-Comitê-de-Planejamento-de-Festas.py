# Input iniciais
nameItem        = input().upper()
valueItem       = float(input())
respForItem     = input().upper()
typeEvent       = input().upper()

# Rules by Angela
# As regras de Angela
if (respForItem == "ANGELA"):
    if (valueItem > 100.0):
        print(f"Compra Aprovada!")
        print(f"Apenas eu tenho discernimento para gastos desta magnitude.")
    else:
        print(f"Compra Aprovada!")
        print(f"Compra feita por mim, obviamente dentro dos padrões de excelência.")

elif (valueItem > 100.0):
        print(f"Compra Reprovada!")
        print(f"Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!")

# Regras para Michael Scott
elif (respForItem == "MICHAEL"):
    if (nameItem == "MÁGICA" or nameItem == "FANTASIA"):
        print(f"Compra Reprovada!")
        print(f"O Comitê não financia frivolidades e palhaçadas, Michael.")
    elif (valueItem > 60.0):
        print(f"Compra Aprovada com ressalvas!")
        if (typeEvent == "NATAL"):
            print(f"O espírito natalino de Michael é... excessivo. A nota será conferida.")
        elif (typeEvent == "ANIVERSARIO"):
            print(f"Michael nunca gasta tanto nos aniversários dos funcionários, deve ser o dele!")
    else:
        print(f"Compra Aprovada!")
        print(f"Uma compra surpreendentemente sensata vinda do Michael. Suspeito.")

# Regras por Tipo de Evento
elif (typeEvent == "HALLOWEEN"):
    if (nameItem == "ABÓBORA" and valueItem <= 30.0):
        print(f"Compra Aprovada!")
        print(f"Uma abóbora de tamanho e custo razoáveis. Eficiente.")
    elif (nameItem == "ABÓBORA" and valueItem > 30.0):
        print(f"Compra Aprovada com ressalvas!")
        print(f"Por que uma abóbora precisa ser tão cara? Extravagância.")
    elif (valueItem <= 100):
        print(f"Compra Aprovada com ressalvas!")
        print(f"Decoração de Halloween... Tenho certeza que Phyllis exagerou de novo.")
elif (typeEvent == "ANIVERSARIO"):
    if (nameItem == "BOLO" and valueItem <= 40.0):
        print(f"Compra Aprovada!")
        print(f"Um bolo modesto para celebrar mais um ano de produtividade, parabéns!")
    elif (nameItem == "SORVETE DE MENTA COM CHOCOLATE"):
        print(f"Compra Reprovada!")
        print(f"Este sabor de sorvete é uma abominação e não entrará em meu evento.")
    else:
        print(f"Compra Aprovada!")
        print(f"Itens de aniversário devem ser práticos, não uma distração do trabalho.")

# Regra Geral
else:
    if (valueItem > 50.0):
        print(f"Compra Aprovada com ressalvas!")
        print(f"Está dentro do orçamento, mas não quer dizer que não vou verificar!")
    else:
        print(f"Compra Aprovada!")
        print(f"Esta compra não viola nenhum regulamento... por enquanto.")

'''
# Sua missão é desenvolver este programa de auditoria. O programa receberá quatro informações sobre uma despesa e,
# com base em um conjunto complexo de regras, decidirá se a compra é APROVADA, APROVADA COM RESSALVAS ou REPROVADA.
budget   = 100.0

# Outputs
print(f"Compra Aprovada!")
print(f"Compra Reprovada!")
print(f"Compra Aprovada com ressalvas!")
'''