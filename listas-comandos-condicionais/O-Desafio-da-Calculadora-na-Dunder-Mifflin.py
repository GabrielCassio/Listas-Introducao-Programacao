x, y = int(input()), int(input())
operator    = input()
z           = 0
print(f"x: {x}, y: {y}")

if (operator == "+"):
    z = x + y
elif (operator == "-"):
    z = x - y
elif (operator == "*"):
    z = x - y
elif (operator == "/"):
    z = x // y
else:
    print(f"Alerta! Alguém tentou usar um operador que não existe. Só um idiota faria isso. Provavelmente o Jim. Isso é claramente uma tentativa de sabotagem corporativa.")
