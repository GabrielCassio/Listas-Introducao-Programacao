val1        = int(input())
val2        = int(input())
somaResult  = 0  # Valor total da soma

for diff in range((val2-val1)+1):
    print(f"{somaResult} | {val1} | {diff}")
    somaResult += (val1 + diff)

print(f"{somaResult}")