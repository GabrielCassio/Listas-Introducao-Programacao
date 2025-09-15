note1   = float(input())
note2   = float(input())
note3   = float(input())

numClasses  = int(input())
numFauls    = int(input())

avarage     = (note1 + note2 + note3) / 3
attendence  = ((numClasses - numFauls) / numClasses) * 100

print(f"Chris, você conseguiu média {avarage:.2f} e {attendence:.2f}% de presença.")

if (avarage >= 8.0 and attendence >= 75.0):
    print(f"Chris está APROVADO por nota e por presença! 🎉\nPisante maneiro, Chris! Agora é só torcer pros outros não vacilarem.")
elif (avarage >= 7.0 and avarage < 8.0 and attendence >= 75.0):
    print(f"Chris está APROVADO! ✅\nSacomé, né? Passou raspando, mas a pizza ainda ficou longe.")
elif (avarage >= 7.0 and attendence < 75.0):
    print(f"Chris ESTÁ REPROVADO por FALTA. ❌\nTrágico! Não adianta só saber, tem que aparecer.")
elif(avarage < 7.0 and attendence > 75.0):
    print(f"Chris ESTÁ REPROVADO por NOTA. ❌\nChris, já pro seu quarto ou eu vou te bater até você virar o avesso!")
else:
    print(f"Chris ESTÁ REPROVADO por NOTA e por FALTA. ❌\nChris, você perdeu o juízo? Eu trouxe você para esse mundo e posso muito bem tirar você dele.")