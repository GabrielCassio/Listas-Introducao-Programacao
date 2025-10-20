nmMonitors = ["Júnior", "Henrique", "Miguel", "Guilherme"]
entry = input().split(", ")
nomes, notas = entry[0:-1:2], [int(i) for i in entry[1:len(entry):2]]
print(notas)

# Verifica se todos os monitores desejados
for i in range(len(nomes)):
    while (not nomes[i] in nmMonitors):
        #print(f"O nome {nomes[i]} não é de um monitor.")
        nomes[i] = input()

#print(f"Todos os nomes são de monitores 👍")
# --------------------------------------

indexMinValue = notas.index(min(notas))
movPes = input().split(", ")

# Verificação dos Movimentos (E ou D) | Tem 7 movimentos
if (len(movPes) != 7):
    pass
