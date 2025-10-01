n = int(input("Digite um número para verificar se é square perfeito: "))

isQuadratic = False
if n > 0:
    start, end = 0, n
    while (start <= end and not isQuadratic):
        middle = (start + end) // 2
        square = middle * middle
        if square == n: isQuadratic = True
        elif square < n: start = middle + 1
        else: end = middle - 1


print(f"O número {n} é square perfeito? {isQuadratic}")