qnf = int(input()) # num frases novas | num frase nova
afs = [["Que tiro foi esse?", 1], ["Segura a marimba", 1], ["Tá com raiva? Morde as costas", 1], ["Bateu de frente é só rajadão", 1]]

for i in range(qnf):
    n = input()
    adt = True
    for j in range(len(afs)):
        if (n in afs[j]): 
            adt = False
            afs[j][1] += 1

    if (adt):
        afs.append([])
        afs[-1].append(n)
        afs[-1].append(1)

for i in range(len(afs)):
    print(f'"{afs[i][0]}": {afs[i][1]}')
lo = [afs[x][0] for x in range(len(afs)) for i in range(afs[x][1])]
lo.sort()
print(lo)