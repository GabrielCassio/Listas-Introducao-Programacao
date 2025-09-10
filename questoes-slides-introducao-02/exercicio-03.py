val1    = int(input())
val2    = int(input())
valIntermed =   0
if (val1 > val2):
    valIntermed =   val1
    val1        = val2
    val1        = valIntermed

print(f"{val1} | {val2}")
