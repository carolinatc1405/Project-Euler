# 
# Solução para o problema do Projeto Euler 60


import eulerlib


def compute():
	PRIME_LIMIT = 100000 # Corte arbitrário inicial
	primes = eulerlib.list_primes(PRIME_LIMIT)
	
	
	# Tenta encontrar qualquer conjunto adequado e devolver sua soma, ou nenhuma se nenhuma for encontrada.
	# Um conjunto é adequado se contiver apenas primos, seu tamanho é o alvo,
	# sua soma é menor ou igual a um limite de soma, e cada par concatena a um primo.
	# o 'prefixo' é um conjunto de índices ascendentes para o conjunto de 'primos',
	# que descreve o conjunto encontrado até agora.
	# A função assume cegamente que cada par de primos em 'prefixo' concatena a um primo.
	# 
	# Por exemplo, find_set_sum([1, 3, 28], 5, 10000) significa "encontrar a soma de qualquer conjunto
	# onde o conjunto tem tamanho 5, consiste de primos com os elementos mais baixos sendo [3, 7, 109],
	# tem soma de 10000 ou menos, e tem cada par concatenado para formar um primo".
	def find_set_sum(prefix, targetsize, sumlimit):
		if len(prefix) == targetsize:
			return sum(primes[i] for i in prefix)
		else:
			istart = 0 if (len(prefix) == 0) else (prefix[-1] + 1)
			for i in range(istart, len(primes)):
				if primes[i] > sumlimit:
					break
				if all((is_concat_prime(i, j) and is_concat_prime(j, i)) for j in prefix):
					prefix.append(i)
					result = find_set_sum(prefix, targetsize, sumlimit - primes[i])
					prefix.pop()
					if result is not None:
						return result
			return None
	
	
	# Testa se concat(primes[x], primes[y]) é um número primo, com memorização.
	@eulerlib.memoize
	def is_concat_prime(x, y):
		return is_prime(int(str(primes[x]) + str(primes[y])))
	
	
	# Testa se o número inteiro dado é o principal. A implementação realiza a divisão experimental,
	# primeiro usando a lista de primes chamada 'primes', depois mudando para incrementação simples.
	# Isto requer que o último número em 'primes' (se houver) seja um número ímpar.
	def is_prime(x):
		if x < 0:
			raise ValueError()
		elif x in (0, 1):
			return False
		else:
			end = eulerlib.sqrt(x)
			for p in primes:
				if p > end:
					break
				if x % p == 0:
					return False
			for i in range(primes[-1] + 2, end + 1, 2):
				if x % i == 0:
					return False
			return True
	
	
	sumlimit = PRIME_LIMIT
	while True:
		setsum = find_set_sum([], 5, sumlimit - 1)
		if setsum is None:  # Não foi encontrada uma soma menor
			return str(sumlimit)
		sumlimit = setsum


if __name__ == "__main__":
	print(compute())