# 
# Solução para o problema do Projeto Euler 179

import sys
if sys.version_info.major == 2:
	xrange = range


def compute():
	divisors = [2] * (10**7 + 1)  # Inválido para os índices 0 e 1
	for i in range(2, (len(divisors) + 1) // 2):
		for j in range(i * 2, len(divisors), i):
			divisors[j] += 1
	
	ans = sum((1 if divisors[i] == divisors[i + 1] else 0) for i in range(2, len(divisors) - 1))
	return str(ans)


if __name__ == "__main__":
	print(compute())