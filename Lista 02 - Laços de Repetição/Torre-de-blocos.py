# Inputs Iniciais
n   = int(input())

for niveis in range(n):
    # Para cada nível da pirâmide temos o equivalente em espaços brancos " "    = número total de andares - valor do nível atual    
    # Para cada nível da pirâmide temos o equiavalente em hashtags "#"          = quantidade igual ao ímpares
    print(f'{(n-niveis) * "⠀"}{(2*niveis + 1) * "#"}')