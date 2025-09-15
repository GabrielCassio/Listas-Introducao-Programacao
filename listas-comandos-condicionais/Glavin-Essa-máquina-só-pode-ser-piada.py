print(f"Ativando a máquina...")
name    = input().capitalize()
year    = int(input())

if (year % len(name) == 0):
    if (name == "Frink"): print(f"Professor Frink irá inventar o rebigulador?! A máquina deve estar com defeito! Glavin!")
    else: print(f"Previsão confiável! O rebigulador será real em {year}!")
else:
    if (name == "Frink"): print(f"Nem precisava colocar os dados! O rebigulador jamais existiria em qualquer universo!")
    else: print(f"Previsão instável! {name} também deve achar que o rebigulador é ridículo...")