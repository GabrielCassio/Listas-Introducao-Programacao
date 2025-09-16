'''
x, operator, y = int(input()), input(), int(input())
if (y != 0):    print(x + y)  if (operator == "+") else print(x - y) if (operator == "-") else print(x * y) if (operator == "*") else print(x // y) if (operator == "/") else  print(f"Alerta! Alguém tentou usar um operador que não existe. Só um idiota faria isso. Provavelmente o Jim. Isso é claramente uma tentativa de sabotagem corporativa.")
else: print(f"Alerta! Alguém tentou usar um operador que não existe. Só um idiota faria isso. Provavelmente o Jim. Isso é claramente uma tentativa de sabotagem corporativa.")
'''

x, operator, y, z = int(input()), input(), int(input()), 0
z = (x + y)  if (operator == "+") else (x - y) if (operator == "-") else (x * y) if (operator == "*") else ((x // y) if (operator == "/") else print(f"Alerta! Alguém tentou usar um operador que não existe. Só um idiota faria isso. Provavelmente o Jim. Isso é claramente uma tentativa de sabotagem corporativa.")) if (y != 0) else print(f"Alerta! Alguém tentou usar um operador que não existe. Só um idiota faria isso. Provavelmente o Jim. Isso é claramente uma tentativa de sabotagem corporativa.")
if (z != None): print(f"{z}")