# 
# Solution to Project Euler problem 208

# Como o robô se move em arcos de 72 graus, ele só pode enfrentar 5 direções possíveis.
# - Definir a direção inicial para o norte como o inteiro 0.
# - Deixe cada movimento anti-horário (para a esquerda) adicionar 1 à direção, modulo 5.
# - Deixe cada movimento no sentido horário (para a direita) subtrair 1 da direção, modulo 5.
# 
# Em cada uma das 5 direções de face possíveis, há 2 movimentos possíveis.
# Qual é o deslocamento (x, y) de cada um desses 10 movimentos possíveis?
# 
# Podemos descobrir isso desenhando um círculo com 5 pontos uniformemente espaçados 72
# graus separados. Para alinhar com a descrição do problema, um dos pontos será
# estar no eixo positivo x. Para nossa conveniência, o círculo deve ter raio 4.
# fazendo alguma álgebra moderada e trigonometria, obtemos estas coordenadas de ponto:
# Ponto 0: (cos 0, sin 0)*4 = (+4, 0).
# - Ponto 1: (cos 72, sin 72)*4 = (+(sqrt(5)-1), +sqrt(10+2sqrt(5))).
# - Ponto 2: (cos 144, sin 144)*4 = (-(sqrt(5)+1), +sqrt(10-2sqrt(5))).
# - Ponto 3: (cos 216, sin 216)*4 = (-(sqrt(5)+1), -sqrt(10-2sqrt(5))).
# - Ponto 4: (cos 288, sin 288)*4 = (+(sqrt(5)-1), -sqrt(10+2sqrt(5))).
# (As entradas para cos e pecado são dadas em graus).
# 
# Esta seqüência de pontos é construída para que o vetor de deslocamento de
# ponto k a ponto k+1 é igual ao deslocamento de fazer um anti-horário
# move-se quando está de frente para a direção k. Por exemplo, (ponto1 - ponto0) é o
# deslocamento de um movimento no sentido anti-horário quando voltado para o norte (dir=0).
# Assim, os vetores de deslocamento dos 5 deslocamentos no sentido anti-horário são:
# - ponto1 - ponto0 = (-(5-sqrt(5)), +sqrt(10+2sqrt(5))).
# - ponto2 - ponto1 = (-2sqrt(5) , -2sqrt( 5-2sqrt(5))).
# - ponto3 - ponto2 = (0 , -2sqrt(10-2sqrt(5))).
# - ponto4 - ponto3 = (+2sqrt(5) , -2sqrt( 5-2sqrt(5))).
# - ponto0 - ponto4 = (+(5sqrt(5)), +sqrt(10+2sqrt(5))).
# Quanto aos movimentos no sentido horário, basta tomar os vetores de deslocamento acima e negar os valores x.
# O mapeamento dos vetores de deslocamento para estados de direção também precisa ser negado no módulo 5.
# 
# No total, temos esta tabela de movimentos válidos:
# Direção | Movimentação | x deslocamento | y deslocamento
# -----------+------+----------------+---------------------
# 0 | ACW | -(5-sqrt(5)) | +sqrt(10+2sqrt(5))
# 0 | CW | +(5-sqrt(5)) | +sqrt(10+2sqrt(5))
# 1 | ACW | -2sqrt(5) | -2sqrt(5-2sqrt(5))
# 1 | CW | -(5-sqrt(5)) | +sqrt(10+2sqrt(5))
# 2 | ACW | 0 | -2sqrt(10-2sqrt(5))
# 2 | CW | -2sqrt(5) | -2sqrt(5-2sqrt(5))
# 3 | ACW | +2sqrt(5) | -2sqrt(5-2sqrt(5))
# 3 | CW | 0 | -2sqrt(10-2sqrt(5))
# 4 | ACW | +(5-sqrt(5)) | +sqrt(10+2sqrt(5))
# 4 | CW | +2sqrt(5) | -2sqrt(5-2sqrt(5))
# Note que -2sqrt(5-2sqrt(5)) = sqrt(10-2sqrt(5)) - sqrt(10+2sqrt(5)).
# 
# À medida que o robô se move, ele adiciona x componentes e y componentes ao seu deslocamento.
# - A qualquer momento, a coordenada x é igual a um único inteiro ponderado
# soma de 2sqrt(5) e (sqrt(5)-5), ou seja i*2sqrt(5) + j*(sqrt(5)-5).
# Podemos mostrar que estes dois componentes irracionais não podem "simplificar"
# entre si - isto é, quando (i, j) != (0, 0), a soma deve ser diferente de zero.
# - A qualquer momento, a coordenada y é igual a um número inteiro único
# soma de sqrt(10-2sqrt(5)) e sqrt(10+2sqrt(5)). Assumiremos, sem prova, que
# estes dois componentes não "interagem" um com o outro ou se cancelam de qualquer forma.
def compute():
	LIMIT = 70
	
	# Devolve um novo tuple de estado.
	def move(state, sign):
		entry = ANTICLOCKWISE_MOVES[state[0] * sign % 5]
		return (
			(state[0] + sign) % 5,
			state[1] + entry[0] * sign,
			state[2] + entry[1] * sign,
			state[3] + entry[2],
			state[4] + entry[3])
	
	reachable = {(0, 0, 0, 0, 0): 1}
	for _ in range(LIMIT):
		newreachable = {}
		for (state, ways) in reachable.items():
			acwst = move(state, +1)
			cwst  = move(state, -1)
			newreachable[acwst] = newreachable.get(acwst, 0) + ways
			newreachable[cwst ] = newreachable.get(cwst , 0) + ways
		reachable = newreachable
	
	ans = sum(reachable.get((dir, 0, 0, 0, 0), 0) for dir in range(5))
	return str(ans)


ANTICLOCKWISE_MOVES = (
	( 0, -1,  0, +1),
	(-1,  0, +1, -1),
	( 0,  0, -2,  0),
	(+1,  0, +1, -1),
	( 0, +1,  0, +1),
)


if __name__ == "__main__":
	print(compute())