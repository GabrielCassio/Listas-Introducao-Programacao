# Algoritmo de Chebyshev para contínuos vetores
'''
def DistChebyshev (position1: list, position2:list) -> list:
   result = 0
   for i in range(len(position1)):   
      d = abs(position1[i] - position2[i])
      result = max(result, d)
   return result

# Para apenas X e Y
def DistChebyshev (position1: list, position2:list) -> list:
   result max(abs(position1[0] - position2[0]), abs(position1[1] - position2[1]))
   
'''
# Algoritmo de Chebyshev para um vetor fixo e um conjunto finito de outros vetores
def DistChebyshev (position1: list, position2: list) -> list:
   result = 0
   indexChebyshev = [0] * 2
   matrixLength = len(position2)
   for i in range(matrixLength):   
      d1 = abs(position1[0] - position2[i][0])
      d2 = abs(position1[1] - position2[i][1])
      curDist = max(d1, d2)
      if (curDist >= result):
         result = curDist
         indexChebyshev = position2[i]
   return indexChebyshev