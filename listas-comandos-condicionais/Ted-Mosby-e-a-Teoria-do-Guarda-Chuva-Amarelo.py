# Coordenadas de Ted
x1  = int(input())
y1  = int(input())
# Coordenadas do Guarda-Chuva Amarelo
x2  = int(input())
y2  = int(input())

nameAmigo          = input() # Nome do amigo
distanciaOriginal  = ((x2-x1)**2 + (y2-y1)**2)**0.5 # Distância até o guarda-chuva
distanciaFinal     = 0

# Ajuste da distância final
if (nameAmigo == "Barney"):     distanciaFinal  = distanciaOriginal + 10
elif (nameAmigo == "Marshall"): distanciaFinal  = distanciaOriginal - 5
elif (nameAmigo == "Lily"):     distanciaFinal  = distanciaOriginal - 10
else:                           distanciaFinal  = distanciaOriginal + 5

print(f"Pelos meus cálculos a distância final encontrada foi {round(distanciaFinal)}!")

if (distanciaFinal <= 50):
    if (nameAmigo == "Barney"): print(f"Nossa, eu sou incrível! Vimos o guarda-chuva em 5 minutos. Tão lendário que eu poderia até ter pego ele pra mim! Desafio aceito!")
    elif (nameAmigo == "Marshall"): print(f"Obrigado pela ajuda, Marsh! Tão bom saber que a gente pode contar com os amigos pra achar a nossa cara-metade. Encontramos o guarda-chuva!")
    elif (nameAmigo == "Lily"): print(f"Ah! Não te falei? Peguei um atalho! Lilypad sabe das coisas. O guarda-chuva está aqui, e nem nos cansamos muito!")
    else: print(f"Bem... acho que isso realmente aconteceu. Nem foi tão difícil assim. O guarda-chuva está bem aqui, Ted. Onde está o mistério?")
else:
    if (nameAmigo == "Barney"): print(f"Esse não era o caminho para o guarda-chuva, mas com certeza é o caminho para uma noite lendária! Challenge accepted, vista seu terno!")
    elif (nameAmigo == "Marshall"):print(f"Tudo bem, cara. O destino é paciente. O importante é que estamos juntos nessa. Vamos tentar de novo amanhã.")
    elif (nameAmigo == "Lily"): print(f"Isso não faz sentido! Meu atalho deveria ter funcionado! Que saco! Fiquei com fome de tanta caminhada.")
    else: print(f"Sério, Ted? Um guarda-chuva? O destino é um conceito abstrato.")