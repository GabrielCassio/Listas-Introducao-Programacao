# Status de Jake
casos               = int(input())
dias                = int(input())
assistenciasCasos   = int(input())
operacoesCampo      = int(input())

# Informações da Operação Especial
operacaoEspecial     = input()

# Soma ponderada
soma    = ((casos * 2) + (assistenciasCasos * 1.5) + (operacoesCampo * 0.5))

# Avaliação de casos com operação especial
if (operacaoEspecial == "sim"):
    tipoOperacaoEspecial    = input()
    if (tipoOperacaoEspecial == "Infiltração"):
        soma    += (soma*0.5)
    elif (tipoOperacaoEspecial == "Escuta"):
        soma    += (soma*0.3)
    elif (tipoOperacaoEspecial == "Invasão"):
        soma    += (soma*0.2)
    else:
        soma    += (soma*0.1)

# Localizaçãod de Jake 
localizacao = input()

# Média diária de casos
mediaCasos  = (casos/dias)

# Classificação Status
statusJake  = True

# Requisito 1
if (localizacao == "Manhattan" or localizacao == "Brooklyn"):
    print(f"Pelo menos nos bairros corretos Jake está!")
else:
    statusJake  = False
    print(f"Os casos não são nas áreas designadas por Holt. Peralta está desclassificado!")
# Requisito 2
if (statusJake):
    if (casos >= 20):
        print(f"Detetive Peralta bateu o mínimo de casos, ele ainda está dentro da competição.")
    else:
        statusJake  = False
        print(f"Vishh, Jake já foi eliminado por não ter o mínimo de casos necessários.")
# Requisito 3
if (statusJake):
    if (mediaCasos > 0.5):
        print(f"Parece que Jake é bem consistente na sua média diária de casos.")
    else:
        statusJake = False
        print(f"A média diária de casos tá muito baixa, Peralta foi desclassificado.")
# Requisito 4
if (statusJake):
    if (assistenciasCasos >= 5):
        print(f"Peralta ajudou bastante outros detetives, ele ainda está na competição!")
    else:
        statusJake  = False
        print(f"Desclassificado! Jake precisa ajudar mais os companheiros.")
# Requisito 5
if (statusJake):
    if (operacoesCampo >= 20):
        print(f"Jake ainda sobrevive por sua participação em campo, será que ele vai levar pra casa o prêmio?")
    else:
        statusJake  = False
        print(f"Peralta precisa sair mais da delegacia, está faltando ação em campo!")

if (statusJake):
    if (operacaoEspecial == "sim"): print(f"Minha nossa! Jake Peralta é realmente um detetive diferenciado.")
    else: print(f"Para que operação especial quando se tem números, não é?")

    if (soma >= 70):
        print(f"Jake é candidato forte ao prêmio. Será que Holt vai premiá-lo?")
    elif (40 <= soma <= 69):
        print(f"Muito bem! Mas ainda é incerto se vai ser suficiente para ganhar o prêmio.")
    elif (soma < 40):
        print(f"Muito difícil de Jake ganhar o prêmio.")