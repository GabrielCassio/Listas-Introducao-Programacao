numRodadas  = int(input())

palavraSecreta, palavraFantasma  = input(), input()

numLetrasDiferentes1, numLetrasDiferentes2, letraGurdada1, letraGurdada2 = 0, 0, "", ""
for letra in palavraSecreta:
    if (letraGurdada1 == ""): letraGurdada1  = letra
    else:
        if (letra != letraGurdada1):
            numLetrasDiferentes1 += 1
            letraGurdada1 = letra
        
