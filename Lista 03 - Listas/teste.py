tab = []
for i in range(9):
    tabLiine = input().split()
    tab.append(tabLiine)

finalMatrix = ""
for length in range(9):
    finalMatrix += " ".join(tab[length])+"\n"


print(f"{finalMatrix}")


print(not '.' in finalMatrix)