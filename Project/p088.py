# 
# Solução para o problema do Projeto Euler 88

# minSumProduto[k] é o menor integer positivo que pode ser escrito como uma soma e um produto da mesma coleção de k integer positivos.
# Por exemplo, minSumProduto[3] = 6 porque 6 = 1 + 2 + 3 = 1 * 2 * 3, e este é o número mínimo possível para 3 termos.
# 
# Para todos os k >= 2:
# - minSumProduto[k] > k porque 1 + ... + 1 (com k termos) = k, que é a soma mínima de k inteiros positivos,
# mas o produto é 1 que é desigual de k, portanto k não é uma solução válida.
# - minSumProduto[k] <= 2k porque 1 + ... + 1 + 2 + k (com k termos no total) = (k - 2) + 2 + k = 2k. O produto é 2k, o que equivale à soma.
# Como se trata de uma solução alcançável, a solução mínima não deve ser maior que isto.
# - Além disso: minSumProduto[k] não é um número primo. Suponha que minSumProduto[k] = p, onde p é prime. Então p só pode ser fatorizado como p, p * 1, p * 1 * 1, etc.
# Assim, sempre que a fatorização tem mais de um termo, a soma excede p, o que a torna desigual para o produto.
# 
# Portanto, precisamos considerar todos os números de 2 a LIMIT*2 e fatorizá-los de todas as maneiras possíveis para encontrar todas as soluções relevantes.
def compute():
	LIMIT = 12000
	minsumproduct = [None] * (LIMIT + 1)
	
	# Calcula todas as fatorizações do número inteiro n >= 2 e atualiza soluções menores em minSumProduto.
	# Por exemplo, 12 podem ser fatorizados da seguinte forma - e as duplicatas são eliminadas ao encontrar apenas seqüências não crescentes de fatores:
	# - 12 = 12. (1 termo)
	# - 12 = 6 * 2 * 1 * 1 * 1 * 1 = 6 + 2 + 1 + 1 + 1 + 1. (6 termos)
	# - 12 = 4 * 3 * 1 * 1 * 1 * 1 * 1 = 4 + 3 + 1 + 1 + 1 + 1 + 1. (7 termos)
	# - 12 = 3 * 2 * 2 * 1 * 1 * 1 * 1 * 1 = 3 + 2 + 2 + 1 + 1 + 1 + 1 + 1. (8 termos)
	def factorize(n, remain, maxfactor, sum, terms):
		if remain == 1:
			if sum > n:  # Sem utilizar fatores de 1, a soma nunca excede o produto
				raise AssertionError()
			terms += n - sum
			if terms <= LIMIT and (minsumproduct[terms] is None or n < minsumproduct[terms]):
				minsumproduct[terms] = n
		else:
			# Nota: maxfactor <= permanece
			for i in range(2, maxfactor + 1):
				if remain % i == 0:
					factor = i
					factorize(n, remain // factor, min(factor, maxfactor), sum + factor, terms + 1)
	
	for i in range(2, LIMIT * 2 + 1):
		factorize(i, i, i, 0, 0)
	
	# Eliminar duplicatas e computar a soma
	ans = sum(set(minsumproduct[2 : ]))
	return str(ans)


if __name__ == "__main__":
	print(compute())