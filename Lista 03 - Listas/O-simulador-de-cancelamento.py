# Essa quesão também não terá minemônicos e as demais também n
# Pq? Pq sim 👌
print(f"--- Simulador de Cancelamento ---\n")
n = int(input())
inf = []

for i in range(n):
    inp  = input().split(" - ")
    nm, s = inp[0], int(inp[1])
    #print(inp)
    inf.append([])
    inf[i].append(nm)
    inf[i].append(s)
    inf[i].append(i)

for j in range(n):
    print(f"A subcelebridade da vez é: {inf[j][0]}")
    e = int(input())
    inf[j].append(e)
    if (e == 1):
        print(f"{inf[j][0]} perdeu 10% dos seguidores!")
        inf[j][1] = int(0.9*inf[j][1])
    elif (e == 2):
        print(f"{inf[j][0]} ganhou 5% de seguidores!")
        inf[j][1] = int(1.05*inf[j][1])
    elif (e == 3):
        print(f"{inf[j][0]} perdeu 15% dos seguidores!")
        inf[j][1] = int(0.85*inf[j][1])
    else:
        print(f"Nenhum evento relevante. Seguidores continuam os mesmos.")
    
print(f"\n--- RANKING FINAL DE SEGUIDORES ---")

# Apliccation Bubble Sorting
for i in range(n):
    for j in range(0, n-1):
        if (inf[j][1] < inf[j+1][1]):
            inf[j], inf[j+1] = inf[j+1], inf[j]
        elif (inf[j][1] == inf[j+1][1]):
            if (inf[j][2] > inf[j+1][2]):
                inf[j], inf[j+1] = inf[j+1], inf[j]

n = n if n < 3 else 3
for i in range(n):
    print(f"{i+1}º Lugar: {inf[i][0]} com {inf[i][1]} seguidores.")
