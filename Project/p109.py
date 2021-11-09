# 
# Solução para o problema do Projeto Euler 109

def compute():
	# Ambas as listas não estão ordenadas, mas as duplicatas são importantes; são como multisets
	points = [i * j for i in range(1, 21) for j in range(1, 4)] + [25, 50]
	doublepoints = [i * 2 for i in range(1, 21)] + [25 * 2]
	
	# matriz de memorização, com dimensões (3, 101, len(pontos))
	ways = [[[None] * len(points) for j in range(101)] for i in range(3)]
	
	# Número de formas de obter pontos exatamente 'totais' em lançamentos exatamente 'throwz', usando
	# itens (não ordenados) da lista de 'pontos' com índice menor ou igual a 'maxIndex'.
	def calc_ways(throws, total, maxindex):
		if ways[throws][total][maxindex] is None:
			if throws == 0:
				result = 1 if total == 0 else 0
			else:
				result = 0
				if maxindex > 0:
					result += calc_ways(throws, total, maxindex - 1)
				if points[maxindex] <= total:
					result += calc_ways(throws - 1, total - points[maxindex], maxindex)
			ways[throws][total][maxindex] = result
		return ways[throws][total][maxindex]
	
	checkouts = 0
	for remainingpoints in range(1, 100):
		for throws in range(3):
			for p in doublepoints:
				if p <= remainingpoints:
					checkouts += calc_ways(throws, remainingpoints - p, len(points) - 1)
	return str(checkouts)


if __name__ == "__main__":
	print(compute())