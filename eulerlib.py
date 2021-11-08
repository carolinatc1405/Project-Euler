

import array, math, sys
if sys.version_info.major == 2:
 xrange = range



# Retorna o número de 1's na representação binária de
# o inteiro não-negativo x. Também conhecido como peso Hamming.
def popcount(x):
	return bin(x).count("1")


# Dado o número inteiro x, isto retorna o piso inteiro(sqrt(x)).
def sqrt(x):
	assert x >= 0
	i = 1
	while i * i <= x:
		i *= 2
	y = 0
	while i > 0:
		if (y + i)**2 <= x:
			y += i
		i //= 2
	return y


# Testa se x é um quadrado perfeito, para qualquer número inteiro x.
def is_square(x):
	if x < 0:
		return False
	y = sqrt(x)
	return y * y == x


# Testa se o número inteiro dado é um número primo.
def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, sqrt(x) + 1, 2):
			if x % i == 0:
				return False
		return True


# Retorna uma lista de Verdadeiro e Falso indicando se cada número é primo.
# Para 0 <= i <= n, resultado[i] é Verdadeiro se i é um número primo, Falso caso contrário.
def list_primality(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(sqrt(n) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result


# Devolve todos os números primos menores ou iguais a n, em ordem ascendente.
# Por exemplo: listPrimes(97) = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ..., 83, 89, 97].
def list_primes(n):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]


# Produz números primos em ordem ascendente de 2 até o limite (inclusive).
def prime_generator(limit):
	if limit >= 2:
		yield 2
	
	# Armazenando apenas números ímpares a partir de 3
	isprime = array.array("B", b"\x01" * ((limit - 1) // 2))
	sieveend = sqrt(limit)
	for i in range(len(isprime)):
		if isprime[i] == 1:
			p = i * 2 + 3
			yield p
			if i <= sieveend:
				for j in range((p * p - 3) >> 1, len(isprime), p):
					isprime[j] = 0


def list_smallest_prime_factors(n):
	result = [None] * (n + 1)
	limit = sqrt(n)
	for i in range(2, len(result)):
		if result[i] is None:
			result[i] = i
			if i <= limit:
				for j in range(i * i, n + 1, i):
					if result[j] is None:
						result[j] = i
	return result


def list_totients(n):
	result = list(range(n + 1))
	for i in range(2, len(result)):
		if result[i] == i:  # i is prime
			for j in range(i, len(result), i):
				result[j] -= result[j] // i
	return result


def binomial(n, k):
	assert 0 <= k <= n
	return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


# Retorna x^-1 mod m. Note que x * x^-1 mod m = x^-1 * x mod m = 1.
def reciprocal_mod(x, m):
	assert 0 <= x < m
	
	# Com base numa simplificação do algoritmo Euclidiano ampliado
	y = x
	x = m
	a = 0
	b = 1
	while y != 0:
		a, b = b, a - x // y * b
		x, y = y, x % y
	if x == 1:
		return a % m
	else:
		raise ValueError("Reciprocal does not exist")


def next_permutation(arr):
	# Encontre um sufixo que não aumente
	i = len(arr) - 1
	while i > 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i <= 0:
		return False
	
	# Encontre um sucessor para pivotar
	j = len(arr) - 1
	while arr[j] <= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	
	# Sufixo inverso
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return True


# Decorador. A função subjacente deve levar apenas argumentos posicionais, sem argumentos de palavras-chave.
class memoize(object):
	
	def __init__(self, func):
		self.func = func
		self.cache = {}
	
	def __call__(self, *args):
		if args in self.cache:
			return self.cache[args]
		else:
			val = self.func(*args)
			self.cache[args] = val
			return val