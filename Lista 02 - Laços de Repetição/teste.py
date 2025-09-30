n  = int(input()) # Um número inteiro qualquer

# Para verificar se n é um númeor primo, podemos aplicar o corolário: Se um inteiro n > 1 for composto,
# então n possui um divisor primo p, tal que p ** 2 <= n, onde n = ab e  p | a or p | b
print(f"{5//2}")
isPrime =   True
if (n > 1):
    i   = 2
    while(i ** 2 <= n):
        if (n % i == 0):
            isPrime = False
        i += 1
else:
    isPrime = False

print(f"O número {n} é primo? {isPrime}")
































'''
numero  = int(input())
quadradoPerfeito    = numero % (numero ** 0.5) == 0 if (numero > 0) else 0
print(f"{numero} | {numero** 0.5} | {numero % (numero ** 0.5)}")
if (quadradoPerfeito): print(f"O número {numero} é quadrado perfeito")
else: print(f"O número não pe quadrado perfeito")
'''