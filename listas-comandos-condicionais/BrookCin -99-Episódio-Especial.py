casos               = int(input())
dias                = int(input())
assistenciasCasos   = int(input())
operacoesCampo      = int(input())
operacaoEspecial    = input()

pontuacaoFinal  = (casos * 2 + assistenciasCasos * 1.5 + operacoesCampo * 0.5) # Soma ponderada
mediaDiariaCasos     = (casos/dias)

if (operacaoEspecial == "sim"):
    tipoOperacaoEspecial    = input()
    localizacao             = input()

    # Verifica o tipo de operação e acresenta percentual
    if (tipoOperacaoEspecial == "Infiltração"):
        pontuacaoFinal += pontuacaoFinal * 0.5
    elif (tipoOperacaoEspecial == "Escuta"):
        pontuacaoFinal += pontuacaoFinal * 0.3
    elif (tipoOperacaoEspecial == "Invasão"):
        pontuacaoFinal += pontuacaoFinal * 0.2
    else:
        pontuacaoFinal += pontuacaoFinal * 0.1

    # Localização de Jake
    if (localizacao == "Manhattan" or localizacao == "Brooklyn"):
        print(f"Pelo menos nos bairros corretos Jake está!")
    else:
        print(f"Os casos não são nas áreas designadas por Holt. Peralta está desclassificado!")
    
    # Verifica número de casos
    if (casos >= 20):
        print(f"Detetive Peralta bateu o mínimo de casos, ele ainda está dentro da competição.")
    else:
        print(f"Vishh, Jake já foi eliminado por não ter o mínimo de casos necessários.")
    
    # Verifica média diária de casos
    if (mediaDiariaCasos >= 0.5):
        print(f"Parece que Jake é bem consistente na sua média diária de casos.")
    else:
        print(f"A média diária de casos tá muito baixa, Peralta foi desclassificado.")

    # Verifica média de assistências
    if (assistenciasCasos >= 5):
        print(f"Peralta ajudou bastante outros detetives, ele ainda está na competição!")
    else:
        print(f"Desclassificado! Jake precisa ajudar mais os companheiros.")

    # Verifica operações de campo
    if (operacoesCampo >= 20):
        print(f"Jake ainda sobrevive por sua participação em campo, será que ele vai levar pra casa o prêmio?")
    else:
        print(f"Peralta precisa sair mais da delegacia, está faltando ação em campo!")

    print(f"Minha nossa! Jake Peralta é realmente um detetive diferenciado.")
else:
    print(f"Para que operação especial quando se tem números, não é?")