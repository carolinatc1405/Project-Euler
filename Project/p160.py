# 
# Solução para o problema do Projeto Euler 160

def compute():
	ans = factorial_suffix(10**12)
	return str(ans)


# Os últimos 5 dígitos de n!, excluindo os zeros traiçoeiros.
def factorial_suffix(n):
	twos = count_factors(n, 2) - count_factors(n, 5)  # Sempre não-negativo para cada n
	# Podemos reduzir 'dois' porque há um ciclo: 2^5 = 2^2505 = 32 mod 100000
	if twos >= 2505:
		twos = (twos - 5) % 2500 + 5
	return factorialish(n) * pow(2, twos, 100000) % 100000


# Igual a n! mas com todos os fatores de 2 e 5 removidos e depois modulo 10^5.
# A identidade factorialIsh(n) = odd_factorialish(n) * even_factorialish(n) (mod 10^5) é verdadeira por definição.
def factorialish(n):
	return even_factorialish(n) * odd_factorialish(n) % 100000


# O produto de {todos os números pares de 1 a n}, mas com todos os fatores de 2 e 5 removidos e depois modulo 10^5.
# Por exemplo, mesmo_factorialish(9) considera apenas os números {2, 4, 6, 8}. Dividir cada número por 2 para obter {1, 2, 3, 4}. Assim, even_factorialish(9) = factorialish(4).
def even_factorialish(n):
	if n == 0:
		return 1
	else:
		return factorialish(n // 2)


# O produto de {todos os números ímpares de 1 a n}, mas com todos os fatores de 2 e 5 removidos e depois modulo 10^5.
# Por definição, odd_factorialish() nunca considera qualquer número que tenha um fator 2. O produto dos números que não sejam múltiplos de 5 são acumulados por factorial_coprime().
# Aqueles que são múltiplos de 5 são tratados recursivamente por odd_factorialish(), observando que ainda são ímpares após a divisão por 5.

def odd_factorialish(n):
	if n == 0:
		return 1
	else:
		return odd_factorialish(n // 5) * factorial_coprime(n) % 100000


# O produto de {todos os números de 1 a n que são coprime com 10}, modulo 10^5.
# O argumento de entrada pode ser tomado modulo 10^5 porque factorialoid(10^5) = 1, e cada bloco de 10^5 números se comporta da mesma forma.
def factorial_coprime(n):
	n %= 100000
	product = 1
	for i in range(1, n + 1):
		if i % 2 != 0 and i % 5 != 0:
			product = i * product % 100000
	return product


# Conta o número de fatores de n no conjunto de inteiros {1, 2, ..., fim}.
# Por exemplo, count_factors(25, 5) = 6 porque {5, 10, 15, 20} cada um tem um fator de 5, e 25 tem dois fatores de 5.
def count_factors(end, n):
	if end == 0:
		return 0
	else:
		return end // n + count_factors(end // n, n)


if __name__ == "__main__":
	print(compute())