# 
# Solução para o problema do Projeto Euler 182

import fractions, sys
if sys.version_info.major == 2:
	xrange = range


def compute():
	P = 1009
	Q = 3643
	TOTIENT = (P - 1) * (Q - 1)
	numunconcealedp = count_all_unconcealed(P)
	numunconcealedq = count_all_unconcealed(Q)
	minunconcealedp = min(numunconcealedp)
	minunconcealedq = min(numunconcealedq)
	
	ans = sum(e for e in range(TOTIENT) if
		numunconcealedp[e % (P - 1)] == minunconcealedp and
		numunconcealedq[e % (Q - 1)] == minunconcealedq)
	return str(ans)


def count_all_unconcealed(prime):
	result = []
	for e in range(prime - 1):
		if fractions.gcd(e, prime - 1) == 1:
			result.append(count_unconcealed(prime, e))
		else:
			result.append(10**20)
	return result


def count_unconcealed(modulus, e):
	result = 0
	for m in range(modulus):
		if pow(m, e, modulus) == m:
			result += 1
	return result


if __name__ == "__main__":
	print(compute())