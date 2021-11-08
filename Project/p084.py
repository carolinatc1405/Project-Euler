# 
# Solução para o problema do Projeto Euler 84


import random


# Este é um algoritmo estatístico de aproximação de amostragem que simplesmente simula o jogo para um número fixo de rolos de dados.
# Um algoritmo exato envolveria o cálculo do auto-vetor do maior valor próprio da matriz de transição (o que é prático),
# mas calculando a média sobre todas as possíveis permutações tanto da Chance como do convés da Comunidade (o que é computacionalmente inviável).
def compute():
	TRIALS = 10**7
	
	visitcounts = [0] * 40
	
	chance = CardDeck(16)
	communitychest = CardDeck(16)
	consecutivedoubles = 0
	location = 0
	
	for i in range(TRIALS):
		# Rolar dados tetraédricos
		die0 = random.randint(1, 4)
		die1 = random.randint(1, 4)
		consecutivedoubles = (consecutivedoubles + 1) if (die0 == die1) else 0
		if consecutivedoubles < 3:
			location = (location + die0 + die1) % 40
		else:
			location = 30
			consecutivedoubles = 0
		
	
		if location in (7, 22, 36):  
			card = chance.next_card()
			if   card == 0:  location =  0
			elif card == 1:  location = 10
			elif card == 2:  location = 11
			elif card == 3:  location = 24
			elif card == 4:  location = 39
			elif card == 5:  location =  5
			elif card in (6, 7): 
				location = (location + 5) // 10 % 4 * 10 + 5
			elif card == 8:
				location = 28 if (12 < location < 28) else 12
			elif card == 9:
				location -= 3
			else:
				pass
		elif location == 30: 
			location = 10
		else:
			pass
		
		if location in (2, 17, 33):
			card = communitychest.next_card()
			if   card == 0:  location =  0
			elif card == 1:  location = 10
		
		visitcounts[location] += 1
	
	temp = sorted(enumerate(visitcounts), key=(lambda ic: -ic[1]))
	ans = "".join("{:02d}".format(i) for (i, c) in temp[ : 3])
	return str(ans)



class CardDeck(object):

	def __init__(self, size):
		self.cards = list(range(size))
		self.index = size
	
	def next_card(self):
		if self.index == len(self.cards):
			random.shuffle(self.cards)
			self.index = 0
		result = self.cards[self.index]
		self.index += 1
		return result


if __name__ == "__main__":
	print(compute())