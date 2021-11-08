# 
# Solução para o problema do Projeto Euler 78

import itertools


MODULUS = 10**6

def compute():
	partitions = [1]
	for i in itertools.count(len(partitions)):
		# Calculamos as partições[i] mod 10^6 usando uma fórmula baseada em números pentagonais generalizados:
		# partições(i) = partições(i - pentagonal(1)) + partições(i - pentagonal(-1))
		# - divisórias(i - pentagonal(2)) - divisórias(i - pentagonal(-2))
		# + divisórias(i - pentagonal(3)) + divisórias(i - pentagonal(-3))
		# - divisórias(i - pentagonal(4)) - divisórias(i - pentagonal(-4))
		# + ...,
		# onde pentagonal(j) = (3*n^2 - n) / 2, e
		# paramos a soma quando i - pentagonal(+/-j) < 0.
		# observamos que para j > 0, pentagonal(j) < pentagonal(-j) < pentagonal(j+1).
		# 
		item = 0
		for j in itertools.count(1):
			sign = -1 if j % 2 == 0 else +1
			index = (j * j * 3 - j) // 2
			if index > i:
				break
			item += partitions[i - index] * sign
			index += j  # índice == (j * j * 3 + j) // 2
			if index > i:
				break
			item += partitions[i - index] * sign
			item %= MODULUS
		
		# Verificar ou memorizar o número
		if item == 0:
			return str(i)
		partitions.append(item)


if __name__ == "__main__":
	print(compute())