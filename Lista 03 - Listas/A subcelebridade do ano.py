print(f"Sejam bem-vindos à Big Sub Brasil, onde a fama é temporária, os barracos são eternos, e só um vai conquistar o título de maior subcelebridade do país!")

participantes = [x.strip() for x in input().split(",")]
participantes[0], participantes[1] = participantes[0].capitalize(), participantes[1].capitalize()

jog, restos = [[[], [], []], [[], [], []]], []

for i in range(2):
    numsAleatorio = sorted([int(x) for x in input().split(" ")])
    jog[i][0] = sorted([numsAleatorio.pop(numsAleatorio.index(max(numsAleatorio))) for x in range(3)])
    jog[i][1] = [numsAleatorio.pop(numsAleatorio.index(min(numsAleatorio))) for x in range(3)]
    jog[i][2] = [numsAleatorio.pop(numsAleatorio.index(x)) + 1 for x in  numsAleatorio[:3]]
    restos.append(numsAleatorio[0])

# Cálculo determinante
# Lembrar de tentar fazer pelo método de eliminação de gauss
det = [
        (jog[0][0][0] * jog[0][1][1] * jog[0][2][2] + jog[0][0][1] * jog[0][1][2] * jog[0][2][0] + jog[0][0][2] * jog[0][1][0] * jog[0][2][1]) - (jog[0][0][2] * jog[0][1][1] * jog[0][2][0] + jog[0][0][1] * jog[0][1][0] * jog[0][2][2] + jog[0][0][0] * jog[0][1][2] * jog[0][2][1]),

       (jog[1][0][0] * jog[1][1][1] * jog[1][2][2] + jog[1][0][1] * jog[1][1][2] * jog[1][2][0] + jog[1][0][2] * jog[1][1][0] * jog[1][2][1]) - (jog[1][0][2] * jog[1][1][1] * jog[1][2][0] + jog[1][0][1] * jog[1][1][0] * jog[1][2][2] + jog[1][0][0] * jog[1][1][2] * jog[1][2][1])
    ]

print(f"{participantes[0]} e {participantes[1]} disputarão entre si.")

for part in  range(2):
    for i in range(3):
        print(f"{jog[part][i][0]} {jog[part][i][1]} {jog[part][i][2]}")
    print(f"{participantes[part]} está com pontuação {det[part]} pontos.")

if (det[0] != det[1]):
    indexVencedor = det.index(max(det))
    print(f"Com talento duvidoso e esforço máximo, a vitória é de {participantes[indexVencedor]}!")
else:
    print(f"RODADA DESEMPATE!!")
    if (restos[0] != restos[1]):
        indexVencedor = restos.index(max(restos))
        print(f"Contra todas as expectativas (inclusive as nossas), {participantes[indexVencedor]} venceu a rodada!")
        print(f"Seu momento de brilhar virou eclipse {participantes[indexVencedor - 1]}. Melhor sorte no próximo flop!")
        print(f"Com talento duvidoso e esforço máximo, a vitória é de {participantes[indexVencedor]}!")
    else:
        print(f"Como isso é possível?? Os participantes empataram até na rodada desempate! EU DESISTO!!!")