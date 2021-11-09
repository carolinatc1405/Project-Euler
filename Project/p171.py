# 
# Solução para o problema do Projeto Euler 171

import eulerlib, itertools


# A chave é usar uma programação dinâmica para construir a resposta um dígito de cada vez.
# 
# Diga Num(n, s) o conjunto de números de comprimento n (com zeros à esquerda) cuja soma dos dígitos ao quadrado é s.
# Por exemplo, Num(2, 25) = {05, 34, 43, 50}.
# Então, para qualquer n e s em particular, sabemos que Num(n, s) = união de
# (prepende 0 para cada um de Num(n-1, s - 0*0)),
# (prepende 1 para cada um de Num(n-1, s - 1*1)),
# ...,
# (prepende 9 para cada um de Num(n-1, s - 9*9)).
# 
# No entanto, o acompanhamento desses conjuntos de números é tão lento quanto a iteração
# todos os números por força bruta. Portanto, ao invés disso, armazenamos apenas as somas e contagens destes conjuntos,
# e estas duas informações são suficientes para determinar a resposta final.
# (Além disso, estas podem ser reduzidas pelo módulo).
def compute():
	LENGTH = 20
	BASE = 10
	MODULUS = 10**9
	
	# Soma máxima possível de dígitos quadrados (para 99...99)
	MAX_SQR_DIGIT_SUM = (BASE - 1)**2 * LENGTH
	
	# sqsum[n][s] é a soma de todos os números de comprimento-n com uma soma de dígitos quadrados de s, modulo MODULUS
	# count[n][s] é a contagem de todos os números de comprimento-n com uma soma de dígitos quadrados de s, modulo MODULUS
	sqsum = []
	count = []
	
	for i in range(LENGTH + 1):
		sqsum.append([0] * (MAX_SQR_DIGIT_SUM + 1))
		count.append([0] * (MAX_SQR_DIGIT_SUM + 1))
		if i == 0:
			count[0][0] = 1
		else:
			for j in range(BASE):
				for k in itertools.count():
					index = k + j**2
					if index > MAX_SQR_DIGIT_SUM:
						break
					sqsum[i][index] = (sqsum[i][index] + sqsum[i - 1][k] + pow(BASE, i - 1, MODULUS) * j * count[i - 1][k]) % MODULUS
					count[i][index] = (count[i][index] + count[i - 1][k]) % MODULUS
	
	ans = sum(sqsum[LENGTH][i**2] for i in range(1, eulerlib.sqrt(MAX_SQR_DIGIT_SUM)))
	return "{:09d}".format(ans % MODULUS)


if __name__ == "__main__":
	print(compute())